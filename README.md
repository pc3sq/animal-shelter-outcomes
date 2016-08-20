# Submission For Shelter Animal Outcomes Kaggle Challenge by Peter Ching

This repo contains all the work created by Peter Ching in building a data pipeline and classification model for the Kaggle challenge entitled [Shelter Animal Outcomes](https://www.kaggle.com/c/shelter-animal-outcomes). The Kaggle challenge asked participants to create a classification model that predicted the outcome of a given animal that ended up in an animal shelter (e.g. ['Return_to_owner' 'Euthanasia' 'Adoption' 'Transfer' 'Died']). This classification model can be used to identify at risk animals so that shelter caregivers know which animals might require more attention and care to increase their chances of a favorable outcome.

# Explanation of Repository Content

Steps taken to build out the data pipeline and model included:
1. exploratory data analysis
2. data cleaning
3. feature selection and extraction
4. modeling

Jupyter Notebook was the primary environment used in prototyping the data pipeline and classification model. Numpy, Pandas, MatPlotLib and Seaborn were used to clean, select, and extract features from the raw data. Scikit-Learn's gradient boosting classifier model was chosen based on its superior cross validation score and its ability to improve iteratively on misclassified outcomes caused by the imbalance of outcome classes. A hyperparamter optimization with grid searching was performed for a final tweak before submitting the predicted probabilities to Kaggle for ranking.

Note that the data contain target leaking features like SubOutcomes which mapped directly to their respective Outcomes (aka the labels/target) and AgeUponOutcome which is data we would not have access to until an outcome occurred. Some Kagglers exploited these features to acheive higher rankings but the model created herein  many of the higher ranking participants of this Kaggle challenge exploited target leaking features like SubOutcomes that map directly to their respective Outcomes and 

The contents of each folder are:
+ data/ contains the original raw data and cleaned/transformed datasets
+ figures/ contains png files of MatPlotLib and Seaborn created data visualizations
+ models/ contains pickled iterations of the classification model
+ notebooks-development/ contains all the Jupyter Notebooks used in creating the data pipeline and models
+ src/ contains miscellaneous Python scripts used in the data pipeline


