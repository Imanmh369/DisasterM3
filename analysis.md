# Task 3 – Repository Structure Analysis

## 1. Current Repository Structure
The current DisasterM3 repository contains the following folders and files:

models/
init.py
pyscripts/
init.py
run_vllm.py
README.md
init.py




### Observations
- The project has two main directories: **models** and **pyscripts**.  
- Each folder includes an `__init__.py` file, indicating Python package initialization.  
- The main script `run_vllm.py` appears to handle model execution or evaluation.  
- The **README.md** file is placed inside `pyscripts` instead of the root directory, which is unconventional.  
- Business logic is embedded inside `__init__.py`, which is not best practice.  
- No clear separation between models, preprocessing, data handling, and evaluation.

---

## 2. Issues in the Current Structure
Several problems were identified in the current layout:

1. **Misuse of `models/__init__.py`**  
   The file contains around 19KB of implementation code instead of just imports. This makes the package hard to maintain, test, and navigate.

2. **Vague module names**  
   The folder `pyscripts` is too generic and does not indicate its purpose. More descriptive names such as `scripts/`, `inference/`, or `evaluation/` would be clearer.

3. **Missing utility organization**  
   Large helper functions (such as video loading and preprocessing) are mixed with model configuration code. There is no separation between preprocessing logic and model logic.

4. **No clear data handling layer**  
   Data loading logic is scattered inside `run_vllm.py` (lines 93–161). There is no dedicated data module to centralize dataset access and prompt templates.

5. **Empty root `__init__.py`**  
   The root package is not properly initialized. This makes imports unclear and inconsistent.

6. **Missing test directory**  
   There is no `tests/` folder, which makes it difficult to validate code quality and ensure reliability.

7. **Unorganized utilities and configs**  
   Hardcoded paths (such as `PROJECT_ROOT` calculation) and embedded prompt templates (lines 21–89 in `run_vllm.py`) should be moved into configuration files or a constants module.

---

## 3. Proposed Modular Structure
A cleaner, scalable structure is recommended:

DisasterM3/
├── __init__.py
├── README.md
├── setup.py or pyproject.toml (missing!)
│
├── disaster_m3/                    # Main package
│   ├── __init__.py
│   │
│   ├── models/                     # Model configurations
│   │   ├── __init__.py
│   │   ├── base.py                 # ModelConfig ABC
│   │   ├── qwen_vl.py              # QwenVL class
│   │   ├── intern_vl.py            # InternVL class
│   │   ├── llava.py                # Llava class
│   │   └── builder.py              # build_model_config()
│   │
│   ├── preprocessing/              # Image/Video utilities
│   │   ├── __init__.py
│   │   ├── image.py                # Image transforms
│   │   └── video.py                # Video loading & processing
│   │
│   ├── data/                       # Data handling
│   │   ├── __init__.py
│   │   ├── loaders.py              # get_messages_from_data()
│   │   └── prompts.py              # PROMPT_TEMPLATES dict
│   │
│   ├── config/                     # Configuration
│   │   ├── __init__.py
│   │   └── paths.py                # Path constants
│   │
│   └── utils/                      # Utilities
│       ├── __init__.py
│       └── constants.py            # Shared constants
│
├── scripts/                        # Executable scripts
│   ├── run_inference.py            # Renamed from run_vllm.py
│   └── evaluate.py                 # Future evaluation script
│
├── tests/                          # Unit tests
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_preprocessing.py
│   └── test_data.py
│
├── configs/                        # Configuration files
│   ├── prompts.yaml               # Prompt templates
│   └── default.yaml               # Default settings
│
└── data/                          # Data directory (not in repo)
    ├── images/
    └── *.json


## 4. Summary
The current repository structure is functional but minimal, with poor use of `__init__.py` files, vague naming, and missing organization for utilities, data handling, and tests.  
By adopting the proposed modular layout, the DisasterM3 project will be easier to maintain, extend, and evaluate. This structure separates concerns clearly, improves readability, and ensures scalability for future development.

