import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_indeed_jobs(query="AI", location="India", pages=1):
    jobs = []

    for page in range(pages):
        start = page * 10
        url = f"https://in.indeed.com/jobs?q={query}&l={location}&start={start}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"URL: {url}")
        soup = BeautifulSoup(response.text, "html.parser")

        cards = soup.find_all("div", class_="job_seen_beacon")

        for card in cards:
            title = card.find("h2").text.strip() if card.find("h2") else "N/A"
            company = card.find("span", class_="companyName").text.strip() if card.find("span", class_="companyName") else "N/A"
            location = card.find("div", class_="companyLocation").text.strip() if card.find("div", class_="companyLocation") else "N/A"
            summary = card.find("div", class_="job-snippet").text.strip().replace('\n', '') if card.find("div", class_="job-snippet") else "N/A"
            jobs.append([title, company, location, summary])

        time.sleep(1)

    df = pd.DataFrame(jobs, columns=["Title", "Company", "Location", "Summary"])
    df.to_csv("ai_jobs.csv", index=False)
    print(f"✅ Saved {len(df)} jobs to ai_jobs.csv")

if __name__ == "__main__":
    scrape_indeed_jobs(query="AI", location="India", pages=2)