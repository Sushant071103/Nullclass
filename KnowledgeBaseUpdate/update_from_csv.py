import pandas as pd
from update_knowledge import add_to_knowledge_base

def update_knowledge_from_csv(csv_file):
    # Read new Q&A pairs from the CSV file
    df = pd.read_csv(csv_file)

    # Loop through each row and add the new Q&A pairs to the knowledge base
    for _, row in df.iterrows():
        new_intent = {
            "tag": row['tag'],
            "patterns": row['patterns'].split(';'),  # Assume patterns are semicolon-separated
            "responses": row['responses'].split(';')
        }
        add_to_knowledge_base(new_intent)

# Example usage
update_knowledge_from_csv('new_qa_pairs.csv')
