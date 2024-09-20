import pandas as pd

def save_data(data):
    df = pd.DataFrame(data)
    df.to_csv('github_data.csv', index=False)

def load_data():
    try:
        df = pd.read_csv('github_data.csv')
        return df
    except FileNotFoundError:
        return "No previous data found."
