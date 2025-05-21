import re
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Step 1: Read chat history
with open("chat_history.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Step 2: Extract all User messages (queries)
user_queries = [line.strip()[4:] for line in lines if line.startswith("You:")]

# Step 3: Count total number of queries
print(f"Total number of user queries: {len(user_queries)}")

# Step 4: Combine all text and extract keywords
all_text = " ".join(user_queries).lower()
words = re.findall(r'\b[a-z]{3,}\b', all_text)  # take only meaningful words (3+ letters)
stopwords = set(["how", "what", "who", "the", "and", "for", "are", "you", "your", "can", "with", "from"])
filtered_words = [word for word in words if word not in stopwords]

word_counts = Counter(filtered_words)
top_words = word_counts.most_common(10)

# Step 5: Convert to DataFrame for plotting
df_words = pd.DataFrame(top_words, columns=["Keyword", "Count"])

# Step 6: Plot bar chart of most common topics
plt.figure(figsize=(10, 6))
sns.barplot(data=df_words, x="Keyword", y="Count", palette="viridis")
plt.title("Top 10 Most Common Topics/Keywords")
plt.xlabel("Keyword")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("dashboard_output/top_keywords.png")
plt.show()

# (Optional Step 7): If ratings are in file as "Rating: X", handle them
# Step 7: Process Ratings (Optional)
ratings = []
for line in lines:
    line = line.strip()
    if line.lower().startswith("rating:"):
        try:
            rating_value = int(line.split(":")[1].strip())
            ratings.append(rating_value)
        except:
            print(f"Invalid rating format found: {line}")

if ratings:
    print(f"Average user satisfaction rating: {sum(ratings)/len(ratings):.2f}")
    rating_df = pd.DataFrame(ratings, columns=["Rating"])
    
    plt.figure(figsize=(6, 6))
    rating_df["Rating"].value_counts().sort_index().plot.pie(
        autopct="%1.1f%%", startangle=140, colors=sns.color_palette("pastel"))
    plt.title("User Satisfaction Rating Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("dashboard_output/ratings_pie_chart.png")
    plt.show()
else:
    print("No satisfaction ratings found.")
