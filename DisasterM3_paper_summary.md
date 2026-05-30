# Task 7 – DisasterM3 Paper Summary

## 1. Problem Statement

There is no unified modular framework for disaster because of existing approaches rely on lightweight benchmark scripts and loosely modular implementations and also the complexity of disaster scenes with diverse disaster types, geographic regions and satellite sensors posed new challenges for VLM applications.

## 2. Solution

By building a modular codebase for disaster analysis from remote sensing data, focused on evaluation and benchmarking of multimodal vision-language models by datasets, model and tasks.

## 3. Experimentation

The author evaluated 14 VLMs models both generic and remote sensing models. The dataset defines 9 disaster related task ranging from disaster bearing body recognition, structural damage assessment, Object relational reasoning, long form disaster report generation. The findings of these showed lack of a disaster-specific corpus, cross-sensor gap, and damage object counting insensitivity. They found four VLMs using disasterM3 dataset and was able to achieve stable improvements across all tasks, with robust cross-sensor and cross-disaster generalization capabilities.