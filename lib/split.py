import pandas as pd
import numpy as np

def eighty_ten_ten(df: pd.DataFrame) -> None:
    """
    Splitting a pandas dataframe into 80/10/10 split: 80% traning data, 10% validation data, and 10% test data.
    The splitting is done by uniformly selecting random rows. Each split is saved as new csv files in 'data' subfolder.
    """
    
    # initialize dataframes
    training_data = pd.DataFrame()
    validation_data = pd.DataFrame()
    test_data = pd.DataFrame()

    # training data split into 80/20
    # random_state saves the state of the random selection. This means it can be reproduced.
    training_data = df.sample(frac=0.8, random_state=0)
    # training_data = df.sample(frac=0.8)

    # remaining data
    remaining_data = df.drop(training_data.index)

    # validation data
    validation_data = remaining_data.sample(frac=0.5, random_state=1)
    # validation_data = remaining_data.sample(frac=0.5)


    # test data
    test_data = remaining_data.drop(validation_data.index)

    # save as csv files
    training_data.to_csv('data/training_data.csv')
    validation_data.to_csv('data/validation_data.csv')
    test_data.to_csv('data/test_data.csv')
    
    return None