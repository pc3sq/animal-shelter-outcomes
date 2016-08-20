

This repo contains all the work created by Peter Ching in building a data pipeline and classification model for the Kaggle challenge entitled [Shelter Animal Outcomes](https://www.kaggle.com/c/shelter-animal-outcomes). The Kaggle challenge asked participants to create 

The work primarily breaks down to four steps:
1. exploratory data analysis
2. data cleaning
3. feature selection and extraction
4. modeling 

Steps were repeated as necessary as new discoveries were made along the way to the final model submitted to Kaggle.

Jupyter Notebook was the primary environment used in prototyping the data pipeline and classification model. Numpy, Pandas, MatPlotLib and Seaborn were used to clean, select, and extract features from the raw data. Scikit-Learn's gradient boosting classifier model was chosen based on its superior cross validation score and its ability to improve iteratively on misclassified outcomes caused by the imbalance of outcome classes. A hyperparamter optimization with grid searching was performed for a final tweak before submitting the predicted probabilities to Kaggle for ranking.

Note that the data contain target leaking features like SubOutcomes which mapped directly to their respective Outcomes (aka the labels/target) and AgeUponOutcome which is data we would not have access to until an outcome occurred. Some Kagglers exploited these features to acheive higher rankings but the model created herein  many of the higher ranking participants of this Kaggle challenge exploited target leaking features like SubOutcomes that map directly to their respective Outcomes and 

Jupyter Notebook, Pandas, Numpy, MatPlotLib, Seaborn, Scikit-Learn, gradient boosting, class imbalances, hyperparameter optimization with grid searching, cross validation, and log loss are among the technologies used and concepts covered in preparing the data and creating the final model.



# Contents of This Repository

This respository contains the Jupyter Notebooks, Python scripts, and data visualizations used in building a full data pipeline and trained gradient boosting model for the Kaggle Challenge entitled 

Here are the contents of each folder:
+ data/ contains the original raw data and cleaned/transformed datasets
+ figures/ contains png files of MatPlotLib and Seaborn created data visualizations
+ models/ contains pickled iterations of the classification model
+ src/ contains miscellaneous scripts used in the data pipeline



# Overview: Shelter Animal Outcomes Challenge On Kaggle.com

The Shelter Animal Outcomes Kaggle challenge asked each participating team to create a classfication model that predicts the outcome of each cat or dog that ends up at a ['Return_to_owner' 'Euthanasia' 'Adoption' 'Transfer' 'Died']



['AgeuponOutcome', 'AnimalID', 'AnimalType', 'Breed', 'Color', 'DateTime', 'Name', 'OutcomeSubtype', 'OutcomeType', 'SexuponOutcome']


