# This code runs in IPython
# All contents are based on Udacity's Deep Learning course.
# [Full source](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/udacity/1_notmnist.ipynb)

from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import tarfile
from IPython.display import display, Image
from scipy import ndimage
from sklearn.linear_model import LogisticRegression
from six.moves.urllib.request import urlretrieve  # This code runs in IPython
from six.moves import cPickle as pickle    # This code runs in IPython

%matplotlib inline

url = 'http://commondatastorage.googleapis.com/books1000/'
last_percent_reported = None

def download_progress_hook(count, blockSize, totalSize):
# To report the progress of a download
	global last_percent_reported
	percent = int(count * blockSize * 100 / totalSize)

	if last_percent_reported != percent:
		if percent % 5 = 0:
			sys.stdout.write("%s%%" % percent)
			sys.stdout.flush()									# What is the difference with flush and print?
		else:
			sys.stdout.write(".")
			sys.stdout.flush()

		last_percent_reported = percent

def maybe_download(filename, expected_bytes, force=False): 							# What is 'force'?
# Download a file, make sure it's the right size
	if force or not os.path.exists(filename):
		print('Attempting to download:', filename)
		filename, _ = urlretrieve( url + filename, filename, reporthook = download_progress_hook)
		print('\nDownload Complete!')
	statinfo = os.stat(filename) 										# Scan File status 
	if statinfo.st_size == expected_bytes:									# statinfo.st_size = file size
		print('Found and verified', filename)
	else:
		raise Exception('Failed to verify ' + filename + '. Can you get to it with a browser?')
	return filename

train_filename = maybe_download('notMNIST_large.tar.gz', 247336696)
test_filename = maybe_download('notMNIST_small.tar.gz', 8458043)


