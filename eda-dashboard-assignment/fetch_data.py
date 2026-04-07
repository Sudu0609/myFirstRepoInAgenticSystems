import requests
import pandas as pd

def fetch_and_process_data():
    # Fetch data
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Cleaning
    df = df.rename(columns={"userId": "user_id"})
    df = df.drop(columns=["id"])

    # New column
    df["post_length"] = df["body"].apply(len)

    # Grouping
    posts_per_user = df.groupby("user_id").size()

    return df, posts_per_user


# Test
if __name__ == "__main__":
    df, posts_per_user = fetch_and_process_data()
    print(df.head())
    print(posts_per_user)