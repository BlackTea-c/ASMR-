# 处理文本首先词嵌入  就是把原本离散的文本词 映射到实数域！


import collections
import math
import random
import sys
import time
import os
import numpy as np
import torch
from torch import nn
import torch.utils.data as Data

sys.path.append("..")

print(torch.__version__)
