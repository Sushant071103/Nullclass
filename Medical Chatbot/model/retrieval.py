# model/retrieval.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Retriever:
    def __init__(self, questions):
        """
        Initializes the Retriever with a list of questions.

        Args:
            questions (list): List of question strings.
        """
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.question_vectors = self.vectorizer.fit_transform(questions)
        self.questions = questions

    def retrieve_best_answer(self, user_query, qa_dataframe):
        """
        Retrieves the most similar question and returns its answer.

        Args:
            user_query (str): User's input query.
            qa_dataframe (pd.DataFrame): DataFrame containing questions and answers.

        Returns:
            str: Best matching answer.
        """
        user_query_vec = self.vectorizer.transform([user_query])
        similarities = cosine_similarity(user_query_vec, self.question_vectors)
        best_match_idx = similarities.argmax()

        return qa_dataframe.iloc[best_match_idx]["answer"]
