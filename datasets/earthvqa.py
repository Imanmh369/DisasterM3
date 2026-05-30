from .base import BaseDataset
import json
from pathlib import Path


class EarthVQADataset(BaseDataset):
    """
    EarthVQA Dataset Adapter
    
    Loads satellite imagery with VQA (Visual Question Answering) pairs.
    Format: Images + Questions + Answers
    """
    
    def __init__(self, dataset_path, split='train', **kwargs):
        """
        Initialize EarthVQA dataset.
        
        Args:
            dataset_path (str): Path to the dataset root directory
            split (str): Data split - 'train', 'val', or 'test'
            **kwargs: Additional arguments
        """
        self.dataset_path = dataset_path
        self.split = split
        self.data = []
        self.load()
    
    def load(self):
        """
        Override the abstract method from BaseDataset.
        Read the annotation file (JSON) and load images and Q&A pairs.
        """
        # Construct paths
        annotation_file = Path(self.dataset_path) / 'annotations' / f'{self.split}.json'
        self.image_dir = Path(self.dataset_path) / 'images'
        
        # Load annotations
        with open(annotation_file, 'r') as f:
            self.data = json.load(f)
    
    def __len__(self):
        """Return number of samples in the dataset."""
        return len(self.data)
    
    def __getitem__(self, idx):
        """
        Return one sample: {image, question, answer, metadata}.
        
        Args:
            idx (int): Index of the sample
            
        Returns:
            dict: Contains 'image', 'question', 'answer', 'image_id'
        """
        sample = self.data[idx]
        
        # Load image
        image_path = self.image_dir / sample['image_id']
       
        
        # Return sample
        return {
            'question': sample['question'],
            'answer': sample['answer'],
            'image_id': sample['image_id']
        }