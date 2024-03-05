import lib.process_methods as pm


def preprocess(dataframe) -> None:
    """
    Preprocessing pipeline for cleaning up the data
    """

    # cleanup text on 'content' column and add into new column 'content_clean'
    dataframe['content_clean'] = dataframe['content'].apply(pm.clean_text)

    # Apply remove_stopwords to 'content_clean' column and create 'content_stopword' column
    dataframe['content_stopword'] = dataframe['content_clean'].apply(pm.remove_stopwords)

    # stemming
    dataframe['content_stem'] = dataframe['content_stopword'].apply(pm.remove_word_variations)

    return None
