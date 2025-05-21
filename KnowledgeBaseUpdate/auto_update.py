import schedule
import time
from update_from_csv import update_knowledge_from_csv

# Function to fetch and add new data to the knowledge base (for now, you can use a predefined CSV file or any source)
def periodic_update():
    # Example: Automatically add a new Q&A pair (this can be fetched from an external file or API)
    new_intent = {
        "tag": "headache",
        "patterns": ["How can I relieve a headache?", "What are the symptoms of a headache?"],
        "responses": ["You can relieve a headache by drinking water, resting, and using over-the-counter medication."]
    }
    add_to_knowledge_base(new_intent)

# Schedule periodic updates (every 24 hours in this case)
schedule.every(24).hours.do(periodic_update)

# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)  # Wait for 1 second before checking again
