import csv
import random

# Sample data for random generation
sample_descriptions = ['Single Parent', 'Mom and Dad', 'Dads', 'Single Mom', 'Single Dad']
sample_family_names = ['Doe', 'Smith', 'Johnson', 'Brown', 'Taylor']
sample_languages = ['English', 'Spanish', 'French', 'German', 'Chinese']
sample_years_experience = ['1', '2', '3', '4', '5']
sample_children = ['1', '2', '3', '4', '5']
sample_neighborhoods = ['Suburban', 'Urban', 'Rural']
sample_interests = ['Music', 'Art', 'Sports', 'Science', 'Cooking']

# Function to generate random data
def generate_random_data(id):
    return [
        id,
        random.choice(sample_descriptions),
        random.choice(sample_family_names),
        random.choice(sample_languages),
        random.choice(sample_years_experience),
        random.choice(sample_children),
        random.choice(sample_neighborhoods),
        random.choice(sample_interests)
    ]

# Define column names
columns = ['id', 'describe_your_family', 'family_name', 'languages_you_speak',
           'expected_years_of_experience', 'children_you_have',
           'what_neighborhood_you_live_in', 'what_are_your_interest_creative']

# Define number of records
num_records = 10

# Generate data for CSV file
data = [columns]  # Add column headers
for i in range(1, num_records + 1):
    data.append(generate_random_data(i))

# Write data to CSV file
csv_filename = 'family_details_sample.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(data)

print(f"CSV file '{csv_filename}' created successfully with random data.")
