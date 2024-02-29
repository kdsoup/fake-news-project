import re
import pandas as pd
from cleantext import clean
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

nltk.download('punkt')
nltk.download("stopwords")


def clean_text(text: str) -> str:
    """
    Clean the data
    """

    # Replace dates with <DATE> (assuming date format MM DD,YYYY (fx Jan. 8, 2017 or april 4, 1999))
    text = re.sub('(?:[a-zA-Z]+)\.?\s+[0-9]{1,2},\s+[0-9]{4}', '_DATE_', text)

    # Remove multiple white spaces, tabs, new lines
    text = re.sub(' +|\n+|\t+',' ', text)
    
    text = clean(text,
        lower=True,                    # lowercase text
        no_urls=True,                  # replace all URLs with a special token
        no_emails=True,                # replace all email addresses with a special token
        no_numbers=True,               # replace all numbers with a special token      
        replace_with_url="_URL_",
        replace_with_email="_EMAIL_",
        replace_with_number="_NUM_"            
    )

    return text


def remove_stopwords(text: str) -> str:
    """
    Tokenize text and remove stopwords
    """

    stop_words = set(stopwords.words('english'))

    # Tokenize the input text
    word_tokens = nltk.word_tokenize(text)

    # Filter out stopwords
    filtered_sentence = [w for w in word_tokens if w.lower() not in stop_words]

    # Join the filtered words back into a single string
    nostop_text = ' '.join(filtered_sentence)

    return nostop_text


def remove_word_variations(text: str) -> str:
    """
    Remove word variations, stemming
    """

    # Initialize a SnowballStemmer with English language
    stemmer = SnowballStemmer("english")
    
    # Tokenize the input text
    word_tokens = nltk.word_tokenize(text)
    
    # Stem each word token
    stemmed_words = [stemmer.stem(word) for word in word_tokens]
    
    # Join the stemmed words back into a single string
    stemmed_text = ' '.join(stemmed_words)
    
    return stemmed_text


def preprocess(dataframe):
    """
    Preprocessing pipeline for cleaning the data
    """

    # remove empty content
    dataframe.dropna(subset=['content'], inplace=True)

    # cleanup text on 'content' column and add into new column 'content_clean'
    dataframe['content'] = dataframe['content'].apply(clean_text)

    # Apply remove_stopwords to 'content_clean' column and create 'content_stopword' column
    dataframe['content'] = dataframe['content'].apply(remove_stopwords)

    # stemming
    dataframe['content'] = dataframe['content'].apply(remove_word_variations)

    return dataframe
