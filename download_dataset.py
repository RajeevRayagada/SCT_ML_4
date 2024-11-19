import kagglehub
import zipfile
import os
import shutil

# Define the target extraction directory
target_directory = "C:\\Users\\rajee\\SCT_ML_4"

# Define the dataset path in the cache
cache_directory = "C:\\Users\\rajee\\.cache\\kagglehub\\datasets\\gti-upm\\leapgestrecog\\versions\\1"

# Check if the dataset already exists in the cache directory
if os.path.exists(cache_directory):
    print("Dataset already downloaded. Extracting to the target directory...")
    
    # If the target directory already has a folder called "1", delete or rename it
    if os.path.exists(target_directory + "\\1"):
        print(f"Warning: {target_directory}\\1 already exists. Renaming it.")
        shutil.move(target_directory + "\\1", target_directory + "\\1_backup")

    # Check if the dataset is a zip file and extract it
    if cache_directory.endswith('.zip'):
        with zipfile.ZipFile(cache_directory, 'r') as zip_ref:
            zip_ref.extractall(target_directory)
    else:
        # Move the dataset files to the target directory
        shutil.move(cache_directory, target_directory)
    
    print(f"Path to dataset files: {target_directory}")
else:
    print("Dataset not found in cache. Downloading...")
    # Download dataset if it doesn't exist
    dataset_name = "gti-upm/leapgestrecog"
    path = kagglehub.dataset_download(dataset_name)
    
    # Extract or move the downloaded dataset to the target directory
    if path.endswith('.zip'):
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(target_directory)
    else:
        shutil.move(path, target_directory)
    
    print(f"Path to dataset files: {target_directory}")
