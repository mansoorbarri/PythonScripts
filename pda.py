import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

PROCESSED_FILE = "/home/anar/Music/anar/gh/PythonScripts/pda.json"  # Changed to relative path

def load_processed_listings():
    try:
        with open(PROCESSED_FILE, "r") as file:
            return set(json.load(file))
    except FileNotFoundError:
        return set()

def save_processed_listings(processed_listings):
    with open(PROCESSED_FILE, "w") as file:
        json.dump(list(processed_listings), file)

def fetch_apprenticeships(url, processed_listings):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return parse_apprenticeships(response.text, processed_listings)
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return []

def parse_apprenticeships(html_content, processed_listings):
    soup = BeautifulSoup(html_content, 'html.parser')
    new_posts = []
    today = datetime.now()
    today_str = f"Posted {today.day} {today.strftime('%B')}"

    listings = soup.find_all('li', class_='das-search-results__list-item')

    for listing in listings:
        date_elem = listing.find('p', class_='govuk-body govuk-!-font-size-16 das-!-color-dark-grey')
        if date_elem and today_str in date_elem.text:  # Check if posted today
            title = listing.find('h2', class_='govuk-heading-m').find('a').text.strip()
            company = listing.find('p', class_='govuk-body govuk-!-margin-bottom-0').text.strip()
            location = listing.find('p', class_='govuk-body das-!-color-dark-grey').text.strip()

            wage_elem = listing.find('b', string='Wage')
            wage = wage_elem.parent.get_text(strip=True).replace('Wage', '').strip() if wage_elem else "Not specified"

            closing_elem = listing.find('p', class_='govuk-body govuk-!-margin-bottom-0 govuk-!-margin-top-1')
            closing_date = closing_elem.text.strip() if closing_elem else "Not specified"

            job_url = listing.find('a', class_='das-search-results__link')['href']
            job_id = job_url.split("/")[-1]

            if job_id not in processed_listings:
                new_posts.append({
                    'id': job_id,
                    'title': title,
                    'location': location,
                    'company': company,
                    'wage': wage,
                    'closing_date': closing_date,
                    'job_url': f"https://www.findapprenticeship.service.gov.uk{job_url}",
                })

    return new_posts


def format_for_terminal(apprenticeships): # Simplified for terminal output
    if not apprenticeships:
        return "No new apprenticeships found."

    output = ""
    for app in apprenticeships:
        output += f"Title: {app['title']}\n"
        output += f"Location: {app['location']}\n"
        output += f"Company: {app['company']}\n"
        output += f"Wage: {app['wage']}\n"
        output += f"Closes: {app['closing_date']}\n"
        output += f"Link: {app['job_url']}\n\n"
    return output.strip()


if __name__ == "__main__":
    url = "https://www.findapprenticeship.service.gov.uk/apprenticeships?sort=AgeAsc&searchTerm=&location=M29+7AR&distance=20&levelIds=5&levelIds=6&routeIds=7#"  # Your specific URL
    processed_listings = load_processed_listings()
    new_apprenticeships = fetch_apprenticeships(url, processed_listings)

    if new_apprenticeships:
        new_ids = {app['id'] for app in new_apprenticeships}
        processed_listings.update(new_ids)
        save_processed_listings(processed_listings)

    terminal_output = format_for_terminal(new_apprenticeships)
    print(terminal_output)
