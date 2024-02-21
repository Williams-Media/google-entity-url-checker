# Web Content Entity Analyzer

## Description
This Python script extracts text from a specified URL and analyzes entities within the text using Google Cloud's Natural Language API. It identifies entities, their types, and salience scores, then outputs the results into a CSV file. This tool is useful for SEO, content analysis, and understanding the context of web pages.

## Features
- Text extraction from web pages
- Entity analysis using Google Cloud Natural Language API
- Results exported to a CSV file with entity names, types, and salience scores

## Prerequisites
Before running this script, ensure you have the following:
- Python 3.x installed
- `requests` and `beautifulsoup4` packages installed for web scraping
- `google-cloud-language` package installed for entity analysis
- A Google Cloud account with the Natural Language API enabled and a service account key

## Installation
1. Clone this repository or download the script.
2. Install the required Python packages:
   ```bash
   pip install requests beautifulsoup4 google-cloud-language  ```
3. Set up your Google Cloud service account and download the service account key JSON file.

##Usage
- Set the service_account_path variable in the script to the path of your Google service account key JSON file.
- Run the script from the command line:
```bash
python entity_analyzer.py ```
- When prompted, enter the full URL of the web page you want to analyze.

##Output
The script will generate a CSV file named entity_analysis_results.csv in the same directory, containing the entities found in the web page, their types, and their salience scores.


<center>❤️ <a href="https://williamsmedia.co">Williams Media SEO Team</a></center>
