import re, requests # because it's this file that uses these libs

def fetch_emails(url):
    response = requests.get(url)
    emails = re.findall(r'[\w.-]+@[\w.-]+', response.text)

    return emails