import lib.process_methods as pm
import swifter


def preprocess(dataframe):
    """
    Preprocessing pipeline for cleaning the 'news_sample.csv' dataset
    """

    # remove empty content
    dataframe.dropna(subset=['content'], inplace=True)

    # cleanup text on 'content' column and add into new column 'content_clean'
    dataframe['content'] = dataframe['content'].swifter.apply(pm.clean_text)

    # Apply remove_stopwords to 'content_clean' column and create 'content_stopword' column
    dataframe['content'] = dataframe['content'].swifter.apply(pm.remove_stopwords)

    # stemming
    dataframe['content'] = dataframe['content'].swifter.apply(pm.remove_word_variations)

    return None