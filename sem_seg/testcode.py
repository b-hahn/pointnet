import os
import sys
import numpy as np
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(ROOT_DIR, 'utils'))
import data_prep_util
import indoor3d_util

print BASE_DIR
print ROOT_DIR
np.set_printoptions(threshold = np.nan)

num_point = 4096
block_size=1.0
stride=1.0
random_sample=False
sample_num=None
sample_aug=1
mesh = data_prep_util.load_ply_data_rgb('/home/ben/Downloads/mesh.ply', num_point)
print mesh.shape

data, label = indoor3d_util.room2blocks_plus_normalized(mesh, num_point, block_size, stride,
                                       random_sample, sample_num, sample_aug)

i = 0
for color in data[1]:
    i += 1
    if np.sum(color[3:6]) > 0:
        print color.shape
print i