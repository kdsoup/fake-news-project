# fake-news-project

To install the package requirements for the miniconda enviroment, use the following command:

    ```bash
    conda create -y -n "fake-news-proj" python=3.12
    conda activate fake-news-proj
    pip install -r requirements.txt
    ```

### Data Files

- 'news_sample.csv' file is available at: https://raw.githubusercontent.com/several27/FakeNewsCorpus/master/news_sample.csv
- '995,000_rows.csv' file is available at: https://absalon.ku.dk/courses/72550/files/8102667?wrap=1
- 'articles.csv' is available in the 'data' folder

### Reproduction Pipeline for Model Results

Please follow the pipeline below to reproduce all data files to get results for the models

    ```
    Pipline:
        1_preprocessing.ipynb
        2_process_baseline_features.ipynb
        4_process_liar_data.ipynb
        sentence_transformer.ipynb
    ```