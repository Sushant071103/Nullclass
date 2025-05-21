# utils/preprocessing.py

import pandas as pd

def load_medquad_data(data_folder_path):
    """
    Loads the clean MedQuAD CSV file containing question-answer pairs.

    Args:
        data_folder_path (str): Path to the data folder (example: "data/medquad/").

    Returns:
        pd.DataFrame: DataFrame containing 'question' and 'answer' columns.
    """
    csv_path = f"{data_folder_path}/medquad_clean.csv"
    
    try:
        df = pd.read_csv(csv_path)

        # Optional Check: If there are unwanted spaces or wrong columns
        df.columns = [col.strip().lower() for col in df.columns]

        # Check if required columns exist
        if 'question' not in df.columns or 'answer' not in df.columns:
            raise ValueError("CSV does not contain 'question' and 'answer' columns.")

        return df

    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return pd.DataFrame(columns=["question", "answer"])
