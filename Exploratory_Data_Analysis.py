# IMPORT LIBRARIES
import pylab as p
from scipy.stats import skew
from scipy.stats import kurtosis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# LOAD THE DATA SET
mat = pd.read_csv("student-mat.csv", sep=';')
por = pd.read_csv("student-por.csv", sep=';')

# MERGE THE DATASET INTO A SINGLE DATAFRAME
student = pd.concat([mat, por], ignore_index=True)


# MEAN SCORES FOR VARIABLES
def mean_score(final):
    return np.mean(final)


# MEDIAN SCORES FOR SOME VARIABLES
def median_scores(data):
    return np.median(data)


# STANDARD DEVIATION FOR SOME VARIABLES
def std_score(data):
    return np.std(data)


# VARIANCE FOR SOME VARIABLES
def variance(data):
    return np.var(data)


# MINIMUM VALUE
def minimum(data):
    return np.min(data)


# MAXIMUM VALUE
def maximum(data):
    return np.max(data)


# SKEW
def skew_point(data):
    return skew(data)


# KURTOSIS
def kurt_point(data):
    return kurtosis(data)
