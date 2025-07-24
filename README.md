# UDA-TCL
UDA-TCL (Unsupervised Domain Adaptation Time patch Contrastive Learning) is a novel framework for time series domain adaptation that addresses distribution shifts between source and target domains through a dual-branch architecture combining contrastive learning and time patch convolution.

# Key Features:
**Cross-Domain Contrastive Learning**: Bidirectional alignment strategy treating source and target domain samples as queries and keys

**Time Patch Convolutional Network**: Hierarchical dual-pathway architecture separating local and global temporal feature learning

**Clustering-Based Pseudo-Labeling**: Source domain knowledge-guided target domain label generation

**Dual-Branch Architecture**: Joint optimization of source domain classification and cross-domain alignment


# Datasets

Due to file size limitations, datasets are not included directly in this repository. Please download the datasets using the provided setup script:

```bash
python setup_datasets.py
```

## Dataset Sources:

1. HAR: UCI Human Activity Recognition Using Smartphones Dataset

2. HHAR: UCI Heterogeneity Activity Recognition Dataset
   
3. AR: WISDM Activity Recognition Dataset (Laboratory)
   
4. AT: WISDM Activity Recognition Dataset (Real-world)


## Manual Download Links:

1. UCI HAR Dataset: https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones

2. UCI HHAR Dataset: https://archive.ics.uci.edu/dataset/344/heterogeneity+activity+recognition

3. WISDM Datasets: https://www.cis.fordham.edu/wisdm/dataset.php



# Experimental Scenarios
**Single Domain Shift**: Individual differences in human activity recognition

**Multiple Domain Shift**: Complex scenarios involving laboratory-to-real-world adaptation 

# Code Availability
The complete source code implementation will be made publicly available upon paper acceptance. This repository currently contains the datasets, preprocessing utilities, and experimental setup to facilitate reproducibility.

# Reproducibility 
This repository contains the datasets and basic processing scripts used in our experiments. Complete implementation code will be made available upon paper acceptance.
