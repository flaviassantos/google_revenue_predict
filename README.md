# Google Analytics Customer Revenue Prediction
================================================

# Introduction

In this section, I will take an initial look at the Google Analytics Customer Revenue Prediction competition  hosted on [Kaggle](<https://www.kaggle.com/c/google-analytics-customer-revenue-prediction>). I am going to apply a compilation of several formal data pipeline researched (e.g. CRISP-DM, KDD, Azure TDSPD), the fundamental steps to solve any problem in a data science domain used in this project are:

- Step 1 - Understanding Business Objective
- Step 2 - Data Collection & Data Preparation
- Step 3 - Modeling
- Step 4 - Communication

Project Organization
------------

Folder PATH listing for volume Windows
Volume serial number is 842A-D560
C:.
│   .gitignore
│   README.md
│   
├───code
│   │   Readme.md
│   │   
│   ├───Data-Collection
│   │   │   Data Preparation.ipynb
│   │   │   DataPreparation.py
│   │   │   Main.py
│   │   │   
│   │   ├───.ipynb_checkpoints
│   │   │       Business Understanding-checkpoint.ipynb
│   │   │       Data Preparation-checkpoint.ipynb
│   │   │       
│   │   └───__pycache__
│   │           DataPreparation.cpython-36.pyc
│   │           
│   └───Modeling
│           baseline_lgb.csv
│           
├───data
│   ├───external
│   ├───processed
│   │       test_flat.csv
│   │       train_flat.csv
│   │       
│   └───raw
│           sample_submission.csv
│           test.csv
│           train.csv
│           
├───docs
│   │   README.md
│   │   
│   ├───Data-Dictionaries
│   │       data-dictionary-from-sql-table.PNG
│   │       Raw-Data-Dictionary.csv
│   │       ReadMe.md
│   │       
│   ├───Data_Report
│   │       Data Defintion.md
│   │       DataPipeline.txt
│   │       DataSummaryReport.md
│   │       ReadMe.md
│   │       
│   ├───Model
│   │   │   FinalReport.md
│   │   │   README.md
│   │   │   
│   │   ├───Baseline
│   │   │       Baseline Models.md
│   │   │       
│   │   └───Model 1
│   │           Model Report.md
│   │           
│   └───Project
│           Charter.md
│           Exit Report.md
│           README.md
│           System Architecture.docx
│           
├───images
│       rmse.jpg
│       
└───notebooks
        1.0-Business-Understanding.ipynb
        2.0-Exploratory-Data-Analysis.ipynb
        3.0-ML-Model-Baseline-LightGBM.ipynb
        
