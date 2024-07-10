import requests
from bs4 import BeautifulSoup

def search_and_fetch(query):
    # Define the URL
    url = "https://www.bing.com/search"

    # Parameters for the search query
    params = {
        "q": query
    }

    try:
        # Perform the GET request
        response = requests.get(url, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extracting search results items
            search_results = soup.find_all('li', class_='b_algo')

            # Initialize an empty list to store the extracted data
            extracted_data = []
            page_links = []

            # Iterate over each search result
            for idx, result in enumerate(search_results, start=1):
                # Extract title and description
                title = result.find('h2').get_text() if result.find('h2') else None
                description = result.find('p').get_text() if result.find('p') else None

                # Extract the URL for each result
                link = result.find('a')['href'] if result.find('a') else None
                if link:
                    page_links.append(link)

                # Extract main content (example: paragraphs)
                main_content = []
                paragraphs = result.find_all('p')
                for paragraph in paragraphs:
                    main_content.append(paragraph.get_text())

                # Create a dictionary for each result including title, description, link, and main content
                result_data = {
                    "title": title,
                    "description": description,
                    "link": link,
                    "content": main_content  # Include main content here
                }

                # Append the result dictionary to the extracted_data list
                extracted_data.append(result_data)

                # Print the result with index
                print(f"{idx}. {title} - {description}")

            # Function to handle user input for fetching specific URLs
            def fetch_url(index):
                if 1 <= index <= len(page_links):
                    url_to_curl = page_links[index - 1]
                    # Perform a curl operation or handle as needed
                    print(f"Fetching URL: {url_to_curl}")

                    # Now, perform a GET request to fetch further data from the selected URL
                    response = requests.get(url_to_curl)

                    # Check if the request was successful
                    if response.status_code == 200:
                        # Parse the content of the fetched page
                        soup = BeautifulSoup(response.text, 'html.parser')

                        # Extracting further data (title, meta description, and main content)
                        title = soup.find('title').get_text() if soup.find('title') else None
                        meta_description = soup.find('meta', attrs={'name': 'description'})['content'] if soup.find('meta', attrs={'name': 'description'}) else None

                        # Extract main content (example: paragraphs)
                        main_content = []
                        paragraphs = soup.find_all('p')
                        for paragraph in paragraphs:
                            main_content.append(paragraph.get_text())

                        # Display the extracted data
                        print(f"Title: {title}")
                        print(f"Meta Description: {meta_description}")
                        print("Main Content:")
                        for content in main_content:
                            print(content)

                        # You can further process or display other data as needed

                    else:
                        print(f"Error: Failed to fetch further data from URL. Status code: {response.status_code}")

                else:
                    print("Invalid selection. Please choose a number from the list.")

            # Example: User input (assuming user chooses the first result)
            user_input = input("Enter the number to curl (1, 2, 3, ...): ")
            try:
                selected_index = int(user_input)
                fetch_url(selected_index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        else:
            print(f"Error: Failed to retrieve results. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching search results: {e}")

# Example usage with dynamic query
new_query = input("Enter a new search query: ")
search_and_fetch(new_query)
