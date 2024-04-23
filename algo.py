import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load family details and caregiver details CSV files into pandas DataFrames
family_df = pd.read_csv('family_details.csv')
caregiver_df = pd.read_csv('caregiver_details.csv')

# Get family criteria
family_criteria = family_df.iloc[0]

# Prepare texts for TF-IDF vectorization
texts = [family_criteria['languages_you_speak'], family_criteria['expected_years_of_experience'],
         family_criteria['children_you_have'], family_criteria['what_neighborhood_you_live_in'],
         family_criteria['what_languages_your_family_speak'], family_criteria['your_expectation_for_job_commitment'],
         family_criteria['your_child_has_difference'], family_criteria['what_pets_are_part_of_your_family'],
         family_criteria['what_are_your_interest_creative'], family_criteria['what_are_your_interest_percussion_instrument'],
         family_criteria['what_are_your_interest_string_instrument'], family_criteria['what_are_your_interest_woodwind_instrument'],
         family_criteria['what_are_your_interest_brass_instrument'], family_criteria['what_are_your_interest_sport'],
         family_criteria['what_are_your_interest_stem'], family_criteria['what_is_your_household_diet'],
         family_criteria['what_is_your_household_religion'], family_criteria['educational_parenting_philosophy'],
         family_criteria['has_require_your_caregiver_age_range'], family_criteria['how_often_you_need_a_caregiver'],
         family_criteria['what_arrangement_you_prefer'], family_criteria['days_hours_of_your_caregiver'],
         family_criteria['responsibilities_require_caregiver_childcare'], family_criteria['responsibilities_require_caregiver_household'],
         family_criteria['how_you_plan_to_pay_caregiver'], family_criteria['plan_to_pay_caregiver_min'],
         family_criteria['plan_to_pay_caregiver_max'], family_criteria['plan_to_pay_caregiver_salary_base'],
         family_criteria['payment_method_to_pay_caregiver'], family_criteria['user_benefits_you_offering_show_on_profile'],
         family_criteria['benefits_you_offering'], family_criteria['prompt_and_answer_know_us'],
         family_criteria['prompt_and_answer_know_us_details'], family_criteria['prompt_and_answer_know_me_details'],
         family_criteria['prompt_and_answer_kids_talking'], family_criteria['prompt_and_answer_kids_talking_details'],
         family_criteria['prompt_and_answer_childcare'], family_criteria['prompt_and_answer_childcare_details'],
         family_criteria['youd_like_caregiver_to_know']]

# Replace NaN values with empty strings in the family DataFrame
texts = [str(text) for text in texts]

print(texts)
# Vectorize texts using TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(texts)

# Calculate cosine similarity between family criteria and caregiver profiles
similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])

print(similarity_scores.shape)  # Print the shape of similarity_scores
print(similarity_scores)  # Print the content of similarity_scores
sorted_indices = similarity_scores.argsort()[0][::-1]  # Check if this line causes the issue

# Find indices of caregivers sorted by similarity score (descending)
sorted_indices = similarity_scores.argsort()[0][::-1]

# Output the matched caregivers
matched_caregivers = caregiver_df.iloc[sorted_indices - 1]  # Subtract 1 to account for 0-based indexing
print(matched_caregivers)
