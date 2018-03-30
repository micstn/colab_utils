from __future__ import print_function

import sys
if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO

import os
import getpass
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from google.colab import files
from google.colab import auth

# https://keras.io/
os.system("pip install -q keras")
import keras

# Mount google drive
os.system("apt-get install -y -qq software-properties-common python-software-properties module-init-tools")
os.system("add-apt-repository -y ppa:alessandro-strada/ppa 2>&1 > /dev/null")
os.system("apt-get update -qq 2>&1 > /dev/null")
os.system("apt-get -y install -qq google-drive-ocamlfuse fuse")

# Authenticate and create the PyDrive client.
# This only needs to be done once per notebook.
def colab_auth():  
    auth.authenticate_user()
    gauth = GoogleAuth()
    gauth.credentials = GoogleCredentials.get_application_default()
    drive = GoogleDrive(gauth)

def colab_mount_gdrive():
    auth.authenticate_user()
    from oauth2client.client import GoogleCredentials
    creds = GoogleCredentials.get_application_default()
    os.system("google-drive-ocamlfuse -headless -id={creds.client_id} -secret={creds.client_secret} < /dev/null 2>&1 | grep URL")
    vcode = getpass.getpass()
    os.system("echo {vcode} | google-drive-ocamlfuse -headless -id={creds.client_id} -secret={creds.client_secret}")


