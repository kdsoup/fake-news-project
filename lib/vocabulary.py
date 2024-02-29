import pandas as pd
import nltk



# compute stopword reduction rate. add vocabulary columns and reduction rate column to csv file
def stopword_reduction_rate(filename: str) -> None:
    df = pd.read_csv(filename)

    for i in range(len(df.index)):
        content_clean_vocabulary_size = len(set(nltk.word_tokenize(df.content_clean[i])))
        content_stopword_vocabulary_size = len(set(nltk.word_tokenize(df.content_stopword[i])))
        decrease = content_clean_vocabulary_size - content_stopword_vocabulary_size
        reduction_rate = (decrease/content_clean_vocabulary_size) * 100
        df.at[i, 'content_clean_vocabulary_size'] = content_clean_vocabulary_size
        df.at[i, 'content_stopword_vocabulary_size'] = content_stopword_vocabulary_size
        df.at[i, 'content_stopword_reduction_rate'] = round(reduction_rate, 3)
    
    df.to_csv(filename)

    # # Printing results for each row
    # for index, row in df.iterrows():
    #     print(f"{index} Clean Vocab Size: {row['content_clean_vocabulary_size']}, Stopword Vocab Size: {row['content_stopword_vocabulary_size']}, Reduction Rate: {row['content_stopword_reduction_rate']}")
    
stopword_reduction_rate('data/news_sample_cleaned.csv')

def vocabulary_size(text: str) -> int:
    size = -1

    
    return size




# compute stopword reduction rate. add vocabulary columns and reduction rate column to csv file
def stopword_reduction_rate(text: str) -> float:

    for i in range(len(df.index)):
        content_clean_vocabulary_size = len(set(nltk.word_tokenize(df.content_clean[i])))
        content_stopword_vocabulary_size = len(set(nltk.word_tokenize(df.content_stopword[i])))
        decrease = content_clean_vocabulary_size - content_stopword_vocabulary_size
        reduction_rate = (decrease/content_clean_vocabulary_size) * 100
        df.at[i, 'content_clean_vocabulary_size'] = content_clean_vocabulary_size
        df.at[i, 'content_stopword_vocabulary_size'] = content_stopword_vocabulary_size
        df.at[i, 'content_stopword_reduction_rate'] = round(reduction_rate, 3)
    
    df.to_csv(filename)

    # # Printing results for each row
    # for index, row in df.iterrows():
    #     print(f"{index} Clean Vocab Size: {row['content_clean_vocabulary_size']}, Stopword Vocab Size: {row['content_stopword_vocabulary_size']}, Reduction Rate: {row['content_stopword_reduction_rate']}")
    
stopword_reduction_rate('data/news_sample_cleaned.csv')


# compute size of vocabulary after stemming. Add column with 'stem vocabulary size' to the csv file
def stemming_reduction_rate(filename: str) -> None:
    df = pd.read_csv(filename)

    for i in range(len(df.index)):
        stem_vocabulary_size = len(set(nltk.kword_tokenize(df.content_stem[i])))
        clean_vocabulary_size = len(set(nltk.word_tokenize(df.content_clean[i])))
        decrease = clean_vocabulary_size - stem_vocabulary_size
        reduction_rate = (decrease/clean_vocabulary_size) * 100
        df.at[i, 'content_stem_vocabulary_size'] = stem_vocabulary_size
        df.at[i, 'content_stem_reduction_rate'] = round(reduction_rate, 3)

    df.to_csv(filename)
    # # Printing results for each row
    # for index, row in df.iterrows():
    #     print(f"{index} Clean Vocab Size: {row['content_clean_vocabulary_size']}, Stopword Vocab Size: {row['content_stopword_vocabulary_size']}, Reduction Rate: {row['content_stopword_reduction_rate']}, Stem Vocabulary Size: {row['content_stem_vocabulary_size']}, Stem Reduction Rate: {row['content_stem_reduction_rate']}")

stemming_reduction_rate('data/news_sample_cleaned.csv')