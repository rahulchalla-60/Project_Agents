import requests
from bs4 import BeautifulSoup
from typing import List
from config import GEMINI_CONFIG

def search_internshala_jobs(keywords, max_results=5):
    """
    Searches Internshala for internships/jobs matching the given keywords.
    Returns a list of dicts: {title, company, location, description}
    """
    base_url = "https://internshala.com"
    search_url = f"{base_url}/internships/keywords-{'-'.join(keywords)}"
    
    try:
        response = requests.get(search_url, timeout=10)
        if response.status_code != 200:
            print(f"Failed to fetch job postings: {response.status_code}")
            return []
        
        soup = BeautifulSoup(response.text, "html.parser")
        cards = soup.find_all("div", class_="individual_internship")
        
        results = []
        seen_jobs = set()  # Track unique job combinations
        
        for card in cards:
            # Try multiple selectors for title
            title = "N/A"
            title_selectors = [
                "div.heading_4_5.profile",
                "h3.heading_4_5.profile",
                "div.profile",
                "h3.profile"
            ]
            for selector in title_selectors:
                title_tag = card.select_one(selector)
                if title_tag:
                    title = title_tag.get_text(strip=True)
                    break
            
            # Try multiple selectors for company
            company = "N/A"
            company_selectors = [
                "a.link_display_like_text",
                "div.company_name",
                "span.company_name",
                "a.company_name"
            ]
            for selector in company_selectors:
                company_tag = card.select_one(selector)
                if company_tag:
                    company = company_tag.get_text(strip=True)
                    break
            
            # Try multiple selectors for location
            location = "N/A"
            location_selectors = [
                "a.location_link.view_detail_button",
                "span.location_link",
                "div.location",
                "span.location"
            ]
            for selector in location_selectors:
                location_tag = card.select_one(selector)
                if location_tag:
                    location = location_tag.get_text(strip=True)
                    break
            
            # Try multiple selectors for description
            description = "N/A"
            desc_selectors = [
                "div.internship_other_details_container",
                "div.description",
                "div.job_description",
                "span.description"
            ]
            for selector in desc_selectors:
                desc_tag = card.select_one(selector)
                if desc_tag:
                    description = desc_tag.get_text(separator=" ", strip=True)
                    break
            
            # If we still have N/A values, try to get any text from the card
            if title == "N/A":
                # Try to find any heading or prominent text
                heading = card.find("h3") or card.find("h4") or card.find("h5")
                if heading:
                    title = heading.get_text(strip=True)
            
            if company == "N/A":
                # Try to find company info in any link or text
                company_link = card.find("a", href=lambda x: x and "company" in x.lower())
                if company_link:
                    company = company_link.get_text(strip=True)
            
            if description == "N/A":
                # Get all text from the card as fallback
                all_text = card.get_text(separator=" ", strip=True)
                # Take first 200 characters as description
                description = all_text[:200] + "..." if len(all_text) > 200 else all_text
            
            # Create unique identifier for deduplication
            job_key = f"{title}_{company}_{location}"
            
            # Only add if we haven't seen this job before
            if job_key not in seen_jobs:
                seen_jobs.add(job_key)
                results.append({
                    "title": title,
                    "company": company,
                    "location": location,
                    "description": description
                })
                
                # Stop if we have enough unique jobs
                if len(results) >= max_results:
                    break
        
        return results
        
    except Exception as e:
        print(f"Error scraping Internshala: {e}")
        return []

def get_mock_jobs():
    """Fallback mock jobs if scraping fails"""
    return [
        {
            "title": "Software Engineer Intern",
            "company": "Tech Corp",
            "location": "Remote",
            "description": "Work on backend systems using Python and cloud technologies."
        },
        {
            "title": "Data Analyst Intern",
            "company": "Data Solutions",
            "location": "Mumbai",
            "description": "Analyze datasets and generate insights using Python and SQL."
        },
        {
            "title": "Web Developer Intern",
            "company": "WebTech",
            "location": "Bangalore",
            "description": "Develop and maintain web applications using React and Django."
        },
        {
            "title": "AI Research Intern",
            "company": "AI Labs",
            "location": "Delhi",
            "description": "Assist in research projects involving machine learning and NLP."
        },
        {
            "title": "Product Management Intern",
            "company": "Product Inc",
            "location": "Hyderabad",
            "description": "Support product managers in market research and feature planning."
        }
    ]

def search_jobs(skills: List[str], max_results: int = 5) -> List[dict]:
    """
    Searches for jobs based on a list of skills/keywords.
    First tries Internshala scraping, falls back to mock data if it fails.
    """
    # Try to get real jobs from Internshala
    real_jobs = search_internshala_jobs(skills, max_results)
    
    if real_jobs:
        print(f"Found {len(real_jobs)} unique jobs from Internshala")
        return real_jobs
    else:
        print("Using mock jobs (scraping failed)")
        # Filter mock jobs by skills (basic matching)
        mock_jobs = get_mock_jobs()
        filtered_jobs = [
            job for job in mock_jobs 
            if any(skill.lower() in job["description"].lower() for skill in skills)
        ]
        return filtered_jobs[:max_results] if filtered_jobs else mock_jobs[:max_results]

if __name__ == "__main__":
    # Example usage
    example_skills = ["python", "developer"]
    jobs = search_jobs(example_skills, max_results=5)
    print("\n--- Job Search Results ---\n")
    for i, job in enumerate(jobs, 1):
        print(f"{i}. {job['title']} at {job['company']} ({job['location']}):")
        print(f"   {job['description']}\n")

