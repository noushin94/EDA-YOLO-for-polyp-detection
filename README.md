# 🚀 Dissertation Project: Enhancing YOLOv8 for Polyp Detection in Colonoscopy Images

![YOLOv8](https://img.shields.io/badge/Yolo-v8-brightgreen)
![Deformable Convolution](https://img.shields.io/badge/Deformable-Convolution-blue)
![Polyp Detection](https://img.shields.io/badge/Polyp-Detection-orange)

This repository has been created for my dissertation project, which focuses on modifying the YOLOv8 model architecture to improve its performance in detecting polyps in colonoscopy images. The primary modification involves incorporating deformable convolution in place of simple convolution in the bottleneck of the C2f block.

## 📑 Table of Contents
- [Key Components and Concepts](#key-components-and-concepts)
  - [Deformable Convolution](#deformable-convolution)
  - [Bottleneck of YOLOv8](#bottleneck-of-yolov8)
  - [C2f Block of the YOLO Model](#c2f-block-of-the-yolo-model)
- [Repository Structure](#repository-structure)
- [Usage](#usage)
- [Results](#results)
- [Conclusion](#conclusion)
- [Acknowledgements](#acknowledgements)

## 🔍 Key Components and Concepts

### Deformable Convolution
Deformable convolution is an advanced variant of the traditional convolution operation. It introduces additional offsets to the standard convolution grid, allowing it to adapt to geometric variations of objects in images. This adaptability helps in better capturing and representing irregular shapes and structures, which is particularly useful in medical imaging for detecting anomalies like polyps.

### Bottleneck of YOLOv8
The bottleneck structure in the YOLOv8 architecture is designed to reduce the dimensionality of the feature maps while preserving essential information. This is achieved through a series of convolutional layers that compress the input features into a more compact representation. By integrating deformable convolution into this bottleneck, the model gains enhanced flexibility and accuracy in feature extraction.

### C2f Block of the YOLO Model
The C2f (Cross-Stage Partial Fusion) block is a critical component of the YOLO model architecture. It connects multiple stages of the network, enabling a more efficient flow of information and features across different layers. This block facilitates better feature fusion and helps in maintaining high detection accuracy. In this study, the simple convolution within the C2f block's bottleneck has been replaced with deformable convolution to further boost the model's performance.

## 📁 Repository Structure
```bash
Kvasir/        # Contains the dataset used for training and testing
nn/blocks/      # Includes the modified YOLOv8 model architecture
notebooks/   # Jupyter notebooks for exploratory data analysis and visualization





