import pandas as pd

# Load family and caregiver data from CSV files
family_df = pd.read_csv('family_details_sample.csv')
caregiver_df = pd.read_csv('caregiver_details_sample.csv')

# Define common columns for compatibility calculation
common_columns = {
    'languages_you_speak',
    'expected_years_of_experience',  # Family
    'years_of_experience'  # Caregiver
}

# Function to calculate compatibility between a family and a caregiver
def calculate_compatibility(family, caregiver):
    compatibility_score = 0
    for param in common_columns:
        if param == 'expected_years_of_experience':
            if family[param] == caregiver['years_of_experience']:
                compatibility_score += 1
        elif param == 'years_of_experience':
            if family['expected_years_of_experience'] == caregiver[param]:
                compatibility_score += 1
        elif family[param] == caregiver[param]:
            compatibility_score += 1
    return compatibility_score

# Function to find the most compatible caregiver for a family
def find_most_compatible_caregiver(family):
    compatibility_scores = {}
    for _, caregiver in caregiver_df.iterrows():
        caregiver_id = caregiver['id']
        compatibility_scores[caregiver_id] = calculate_compatibility(family, caregiver)
    most_compatible_caregiver_id = max(compatibility_scores, key=compatibility_scores.get)
    return most_compatible_caregiver_id, compatibility_scores[most_compatible_caregiver_id]

# Test the compatibility calculation for the first family
family = family_df.iloc[0]
caregiver_id, compatibility_score = find_most_compatible_caregiver(family)
print(f"The most compatible caregiver for the family is caregiver ID: {caregiver_id} with a compatibility score of {compatibility_score}")

# Calculate compatibility scores for all families and caregivers
compatibility_scores = {}
for _, family in family_df.iterrows():
    family_id = family['id']
    family_scores = {}
    for _, caregiver in caregiver_df.iterrows():
        caregiver_id = caregiver['id']
        family_scores[caregiver_id] = calculate_compatibility(family, caregiver)
    compatibility_scores[family_id] = family_scores

# Print compatibility scores for all families and caregivers
for family_id, family_scores in compatibility_scores.items():
    print(f"Family ID: {family_id}")
    for caregiver_id, compatibility_score in family_scores.items():
        print(f"    Caregiver ID: {caregiver_id}, Compatibility Score: {compatibility_score}")
