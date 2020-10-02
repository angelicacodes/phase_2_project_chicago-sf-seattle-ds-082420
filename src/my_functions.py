import pandas as pd
import numpy as np
import zipfile

def map_Y_N(x):
    x = x.map({'Y' : 1, 'N' : 0})
    return x

def test():
    return 12