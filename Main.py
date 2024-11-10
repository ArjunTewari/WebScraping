# from bs4 import BeautifulSoup
# import pandas as pd
# import requests
# import re
# import time
# import random
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer
#
# # Load the Excel file
# file_path = "C:/Users/hp/OneDrive/Desktop/christmas list december 18th 2022 w numbers .xlsx"
# df = pd.read_excel(file_path, engine='openpyxl')
# names = df['NAME'].tolist()
#
# # Function to search Google and retrieve bio information
# def fetch_info_google_search(name):
#     search_url = f"https://www.google.com/search?q={name.replace(' ', '+')}+biography"
#     headers = {
#         "User-Agent": "Mozilla/5.0"
#     }
#     try:
#         response = requests.get(search_url, headers=headers, timeout=10)
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, 'html.parser')
#             bio_snippet = " ".join([span.get_text() for span in soup.find_all('span')])
#             return bio_snippet[:500]  # Limit to 500 characters
#         else:
#             return "No relevant information found."
#     except Exception as e:
#         print(f"Error fetching info for {name} from Google search: {e}")
#         return "Error fetching bio."
#
# def summarize_text(text, sentence_count=2):
#     parser = PlaintextParser.from_string(text, Tokenizer("english"))
#     summarizer = LsaSummarizer()
#     summary = summarizer(parser.document, sentence_count)
#     return " ".join(str(sentence) for sentence in summary)
#
# # Generate bios and add to DataFrame
# def create_short_bio(name):
#     info = fetch_info_google_search(name)
#     short_bio = summarize_text(info)
#     return short_bio
#
# df['Short Bio'] = df['NAME'].apply(create_short_bio)
#
# # Save to new Excel file
# output_file = 'C:/Users/hp/PycharmProjects/FirstpythonProject/final.xlsx'
# df.to_excel(output_file, index=False)
# print("Biographical details added successfully to the Excel file!")


import openai
import pandas as pd

# Set your OpenAI API key
openai.api_key = "HIDDEN"

# Update file paths
file_path = "C:/Users/hp/OneDrive/Desktop/christmas list december 18th 2022 w numbers  - Copy.xlsx"
output_path = "C:/Users/hp/PycharmProjects/FirstpythonProject/final.xlsx"

# Load the Excel file
df = pd.read_excel(file_path)

# Function to generate a biography using OpenAI API with gpt-3.5-turbo
def generate_biography(name, email):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that generates brief info snippet about works using information on wikipedia and linkedin."},
                {"role": "user", "content": f"Write a short, to the point 30 word informational paragraph about the person work and achievements for {name}."}
            ],
            max_tokens=50,
            temperature=0.9
        )
        biography = response.choices[0].message['content']
        return biography
    except Exception as e:
        print(f"Error generating biography for {name}: {e}")
        return "Biography not available."

# Apply the biography generation function to each row, passing both NAME and CATEGORY columns
df["Biography"] = df.apply(lambda row: generate_biography(row["NAME"], row["Email"]), axis=1)

# Save the updated file
df.to_excel(output_path, index=False)
print(f"Updated Excel file saved as {output_path}")






