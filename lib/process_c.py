import lib.process_methods as pm
import pandas as pd


def preprocess(dataframe) -> None:
    """
    Preprocessing pipeline for cleaning up the data
    """

    # vocabulary size of uncleaned text
    pm.vocabulary_size(dataframe, 'content', 'content_vocabulary_size')

    # cleanup text in 'content' column
    dataframe['content'] = dataframe['content'].apply(pm.clean_text)

    # Remove stopwords
    dataframe['content'] = dataframe['content'].apply(pm.remove_stopwords)

    # Compute the size of vocabulary after removing stop words, and compute the reduction rate
    pm.vocabulary_size(dataframe, 'content', 'stopword_vocabulary_size')
    pm.reduction_rate(dataframe, 
                      'content_vocabulary_size', 
                      'stopword_vocabulary_size',
                      'stopword_reduction_rate'
                      )

    # stemming
    dataframe['content'] = dataframe['content'].apply(pm.remove_word_variations)

    # Compute the size of vocabulary after stemming, and compute the reduction rate
    pm.vocabulary_size(dataframe, 'content', 'stem_vocabulary_size')
    pm.reduction_rate(dataframe, 
                      'content_vocabulary_size', 
                      'stem_vocabulary_size',
                      'stem_reduction_rate'
                      )

    return None