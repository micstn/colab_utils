from __future__ import print_function

import sys
if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import keras

# http://pytorch.org/
from os import path
from wheel.pep425tags import get_abbr_impl, get_impl_ver, get_abi_tag
platform = '{}{}-{}'.format(get_abbr_impl(), get_impl_ver(), get_abi_tag())
accelerator = 'cu80' if path.exists('/opt/bin/nvidia-smi') else 'cpu'
import torch

# Install the PyDrive wrapper & import libraries.
# This only needs to be done once per notebook.
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

# Authenticate and create the PyDrive client.
# This only needs to be done once per notebook.
def colab_auth():  
    auth.authenticate_user()
    gauth = GoogleAuth()
    gauth.credentials = GoogleCredentials.get_application_default()
    drive = GoogleDrive(gauth)

def get_gdrive_csv(file_id):
  # colaboratory - read csv from google drive to pandas dataframe
  get_file = drive.CreateFile({'id': file_id})
  file_content = get_file.GetContentString()
  df = pd.read_csv(StringIO(file_content), sep="\t")
  return df

def save_gdrive_csv():
  uploaded = drive.CreateFile({'title': 'Sample file.txt'})
  uploaded.SetContentString('Sample upload file content')
  uploaded.Upload()
  print('Uploaded file with ID {}'.format(uploaded.get('id')))
