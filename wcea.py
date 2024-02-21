import requests
import os
from bs4 import BeautifulSoup
from google.cloud import language_v1
import csv

def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Remove script and style elements
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()
    # Get text
    text = soup.get_text(separator=' ', strip=True)
    return text

def analyze_entities(text, client):
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    response = client.analyze_entities(document=document)
    return [(entity.name, entity.type_.name, entity.salience) for entity in response.entities]

def main(url):
    # Set the path to your service account key file here
    service_account_path = "/root/vscode1/sunny-dialect-297820-87c5682c2e2e.json"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_path

    # Initialize the Google Cloud client with your credentials
    client = language_v1.LanguageServiceClient()

    text = extract_text_from_url(url)
    entities = analyze_entities(text, client)
    
    # Specify the CSV file name
    csv_filename = "entity_analysis_results.csv"

    # Write data to CSV
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['Entity', 'Type', 'Salience'])

        # Write the entity data
        for name, type_, salience in entities:
            writer.writerow([name, type_, salience])

    print(f"Results saved to {csv_filename}")

if __name__ == "__main__":
    url = input("Enter the URL: ")
    main(url)
