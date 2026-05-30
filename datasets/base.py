from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, List

class BaseDataset(ABC):
    """
    Abstract base class for all dataset implementations.
    
    This class defines the interface that all concrete datasets must follow,
    ensuring consistency across different dataset implementations.
    """
    
    def __init__(self, data_path: str, **kwargs):
        """
        Initialize the dataset.
        
        Args:
            data_path: Path to the dataset directory or file
            **kwargs: Additional arguments specific to the dataset
        """
        self.data_path = data_path
        self.data = None
        self.metadata = {}
    
    @abstractmethod
    def load(self):
        """
        Load the dataset from the specified path.
        
        This method must be implemented by all subclasses to define
        how the specific dataset should be loaded.
        
        Returns:
            The loaded dataset (format depends on implementation)
        
        Raises:
            NotImplementedError: If not implemented by subclass
            FileNotFoundError: If data path doesn't exist
        """
        raise NotImplementedError("Subclasses must implement the load() method")
    
    @abstractmethod
    def __len__(self) -> int:
        """
        Return the number of samples in the dataset.
        
        Returns:
            int: Total number of samples
        """
        raise NotImplementedError
    
    @abstractmethod
    def __getitem__(self, idx: int) -> Dict[str, Any]:
        """
        Get a single sample from the dataset.
        
        Args:
            idx: Index of the sample to retrieve
        
        Returns:
            dict: A sample containing images, text, metadata, etc.
        """
        raise NotImplementedError
    
    def get_metadata(self) -> Dict[str, Any]:
        """
        Get metadata about the dataset.
        
        Returns:
            dict: Metadata such as number of samples, classes, etc.
        """
        return self.metadata
    
    def validate(self) -> bool:
        """
        Validate that the dataset is properly loaded.
        
        Returns:
            bool: True if dataset is valid, False otherwise
        """
        return self.data is not None and len(self) > 0