# Task 4 – Minimal Execution Notes

## 1. Dependencies
The script `scripts/run_inference.py` required the following dependencies:

- **numpy** → numerical operations  
- **torch** → PyTorch deep learning framework  
- **torchvision** → image transforms and interpolation modes  
- **transformers** → Hugging Face library for models, processors, tokenizers  
- **pillow (PIL)** → image loading and processing (`pip install pillow`)  
- **tqdm** → progress bar for loops (`pip install tqdm`)  
- **vllm** → inference engine (`pip install vllm`)  
- **decord** → video reading utility (`pip install decord`)  
- **qwen_vl_utils** → custom utility (not available on PyPI, likely part of repo or needs manual setup)

Installation attempt:
```bash
pip install numpy torch torchvision transformers pillow tqdm vllm decord
