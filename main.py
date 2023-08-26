import feedparser
import xml.etree.ElementTree as ET

# RSS feed URL to query
rss_feed_url = 'https://www.bankless.com/rss/feed'

# Parse the RSS feed
feed = feedparser.parse(rss_feed_url)

# Create XML structure
rss = ET.Element('rss')
channel = ET.SubElement(rss, 'channel')

for entry in feed.entries:
    item = ET.SubElement(channel, 'item')
    
    title = ET.SubElement(item, 'title')
    title.text = entry.title
    
    link = ET.SubElement(item, 'link')
    link.text = entry.link
    
    author = ET.SubElement(item, 'author')
    author.text = entry.author if hasattr(entry, 'author') else ''
    
    date = ET.SubElement(item, 'pubDate')
    date.text = entry.published if hasattr(entry, 'published') else ''
    
    content = ET.SubElement(item, 'content')
    content.text = entry.summary if hasattr(entry, 'summary') else ''

# Create an ElementTree object and write to XML file
tree = ET.ElementTree(rss)
tree.write('rss_data.xml', encoding='utf-8', xml_declaration=True)

print("XML data saved to 'rss_data.xml'")
