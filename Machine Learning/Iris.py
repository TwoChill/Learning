# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/ #


# Load libraries

import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

import os
import time
os.system('clear')

# Load dataset
# This dataset has 5 collums. The 5th coloum is the species of the flower.

# This is the URL for the acctual dataset CSV file.
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'

# Here you'll specifiy the names of each colum.
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

# Here you'll load the dataset with pandas.
dataset = pandas.read_csv(url, names=names)

# SHAPE

print('>>> This is the data inside the Iris dataset <<<\n\n', dataset)
print('\n>>> The shape of the dataset is:', dataset.shape)
