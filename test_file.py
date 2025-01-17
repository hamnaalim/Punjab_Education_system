

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
url = ['https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=334--Chiniot',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=371--Attock',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=383--Mianwali',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=373--Rawalpindi',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=374--Chakwal',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=382--Khushab',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=372--Jhelum',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=381--Bhakkar',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=384--Sargodha',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=346--Mandi%20Bahauddin',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=342--Gujrat',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=321--D.G.Khan',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=322--Layyah',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=345--Hafizabad',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=341--Gujranwala',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=343--Sialkot',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=332--Jhang',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=333--Toba%20Tek%20Singh',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=331--Faisalabad',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=356--Nankana%20Sahib',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=354--Sheikhupura',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=344--Narowal',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=323--Muzaffargarh',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=364--Khanewal',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=391--Sahiwal',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=393--Okara',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=352--Lahore',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=351--Kasur',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=361--Multan',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=366--Lodhran',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=363--Vehari',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=392--Pakpattan',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=313--Rahim%20Yaar%20Khan',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=312--Bahawalpur',
        'https://schoolportal.punjab.gov.pk/sed_census/new_emis_details.aspx?distId=311--Bahawalnagar'
        ]


csv_filename = ['Chiniot_school_data.csv',
                'Attock_school_data.csv',
                'Mianwali_school_data.csv',
                'Rawalpindi_school_data.csv',
                'Chakwal_school_data.csv',
                'Khushab_school_data.csv',
                'Jhelum_school_data.csv',
                'Bhakkar_school_data.csv',
                'Sargodha_school_data.csv',
                'Mandi-Bahauddin_school_data.csv',
                'Gujrat_school_data.csv',
                'D.G.Khan_school_data.csv',
                'Layyah_school_data.csv',
                'Hafizabad_school_data.csv',
                'Gujranwala_school_data.csv',
                'Sialkot_school_data.csv',
                'Jhang_school_data.csv',
                'Toba-Tek-Singh_school_data.csv',
                'Faisalabad_school_data.csv',
                'Nankana-Sahib_school_data.csv',
                'Sheikhupura_school_data.csv',
                'Narowal_school_data.csv',
                'Muzaffargarh_school_data.csv',
                'Khanewal_school_data.csv',
                'Sahiwal_school_data.csv',
                'Okara_school_data.csv',
                'Lahore_school_data.csv',
                'Kasur_school_data.csv',
                'Multan_school_data.csv',
                'Lodhran_school_data.csv',
                'Vehari_school_data.csv',
                'Pakpattan_school_data.csv',
                'Rahim-Yaar-Khan_school_data.csv',
                'Bahawalpur_school_data.csv',
                'Bahawalnagar_school_data.csv'
]

# 🔹 Step 2: Fetch and Clean Text
for i in range(len(url)):
    print("Fetching data for: ", csv_filename[i])
    cleaned_lines = fetch_and_clean_text(url[i])

    if not cleaned_lines:
        print("Skipping ",csv_filenames[i]," due to an error.")
        continue

    try:
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


        df.to_csv(csv_filename[i], index=False, encoding="utf-8")

        print("data added to",csv_filename[i]," successfully")

    except ValueError:
        print(f"Skipping {csv_filename[i]}: 'emiscode' not found in data.")
    except Exception as e:
        print(f"An unexpected error occurred while processing {csv_filename[i]}: {e}")

print("Data extraction completed successfully!")
