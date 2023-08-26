import feedparser
import json
from datetime import datetime, timedelta
import time

# List of RSS feed URLs to scrape
rss_feeds = ['http://example.com/rss/feed1.xml', 'http://example.com/rss/feed2.xml']

# List of keywords to filter for
keywords = ['keyword1', 'keyword2', 'keyword3']

# Function to scrape and save matching entries
def scrape_and_save(feed_url):
    feed = feedparser.parse(feed_url)
    
    matching_entries = []
    
    for entry in feed.entries:
        if any(keyword in entry.title.lower() or keyword in entry.summary.lower() for keyword in keywords):
            matching_entries.append({
                'title': entry.title,
                'summary': entry.summary,
                'link': entry.link
            })

    # Write matching entries to TXT file
    with open(f'matching_entries_{feed.feed.title}.txt', 'w') as txt_file:
        for entry in matching_entries:
            txt_file.write(f"Title: {entry['title']}\nSummary: {entry['summary']}\nLink: {entry['link']}\n\n")

    # Write matching entries to JSON file
    with open(f'matching_entries_{feed.feed.title}.json', 'w') as json_file:
        json.dump(matching_entries, json_file, indent=4)

# Function to run daily scraping process
def run_daily_scraping():
    start_time = datetime.now().replace(hour=0, minute=0, second=0) + timedelta(days=1)
    delay = (start_time - datetime.now()).total_seconds()
    time.sleep(delay)

    for feed_url in rss_feeds:
        scrape_and_save(feed_url)

    exit()

# Run the daily scraping program
run_daily_scraping()
