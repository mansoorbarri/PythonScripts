import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

def fetch_apprenticeships(url):
    """
    Fetch and parse apprenticeship listings from the given URL
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5'
        }
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        return parse_apprenticeships(response.text)
        
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return []

def parse_apprenticeships(html_content):
    """
    Parse apprenticeship listings and return those posted today
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    today_posts = []
    
    listings = soup.find_all('li', class_='das-search-results__list-item')
    
    for listing in listings:
        date_elem = listing.find('p', class_='govuk-body govuk-!-font-size-16 das-!-color-dark-grey')
        if date_elem and "Posted 9 January" in date_elem.text:
            title = listing.find('h2', class_='govuk-heading-m').find('a').text.strip()
            company = listing.find('p', class_='govuk-body govuk-!-margin-bottom-0').text.strip()
            location = listing.find('p', class_='govuk-body das-!-color-dark-grey').text.strip()
            
            wage_elem = listing.find('b', string='Wage')
            if wage_elem:
                wage = wage_elem.parent.get_text(strip=True).replace('Wage', '').strip()
            else:
                wage = "Not specified"
            
            closing_elem = listing.find('p', class_='govuk-body govuk-!-margin-bottom-0 govuk-!-margin-top-1')
            closing_date = closing_elem.text.strip() if closing_elem else "Not specified"
            
            job_url = listing.find('a', class_='das-search-results__link')['href']
            
            today_posts.append({
                'title': title,
                'location': location,
                'company': company,
                'wage': wage,
                'closing_date': closing_date,
                'job_url': f"https://www.findapprenticeship.service.gov.uk{job_url}",
            })
    
    return today_posts

def format_for_discord(apprenticeships):
    """
    Format apprenticeship listings for Discord using markdown
    """
    if not apprenticeships:
        return "No apprenticeships found posted today."
    
    output = ""
    for app in apprenticeships:
        # Format title with location
        title_with_location = f"{app['title']} in {app['location']}"
        output += f"## {title_with_location}\n"
        
        # Format details
        output += f"**Wage:** {app['wage']}\n"
        output += f"**Company:** {app['company']}\n"
        output += f"**Closes:** {app['closing_date'].replace('Closes on ', '').replace('Closes in ', '')}\n"
        output += f"**Link:** {app['job_url']}\n\n"
    
    return output.strip()

# Main execution
if __name__ == "__main__":
    url = "https://www.findapprenticeship.service.gov.uk/apprenticeships?routeIds=7&sort=AgeAsc&levelIds=6"
    apprenticeships = fetch_apprenticeships(url)
    discord_formatted = format_for_discord(apprenticeships)
    print(discord_formatted)