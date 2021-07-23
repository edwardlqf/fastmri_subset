from pathlib import Path
import os
import shutil
import argparse
import numpy as np

def split(path, precentage, seed):
    subset_size = precentage / 100 #precentage of total data

    np.random.seed(seed)
    
    artifact_path = Path(path)
    subest_path = Path(artifact_path, 'subset')

    #create subset folder
    if not os.path.exists(subest_path):
        os.mkdir(subest_path)

    for folder in os.listdir(artifact_path):
        if folder != 'subset':
            files = [name for name in os.listdir(Path(artifact_path, folder))] 

            subset_count = int(np.floor(len(files) * subset_size))
            subset_files = np.random.choice(files, size = subset_count, replace = False)

            for file in subset_files:
                src = Path(artifact_path, folder, file)
                dst = Path(subest_path, folder)
                if not os.path.exists(dst):
                    os.mkdir(dst)
                shutil.copy(src, dst)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Creates subset of fastMRI data")
    parser.add_argument('--path', type=Path, help="Path to datasets.", required=True)
    parser.add_argument("--precentage", type=int, nargs='?', default=10, help="enter as precentage, 100 means 100% of the dataset")
    parser.add_argument('--seed', type=int, nargs='?', default=123)
    
    args = parser.parse_args()
    
    split(args.path, args.precentage, args.seed)