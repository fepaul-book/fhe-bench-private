print(f'script started')

import numpy as np
import math
import os
import pyhelayers
import shutil
from sklearn import datasets
from sklearn.model_selection import train_test_split
from utils import get_used_ram, get_data_sets_dir
from xgboost import XGBClassifier
import pandas as pd

# Print the ciphertext content for demo purposes
pyhelayers.get_print_options().print_encrypted_content=True 
print("Imported pyhelayers", pyhelayers.VERSION)

# process data depending on environment variable

print(f'script finished')
