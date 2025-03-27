import re      #For regular expresion patterns
import sys     #For handling command line argument
from urllib.parse import urlparse  #For validating proper url format
from colorama import Fore, Style, init # For coloured output
init(autoreset=True)

# List of common phishing keywords (for demonstration purposes)
phishing_keywords = ["login", "verify", "account", "update", "secure", "bank", "password", "signin", "confirm","0"]

#Function to check if the URL is valid
def is_valid_url(url):
    url = url.strip()  #Remove any space around url
    parsed = urlparse(url)
    return bool(parsed.scheme) and bool(parsed.netloc)

# Function to check if a URL contains phishing keywords
def contains_phishing_keywords(url):
    for keyword in phishing_keywords:
        if keyword in url.lower():
            return True
    return False

# Function to check if a URL contains suspicious patterns (e.g., IP addresses)
def contains_suspicious_patterns(url):
    # Check for presence of IP address in URL
    ip_pattern = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
    if ip_pattern.search(url):
        return True

    # Check for multiple subdomains (e.g., http://secure-login.example.com)
    subdomain_pattern = re.compile(r'(\w+\.){3,}')
    if subdomain_pattern.search(url):
        return True

    return False

# Main function to scan a list of URLs for phishing
def scan_for_phishing(urls):
    for url in urls:
        if not is_valid_url(url):
            url = url.strip()  #Remove any space around url
            print(f" ❌ Invalid URL Format: {url}")
            continue
    
        if contains_phishing_keywords(url):
            print(f" ⚠️ Potential phishing URL detected: {url}")
        elif contains_suspicious_patterns(url):
            print(f" ⚠️ Suspicious URL detected: {url}")
        else:
            print(f"✅ URL seems safe: {url}")



# Example usage
def main():
    if len(sys.argv) > 1:
        urls = sys.argv[1:]  #Take url from command-line argument
    else:
        urls = input("Enter the url to scan: ").split(',') #Accepting multiple urls separated by commas or space

    #Cleaning and Scanning each url
    urls = [url.strip() for url in urls if url.strip()]
    scan_for_phishing(urls)

#Runnig main function
main()