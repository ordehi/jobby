import requests
from bs4 import BeautifulSoup
import json


def extract_data(soup, schema):
    results = []
    # Check if the current schema level describes a container for multiple items
    if schema.get("extract") == "multiple":
        containers = soup.select(schema["container"])
        for container in containers:
            item_data = {}
            for key, detail in schema["details"].items():
                if detail.get("extract") == "multiple":
                    # Recursive call for nested multiple items
                    item_data[key] = extract_data(container, detail)
                else:
                    # Handling single item extraction
                    if detail.get("extract") == "text":
                        element = container.select_one(detail["selector"])
                        item_data[key] = element.text.strip(
                        ) if element else 'N/A'
                    elif detail.get("extract") == "attribute":
                        element = container.select_one(detail["selector"])
                        item_data[key] = element[detail["attribute_name"]
                                                 ].strip() if element else 'N/A'
            results.append(item_data)
    else:
        # Handling for non-multiple extraction at the top level, if applicable
        pass
    return results if results else None


def scrape(url, schema):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        data = extract_data(soup, schema)
        return data
    else:
        print(f"Error fetching {url}: Status code {response.status_code}")
        return []


def scrape_sites_from_file(file_path):
    with open(file_path, 'r') as f:
        sites = json.load(f)

    all_data = []
    for site in sites:
        url = site['url']
        schema = site['schema']
        data = scrape(url, schema)
        all_data.append({'url': url, 'data': data})

    return all_data


if __name__ == "__main__":
    all_data = scrape_sites_from_file('data/sites.json')
    print(all_data)
