import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# pre-defined values of the columns
'''
predefined_values = {
        
}
'''

# - right now i have only mapped the highest priority ones
column_mapping = {
    # highest priority (65-80% weight)
    'what_are_your_interest_creative': 'caregiver_interest_creative',
    'plan_to_pay_caregiver_max': 'caregiver_like_pay_max',
    'years_of_experience_require_your_caregiver': 'caregiver_years_of_experience',
    'your_child_difference': 'experience_neurodivergent_children',
    'require_your_caregiver_age_range': 'caregiver_date_of_birth',
    'preference_gender_of_your_caregiver': 'caregiver_gender'}

# dataframe of caregiver details
caregiver_df = pd.read_csv('caregiver_details.csv')

# dataframe of family details
family_df = pd.read_csv('family_details.csv')

# collecting only the columns given in mapping

caregiver_selected_columns = list(column_mapping.values())
caregiver_df = caregiver_df[caregiver_selected_columns]
print(caregiver_df)

family_selected_columns = list(column_mapping.keys())
family_df = family_df[family_selected_columns]
print(family_df)

# replacing null values with empty strings
family_df.fillna('', inplace=True)
caregiver_df.fillna('', inplace=True)

# tf-idf vectorization
texts = family_df.values.tolist()
caregiver_texts = caregiver_df.values.tolist()
print(texts)

# converting each list of strings to a single string
texts = [' '.join(row) for row in texts]
caregiver_texts = [' '.join(row) for row in caregiver_texts]

texts += caregiver_texts

# vectorizing
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(texts)

# fetching selected family record (can be based upon the user id)
family_criteria = family_df.iloc[21]

family_vector = vectorizer.transform([family_criteria])

# calculatin cosine similarity between family criteria and caregiver profiles
similarity_scores = cosine_similarity(family_vector, tfidf_matrix[1:])  #exclude family criteria

#finding indices of caregivers sorted by similarity score (descending)
sorted_indices = similarity_scores.argsort()[0][::-1]

# top 10 matching caregivers (user_id) - incomplete
top_10_caregivers = caregiver_df.iloc[sorted_indices[:10]]
print(top_10_caregivers)
