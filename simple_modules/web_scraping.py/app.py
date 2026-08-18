import web_scraper # including my module

emails = web_scraper.fetch_emails("https://example.com")
print(emails)

## HOWEVER: SOMETIME NEED TO INCLUDE THE LIBS ON BOTH 
# import requests
# import web_scraper

# # Using requests directly in main.py
# my_response = requests.get("https://other-site.com")

# # Using web_scraper module
# emails = web_scraper.fetch_emails("https://example.com")