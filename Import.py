import os
import re
from scipy import ndimage, misc
from skimage.transform import resize, rescale
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)

from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D
from tensorflow.keras.layers import Conv2DTranspose, UpSampling2D, add
from tensorflow.keras.models import Model
from tensorflow.keras import regularizers
import tensorflow as tf
tf.compat.v1.logging.set_verbosity (tf.compat.v1.logging.ERROR)
print('Using tensorflow version', tf.__version__)

