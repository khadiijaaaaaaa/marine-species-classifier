# 🐠 FathomNet 2025 Challenge: Hierarchical Classification of Ocean Life

This repository contains my solution for the [FathomNet 2025 Challenge](https://fathomnet.org/), focused on hierarchical image classification of marine organisms using deep learning. The goal was to build a model that understands the **taxonomic hierarchy** of marine species and predicts the most confident level (from Kingdom to Species) based on the input image.

## 🧠 Problem Overview

Unlike flat classification, this challenge requires **hierarchical classification**. A prediction is scored based on how far it deviates from the correct taxonomic label in the hierarchy. Predictions closer to the true label receive better scores.

- **Example:** If the true label is "Apostichopus leukothele" (species), predicting "Apostichopus" (genus) is better than predicting "Stichopodidae" (family).

## 🗂 Project Structure

```
.
marine-species-cliassifier/
├── notebook.ipynb                  # Full pipeline in Jupyter Notebook
├── taxonomy_hierarchy.json        # Generated using GBIF API
├── submission.csv                 # Final model predictions
├── best_model.pt                  # Saved PyTorch model weights
├── README.md                      # Project description and instructions
├── requirements.txt               # Python dependencies for the whole project
└── utils/
    └── download.py                # Script to download COCO-formatted images (not included)
    └── dataset_train.json         # COCO-formatted annotations for training set
    └── dataset_test.json          # COCO-formatted annotations for test set
    └── requirements.txt           # Requirements specifically for downloading script

```

> ⚠️ **Note:** The training and testing images are not included in this repository. Follow the dataset instructions below to download them using the provided COCO-format annotation files.

## 🧾 Dataset Overview

- Format: COCO-style object detection JSON files
- Categories: 79 marine organism classes
- Each image is annotated with bounding boxes and associated taxonomy info

### How to Download Images

Images are not hosted directly due to licensing. Instead, use the provided script to download them using `coco_url`:

```bash
pip install -r requirements.txt
python utils/download.py dataset/dataset_train.json data/train
python utils/download.py dataset/dataset_test.json data/test
```

## ⚙️ Setup and Configuration

Install dependencies:

```bash
pip install timm gdown opencv-python pandas numpy matplotlib scikit-learn tqdm torch torchvision
```

Then download and unzip the dataset via Google Drive (if you're not using `download.py`):

```python
import gdown
url = 'https://drive.google.com/uc?id=YOUR_FILE_ID'
gdown.download(url, 'fathomnet.zip', quiet=False)
!unzip fathomnet.zip -d ./data/
```

## 🧬 Taxonomic Hierarchy

I built a complete taxonomic tree (from **Kingdom** to **Species**) using the **GBIF API**. This allowed me to implement:

- Hierarchical label encoding
- Fallback predictions at higher levels (if confidence is low)

Stored in `taxonomy_hierarchy.json`.

## 🔨 Pipeline Highlights

- Built using PyTorch and `timm` EfficientNet backbones
- Multi-head architecture (one head per taxonomic level)
- Custom hierarchical loss function averaging the loss at each taxonomic level
- Fallback inference strategy: If low confidence at "species", fallback to "genus", and so on

## 🧪 Evaluation Strategy

- Custom metric: Score = distance between predicted and true label in taxonomy tree
- Goal: Minimize taxonomic distance (0 is best, 12 is worst)

## 📄 Submission Format

```csv
annotation_id,concept_name
1,Apostichopus
2,Ophiuroidea
...
```

## 📌 Notes

- Training/validation split was 90/10
- Early stopping after 3 validation stagnations
- Model checkpoints saved with best validation score

## 🙏 Acknowledgements

- [FathomNet](https://fathomnet.org/) & MBARI for the dataset
- [GBIF](https://www.gbif.org/) for taxonomic data
- PyTorch, timm, and torchvision for the deep learning stack

---
