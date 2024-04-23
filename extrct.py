import requests
from bs4 import BeautifulSoup
import csv

# Replace with the actual URL of the caregiver signup page
url = "https://karama.torovin.com/sign_up"

# Ethical reminder: Ensure responsible use of extracted data
print("Ethical Reminder: Extracted data should be used responsibly and ethically, respecting user privacy and intellectual property.")

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all question input elements using class and attribute combination
question_inputs = soup.find_all("input", class_="d-input-text")

# Extract IDs and create header list
ids = [input_element["id"] for input_element in question_inputs]
headers = [""] + ids  # Add an empty column for the first row

# Write to CSV file
with open("caregiver_questions.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write empty row first
    writer.writerow([""] * len(headers))

    # Write column headings
    writer.writerow(headers)

print("CSV file generated successfully!")
