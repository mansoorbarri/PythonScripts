import requests
from bs4 import BeautifulSoup
import json

def scrape_findajob(url):
    """
    Scrapes job listings from findajob.dwp.gov.uk
    
    Args:
        url: The URL to scrape
        
    Returns:
        list: A list of dictionaries containing job information
    """
    
    # Set headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Fetch the webpage
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all job listings
        job_listings = soup.find_all('div', class_='search-result')
        
        jobs = []
        
        for job in job_listings:
            job_data = {}
            
            # Extract title
            title_elem = job.find('h3', class_='govuk-heading-s')
            if title_elem:
                link = title_elem.find('a')
                job_data['title'] = link.text.strip() if link else ''
                job_data['url'] = 'https://findajob.dwp.gov.uk' + link['href'] if link else ''
            
            # Extract details from the list
            details = job.find('ul', class_='search-result-details')
            if details:
                list_items = details.find_all('li')
                
                for item in list_items:
                    text = item.text.strip()
                    
                    # Extract employer and location
                    if item.find('strong') and ' - ' in text:
                        parts = text.split(' - ')
                        job_data['employer'] = parts[0].replace('**', '').strip()
                        job_data['location'] = parts[1].strip() if len(parts) > 1 else ''
                    
                    # Extract salary
                    elif '£' in text or 'per annum' in text.lower() or 'per year' in text.lower():
                        job_data['salary'] = text.replace('**', '').strip()
                
                # Extract contract type and hours from tags
                tags = item.find_all('li', class_='govuk-tag')
                contract_info = []
                
                for tag in tags:
                    tag_text = tag.text.strip()
                    contract_info.append(tag_text)
                    
                    # Determine if permanent or contract
                    if tag_text.lower() == 'permanent':
                        job_data['employment_status'] = 'Permanent'
                    elif tag_text.lower() == 'contract':
                        job_data['employment_status'] = 'Contract'
                    
                    # Check if part time or full time
                    if tag_text.lower() == 'part time':
                        job_data['hours'] = 'Part time'
                    elif tag_text.lower() == 'full time':
                        job_data['hours'] = 'Full time'
                    
                    # Check for remote working
                    if 'remote' in tag_text.lower():
                        job_data['remote_working'] = tag_text
                
                job_data['contract_tags'] = contract_info
            
            # Extract description
            description_elem = job.find('p', class_='search-result-description')
            if description_elem:
                job_data['description'] = description_elem.text.strip()
            
            # Set defaults if not found
            job_data.setdefault('salary', 'Not specified')
            job_data.setdefault('location', 'Not specified')
            job_data.setdefault('employment_status', 'Not specified')
            job_data.setdefault('hours', 'Not specified')
            
            jobs.append(job_data)
        
        return jobs
    
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []
    except Exception as e:
        print(f"Error parsing the page: {e}")
        return []


def load_existing_jobs():
    """Load existing jobs from JSON file"""
    try:
        with open('jobs.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def main():
    url = "https://findajob.dwp.gov.uk/search?cat=14&cti=part_time&f=1&loc=86397&pp=50"
    
    existing_jobs = load_existing_jobs()
    existing_urls = {job.get('url') for job in existing_jobs if job.get('url')}
    
    all_jobs = scrape_findajob(url)
    new_jobs = [job for job in all_jobs if job.get('url') not in existing_urls]
    
    if not new_jobs:
        print("No jobs found")
        return
    
    for i, job in enumerate(new_jobs, 1):
        print(f"\n{'='*70}")
        print(f"JOB {i}")
        print(f"{'='*70}")
        print(f"Title:      {job.get('title', 'N/A')}")
        print(f"Employer:   {job.get('employer', 'N/A')}")
        print(f"Location:   {job.get('location', 'N/A')}")
        print(f"Salary:     {job.get('salary', 'N/A')}")
        print(f"Status:     {job.get('employment_status', 'N/A')}")
        print(f"Hours:      {job.get('hours', 'N/A')}")
        if 'remote_working' in job:
            print(f"Remote:     {job['remote_working']}")
        print(f"URL:        {job.get('url', 'N/A')}")
    
    # print(f"\n{'='*70}")
    # print(f"Total: {len(new_jobs)} new job(s)")
    # print(f"{'='*70}\n")
    
    updated_jobs = existing_jobs + new_jobs
    with open('jobs.json', 'w', encoding='utf-8') as f:
        json.dump(updated_jobs, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()