# Task 6 – Reuse Analysis (EarthVQA)

## 1. Overview
Earth vision research has traditionally focused on detecting and categorizing geospatial objects, but often neglects the exploration of relations between objects and comprehensive reasoning. To address this gap, **EarthVQA** was developed as a multi‑modal, multi‑task Visual Question Answering (VQA) dataset that advances relational reasoning for city planning and governance needs.

The dataset contains:
- 6,000 satellite images  
- Corresponding semantic masks  
- 208,593 question–answer pairs  

To support complex reasoning tasks such as judging, counting, and relational analysis, EarthVQA introduces the **Semantic Object Awareness (SOBA) framework**. SOBA is object‑centric and leverages:
- A segmentation network to preserve refined spatial locations and semantics.  
- Object‑guided attention to aggregate features within objects.  
- Bidirectional cross‑attention to model relations between objects hierarchically.  
- A numerical difference loss to improve object counting by unifying classification and regression tasks.  

Experimental results show that SOBA outperforms both advanced general VQA methods and specialized remote sensing approaches. Together, EarthVQA and SOBA provide a strong benchmark for complex Earth vision analysis, particularly in urban and rural governance contexts.

---

## 2. Reusable Design Pattern: Dataset Interface
A key reusable design pattern in EarthVQA is the dataset interface pattern. Instead of embedding dataset logic directly into scripts, EarthVQA defines a base dataset class and then implements specific loaders for each dataset. This ensures consistency in how data is accessed, preprocessed, and passed to models.

Example:
```python
class BaseDataset:
    def load(self):
        raise NotImplementedError

class EarthVQADataset(BaseDataset):
    def load(self):
        # Load image-question pairs
        ...
