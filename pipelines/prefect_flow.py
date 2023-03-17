from prefect import flow, task
import pandas as pd


@task
def load_file_to_db(file):
    return pd.read_csv(file)


@task
def split_url(df):
    df['domain_of_url'] = df['url'].str.extract('//(?:www\.)?(.*?)/')
    return df


@task
def copy_to_file(norm):
    norm.to_csv('pipelines/data/result.csv', index=False)


@flow
def prefect():
    df = load_file_to_db('pipelines/data/data.csv')
    df = split_url(df)
    copy_to_file(df)


if __name__ == "__main__":
    prefect()
