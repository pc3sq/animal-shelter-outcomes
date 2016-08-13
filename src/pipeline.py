import pandas as pd, numpy as np
from .extract_color import multi_dog, multi_cat, patterned_dog, patterned_cat


def age_to_days(age_str):
    age_val = int(str(age_str).split()[0])

    if "day" in age_str or "days" in "age_str":
        return age_val
    elif "week" in age_str or "weeks" in "age_str":
        return age_val * 7
    elif "month" in age_str or "months" in "age_str":
        return age_val * 30
    elif "year" in age_str or "years" in "age_str":
        return age_val * 365
    elif age_str == "0" or "0 years": # new conditional
        return 0
    else:
        return "unknownAge"


def cleaning_pipeline(df):
    dframe = df.copy()

    if 'OutcomeSubtype' in dframe.columns:
        dframe = dframe.drop(['OutcomeSubtype'], axis=1)

    print dframe.columns

    dframe['Name'] = dframe['Name'].fillna(value="noName")

    # simply fillna with "0" for AgeuponOutcome
    dframe['AgeuponOutcome'] = dframe['AgeuponOutcome'].fillna(value="0")

    # no longer dropping "Unknown" in SexuponOutcome
    dframe['SexuponOutcome'] = dframe['SexuponOutcome'].fillna(value='Unknown')

    if np.any(dframe.isnull() > 0):
        for col in dframe.columns:
            if sum(dframe[col].isnull()) > 0:
                print "%s contains %d nulls" %(col, sum(dframe[col].isnull()))
    else:
        return dframe


def transform_pipeline(df, test_set=True):
    dframe = df.copy()

    #new treatment of AgeuponOutcome
    # create new ageInDaysAtOutcome from AgeuponOutcome
    dframe['ageInDaysAtOutcome'] = dframe['AgeuponOutcome'].apply(age_to_days)
    # calculate mean age in days without 0s
    mean_age_in_days_no_0s = (dframe[dframe['ageInDaysAtOutcome'] > 0]).mean().values[0]
    # create new hasAge feature from AgeuponOutcome
    dframe['hasAge'] = dframe['ageInDaysAtOutcome'].apply(lambda age: 0 if age==0 else 1)
    # fill 0s in ageInDaysAtOutcome with mean_age_in_days_no_0s
    dframe['ageInDaysAtOutcome'] = dframe['ageInDaysAtOutcome'].apply(lambda age: mean_age_in_days_no_0s if age==0 else age)

    # extract Dog or not dog from AnimalType
    dframe['Dog'] = dframe['AnimalType'].apply(lambda specie: 1 if specie=="Dog" else 0)

    # extract mixed vs. pure for Breed
    dframe['pureBreed'] = dframe['Breed'].apply(lambda breed: 0 if "Mix" in breed or "/" in breed else 1)

    # extract hasName from Name
    dframe['hasName'] = dframe['Name'].apply(lambda name: 0 if name=="noName" else 1)

    # extract Multi-colored from Color for dogs and cats
    dframe['Multi-Colored'] = [multi_dog(row['Color']) if row['Dog']==1 else multi_cat(row['Color']) for i, row in dframe.iterrows()]

    # extract Patterned from Color for dogs and cats
    dframe['Patterned'] = [patterned_dog(row['Color']) if row['Dog']==1 else patterned_cat(row['Color']) for i, row in dframe.iterrows()]

    # convert all values in AgeuponOutcome to days
    dframe['AgeuponOutcome'] = dframe['AgeuponOutcome'].apply(age_to_days)

    # get dummies for non-binary categorical variables
    categoricals = ['SexuponOutcome']
    dframe = pd.get_dummies(dframe, columns=categoricals)

    # return only select columns
    if test_set:
        return dframe.drop(['AnimalType', 'Breed', 'Name', 'DateTime', 'Color'], axis=1)
    else:
        # dropping OutcomeSubtype due to target leakage
        return dframe.drop(['AnimalID', 'AnimalType', 'Breed', 'Name', 'DateTime', 'Color'], axis=1)
