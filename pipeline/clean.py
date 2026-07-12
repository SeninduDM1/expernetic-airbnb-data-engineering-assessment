import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def remove_empty_columns(df):
    missing_percentage = df.isnull().mean() * 100
    columns_to_drop = missing_percentage[
        missing_percentage == 100
    ].index

    return df.drop(columns=columns_to_drop)

def clean_price(df):
    df["price"] = (
        df["price"]
        .str.replace("$", "", regex=False)
    )

    df["price"] = pd.to_numeric(
        df["price"],
        errors="coerce"
    )

    return df

def save_data(df, path):
    df.to_csv(path, index=False)

def main():
    df = load_data("data/raw/listings.csv.gz")
    clean_df = remove_empty_columns(df)
    clean_df = clean_price(clean_df)
    save_data(clean_df, "data/processed/listings_clean.csv")
    print("Cleaning pipeline completed successfully!")

if __name__ == "__main__":
    main()