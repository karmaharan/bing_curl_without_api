

# bing_curl_without_api

## Overview
The `search_and_fetch` Python script allows users to perform Bing searches and extract detailed information from top search results. It utilizes web scraping techniques with `requests` and `BeautifulSoup` to fetch titles, descriptions, links, and main content from search results. Users can select specific search results to retrieve additional details such as titles, meta descriptions, and further content from the linked pages.

## Features
- Conduct Bing searches based on user input queries.
- Extract titles, descriptions, links, and main content from search results.
- Select specific search results to fetch detailed information from linked pages.
- Provides a straightforward method for analyzing and extracting web data directly from Bing search outputs.

## Usage
1. **Installation:**
   - Clone the repository:
     ```
     git clone https://github.com/karmaharan/bing_curl_without_api/
     ```
   
2. **Dependencies:**
   - Install required Python packages:
     ```
     pip install requests beautifulsoup4
     ```

3. **Execution:**
   - Run the script and follow the prompts:
     ```
     python app.py
     ```
   - Enter a search query when prompted, choose a result to fetch additional details.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer
This script is for educational purposes and should be used responsibly. It relies on web scraping, which may be subject to terms of service of the search engine provider (e.g., Bing). Ensure compliance with legal and ethical guidelines when using this script.

