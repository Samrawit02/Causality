# Causality
Perform Casualty Inference on Brest cancer data set using Judea Pearl and his research groups framework.

# Table of content
- [Introduction](#introduction)
- [Folders](#folders)
  - [data](#data)
  - [scripts](#scripts)
  - [notebooks](#notebooks)
  - [tests](#tests)
## Introduction
A common frustration in the industry, especially when it comes to getting business insights from tabular data, is that the most interesting questions (from their perspective) are often not answerable with observational data alone. These questions can be similar to:
- “What will happen if I halve the price of my product?”
- “Which clients will pay their debts only if I call them?”

Judea Pearl and his research group have developed in the last decades a solid theoretical framework to deal with that, but the first steps toward merging it with mainstream machine learning are just beginning.
## Installation
- Install Packages
```
git clone 
cd Causality
pip install -r requriements.txt
```

- Jupyter Noteboks
```
cd notebooks
jupyter notebook
```
#### data: 
folder containing the data set of breast cancer downloaded from [kaggle](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data). The data set contain about 570 rows and 33 columns.

#### scripts:
This folder contain python modules. The main purpose of this forlder is for code modularization and increase code reusability. 


- ```clean_data.py``` : python module concerned with cleaning data frame. operation include filling null values, droping columns and others.
- ```visualization.py``` : python module concerned with generating graphs and plots from provided data frame.

#### notebooks:
This folder contain notebooks files that are necessary for data exploration and to get more indepth analysis on the data set.
- ```EDA``` : Notebook file for making exploratory data analysis and help us understand more about the data.