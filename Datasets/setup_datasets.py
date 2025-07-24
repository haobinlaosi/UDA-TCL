#!/usr/bin/env python3
"""
Dataset setup script for UDA-TCL experiments
Downloads and organizes HAR, HHAR, AR, and AT datasets
"""

import os
import urllib.request
import zipfile
from pathlib import Path

def download_datasets():
    """Download and extract required datasets"""
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    datasets = {
        "HAR": "https://archive.ics.uci.edu/ml/machine-learning-databases/00240/UCI%20HAR%20Dataset.zip",
        "HHAR": "https://archive.ics.uci.edu/ml/machine-learning-databases/00344/Activity%20recognition%20exp.zip",
        # Add other dataset URLs
    }
    
    for name, url in datasets.items():
        print(f"Downloading {name} dataset...")
        # Download and extract logic here
        
if __name__ == "__main__":
    download_datasets()
