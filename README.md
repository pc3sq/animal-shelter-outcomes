# Submission For Shelter Animal Outcomes Kaggle Challenge

The [Shelter Animal Outcomes](https://www.kaggle.com/c/shelter-animal-outcomes) Kaggle challenge asked participants to create a classification model that predicts the outcomes of animals (e.g. ['Return_to_owner' 'Euthanasia' 'Adoption' 'Transfer' 'Died']) that ended up in an animal shelter using predictors like age, color, species, and breed. Shelter caregivers would use this classification model to identify at risk animals that need additional attention and care to achieve favorable outcomes. This repo contains all the work created by Peter Ching in building a data pipeline and classification model for this Kaggle challenge.

Broadly, the steps taken to build out the data pipeline and model included:
1. exploratory data analysis
2. data cleaning
3. feature selection and extraction
4. modeling

Jupyter Notebook was the primary environment used in prototyping the data pipeline and classification model. Numpy, Pandas, MatPlotLib and Seaborn were used for exploratory data analysis, data preparation (cleaning, tranforming, etc.), and feature selection and extraction. Scikit-Learn's gradient boosting classifier model was chosen based on its superior cross validation score (least overfitted) and its ability to improve iteratively on misclassified outcomes caused by the imbalance of outcome classes. Hyperparameter optimization with grid searching was performed for a final tweak before submitting the predicted probabilities to Kaggle for ranking.

Note that the original raw data contained target leaking features like SubOutcomes which mapped directly to their respective Outcomes (aka the labels/target) and AgeUponOutcome which is data we would not have access to until the outcome occurred. Some Kagglers exploited these features to acheive higher rankings but the model created herein removed the Suboutcomes feature and treated the AgeUponOutcome feature as a simple current age feature when training the classification model.

The contents of each folder are:
+ `data/` contains the original raw data and cleaned/transformed data
+ `figures/` contains PNG files of MatPlotLib and Seaborn created data visualizations
+ `models/` contains pickled iterations of the classification model
+ `notebooks-development/` contains the Jupyter Notebooks used in creating the data pipeline and models
+ `src/` contains custom Python scripts used in the data pipeline

To begin exploring this repo, I recommend starting with the `notebooks-developments/` folder and following the chronologically named notebooks to understand the path leading up to how the final model was built.
