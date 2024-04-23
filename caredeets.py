import csv
import random

# Sample data for random generation
sample_languages = ['English', 'Spanish', 'French', 'German', 'Chinese']
sample_experience_years = ['1', '2', '3', '4', '5']
sample_experience_with_age = ['Infant', 'Toddler', 'Preschooler', 'School-Age', 'Teenager']
sample_job_types = ['Nanny', 'Babysitter', 'Tutor', 'Au Pair', 'Childminder']
sample_certifications = ['CPR', 'First Aid', 'Early Childhood Education', 'Special Needs Care', 'Child Development Associate']
sample_availability = ['Full-time', 'Part-time', 'Flexible']
sample_pet_compatibility = ['Dog', 'Cat', 'Fish', 'Bird', 'Reptile']

# Function to generate random data
def generate_random_data(id):
    return [
        id,
        random.choice(sample_languages),
        random.choice(sample_experience_years),
        random.choice(sample_experience_with_age),
        random.choice(sample_job_types),
        random.choice(sample_certifications),
        random.choice(sample_availability),
        random.choice(sample_pet_compatibility)
    ]

# Define column names
columns = ['id', 'languages_you_speak', 'years_of_experience', 'experience_with_age',
           'job_type', 'certifications', 'availability', 'pet_compatibility']

# Define number of records
num_records = 10

# Generate data for CSV file
data = [columns]  # Add column headers
for i in range(1, num_records + 1):
    data.append(generate_random_data(i))

# Write data to CSV file
csv_filename = 'caregiver_details_sample.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(data)

print(f"CSV file '{csv_filename}' created successfully with random data.")
