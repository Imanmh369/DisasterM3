import os
import json
from typing import Dict, Any, List, Optional
from pathlib import Path
from .base import BaseDataset


class DisasterM3Dataset(BaseDataset):
    """
    Concrete implementation of DisasterM3 dataset.
    
    This class handles loading and accessing the DisasterM3 remote sensing
    vision-language dataset for disaster damage assessment.
    """
    
    def __init__(
        self, 
        data_path: str, 
        subset: Optional[str] = None,
        split: str = "train",
        **kwargs
    ):
        """
        Initialize the DisasterM3Dataset.
        
        Args:
            data_path: Path to the DisasterM3 dataset directory
            subset: Specific subset of data (e.g., 'bearing_body', 'report', etc.)
            split: Data split - 'train', 'val', or 'test'
            **kwargs: Additional arguments
        """
        super().__init__(data_path, **kwargs)
        self.subset = subset
        self.split = split
        self.images = []
        self.annotations = []
        self.instruction_pairs = []
        
    def load(self):
        """
        Load the DisasterM3 dataset from the specified path.
        
        This method:
        1. Validates the data path exists
        2. Loads images and metadata
        3. Loads annotation/instruction pairs
        4. Populates metadata about the dataset
        
        Returns:
            dict: Loaded dataset containing images and annotations
        
        Raises:
            FileNotFoundError: If data path doesn't exist
            ValueError: If dataset format is invalid
        """
        # Validate data path
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Dataset path not found: {self.data_path}")
        
        # Load images
        self._load_images()
        
        # Load annotations and instruction pairs
        self._load_annotations()
        
        # Set metadata
        self.metadata = {
            "dataset_name": "DisasterM3",
            "num_samples": len(self.images),
            "num_annotations": len(self.annotations),
            "subset": self.subset,
            "split": self.split,
            "description": "Remote Sensing Vision-Language Dataset for Disaster Damage Assessment"
        }
        
        # Compile data
        self.data = {
            "images": self.images,
            "annotations": self.annotations,
            "instruction_pairs": self.instruction_pairs
        }
        
        return self.data
    
    def _load_images(self):
        """
        Load all images from the dataset directory.
        
        Expected structure:
        data_path/
        ├── images/
        │   ├── pre_disaster/
        │   └── post_disaster/
        └── annotations/
        """
        images_dir = os.path.join(self.data_path, "images")
        
        if not os.path.exists(images_dir):
            raise FileNotFoundError(f"Images directory not found: {images_dir}")
        
        # Load pre-disaster images
        pre_dir = os.path.join(images_dir, "pre_disaster")
        if os.path.exists(pre_dir):
            for img_file in os.listdir(pre_dir):
                if img_file.endswith(('.png', '.jpg', '.jpeg', '.tif')):
                    self.images.append({
                        "path": os.path.join(pre_dir, img_file),
                        "type": "pre_disaster",
                        "filename": img_file
                    })
        
        # Load post-disaster images
        post_dir = os.path.join(images_dir, "post_disaster")
        if os.path.exists(post_dir):
            for img_file in os.listdir(post_dir):
                if img_file.endswith(('.png', '.jpg', '.jpeg', '.tif')):
                    self.images.append({
                        "path": os.path.join(post_dir, img_file),
                        "type": "post_disaster",
                        "filename": img_file
                    })
    
    def _load_annotations(self):
        """
        Load annotations and instruction pairs from JSON files.
        
        Expected format:
        annotations.json containing list of annotation objects
        instruction_pairs.json containing instruction-response pairs
        """
        annotations_dir = os.path.join(self.data_path, "annotations")
        
        if os.path.exists(annotations_dir):
            # Load main annotations
            annotations_file = os.path.join(annotations_dir, "annotations.json")
            if os.path.exists(annotations_file):
                with open(annotations_file, 'r') as f:
                    self.annotations = json.load(f)
            
            # Load instruction pairs
            instruction_file = os.path.join(annotations_dir, "instruction_pairs.json")
            if os.path.exists(instruction_file):
                with open(instruction_file, 'r') as f:
                    self.instruction_pairs = json.load(f)
    
    def __len__(self) -> int:
        """
        Return the number of samples in the dataset.
        
        Returns:
            int: Total number of image pairs/samples
        """
        if self.data is None:
            return 0
        return len(self.images)
    
    def __getitem__(self, idx: int) -> Dict[str, Any]:
        """
        Get a single sample (image pair + annotations) by index.
        
        Args:
            idx: Index of the sample
        
        Returns:
            dict: Sample containing:
                - image_path: path to image file
                - image_type: 'pre_disaster' or 'post_disaster'
                - annotation: associated annotation/label
                - instruction_pair: question-answer pair (if available)
        
        Raises:
            IndexError: If index is out of range
        """
        if idx < 0 or idx >= len(self):
            raise IndexError(f"Index {idx} out of range for dataset of size {len(self)}")
        
        if self.data is None:
            raise RuntimeError("Dataset not loaded. Call load() first.")
        
        sample = {
            "image": self.images[idx],
            "annotation": self.annotations[idx] if idx < len(self.annotations) else None,
            "instruction_pair": self.instruction_pairs[idx] if idx < len(self.instruction_pairs) else None
        }
        
        return sample
    
    def get_subset_samples(self, subset_name: str) -> List[Dict[str, Any]]:
        """
        Get all samples from a specific subset (e.g., 'bearing_body', 'report').
        
        Args:
            subset_name: Name of the subset
        
        Returns:
            List of samples belonging to the subset
        """
        if self.data is None:
            raise RuntimeError("Dataset not loaded. Call load() first.")
        
        filtered_samples = []
        for i in range(len(self)):
            sample = self[i]
            if sample.get("instruction_pair", {}).get("subset") == subset_name:
                filtered_samples.append(sample)
        
        return filtered_samples
    
    def filter_by_disaster_type(self, disaster_type: str) -> List[Dict[str, Any]]:
        """
        Filter samples by disaster type (e.g., 'flood', 'earthquake', etc.).
        
        Args:
            disaster_type: Type of disaster to filter by
        
        Returns:
            List of samples for the specified disaster type
        """
        if self.data is None:
            raise RuntimeError("Dataset not loaded. Call load() first.")
        
        filtered_samples = []
        for i in range(len(self)):
            sample = self[i]
            if sample.get("annotation", {}).get("disaster_type") == disaster_type:
                filtered_samples.append(sample)
        
        return filtered_samples