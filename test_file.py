

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def fetch_and_clean_text(url):
    """
    Fetches and cleans data from the given URL by removing extra spaces and newlines.
    """
    try:
        # Fetch the HTTP response
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text with line breaks for better readability
        text_content = soup.get_text(separator='\n').strip()

        # Normalize multiple newlines (convert multiple `\n` to a single `\n`)
        clean_text = re.sub(r'\n+', '\n', text_content)

        return clean_text.split("\n")  # Split into a list of lines

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# 🔹 Step 1: Define the Target URL
url = "https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=334--Chiniot"

# 🔹 Step 2: Fetch and Clean Text
cleaned_lines = fetch_and_clean_text(url)
ind=cleaned_lines.index('emiscode')
cleaning=cleaned_lines[ind:]
cleaning.remove("Location")
#print(cleaning)

headers = cleaning[:5]
#print(headers)

data = cleaning[5:]
#print(data)

structured_data = [data[i:i+5] for i in range(0, len(data), 5)]

# Convert to a dictionary (list of dictionaries)
data_dicts = [dict(zip(headers, row)) for row in structured_data]

# Convert to a DataFrame
df = pd.DataFrame(data_dicts)
print(df)

csv_filename = "structured_school_data.csv"
df.to_csv(csv_filename, index=False, encoding="utf-8")

print("data added to csv successfully")