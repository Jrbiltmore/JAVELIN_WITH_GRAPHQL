import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import logging
import re
import subprocess

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WebCrawler:
    def __init__(self, base_url, max_depth=3, max_pages=100):
        self.base_url = base_url
        self.max_depth = max_depth
        self.max_pages = max_pages
        self.visited = set()
        self.to_visit = [(base_url, 0)]
        self.targets = []

    def start_crawl(self):
        while self.to_visit and len(self.visited) < self.max_pages:
            url, depth = self.to_visit.pop(0)
            if depth > self.max_depth:
                continue
            self.crawl_page(url, depth)
        logging.info(f"Crawling finished. Found {len(self.targets)} targets.")

    def crawl_page(self, url, depth):
        if url in self.visited:
            return
        try:
            response = requests.get(url)
            if response.status_code != 200:
                return
            self.visited.add(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            self.extract_links(soup, url, depth)
            self.extract_forms(soup, url)
        except requests.RequestException as e:
            logging.error(f"Error crawling {url}: {e}")

    def extract_links(self, soup, current_url, depth):
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            full_url = urljoin(current_url, href)
            if self.is_valid_url(full_url):
                self.to_visit.append((full_url, depth + 1))

    def extract_forms(self, soup, current_url):
        for form in soup.find_all('form'):
            action = form.get('action')
            method = form.get('method', 'get').lower()
            form_url = urljoin(current_url, action)
            inputs = [input_tag.get('name') for input_tag in form.find_all('input') if input_tag.get('name')]
            self.targets.append({'url': form_url, 'method': method, 'inputs': inputs})
            logging.info(f"Found form: {form_url} with inputs {inputs}")

    def is_valid_url(self, url):
        parsed_url = urlparse(url)
        return parsed_url.scheme in ['http', 'https'] and parsed_url.netloc and url not in self.visited

    def save_results(self, filename='targets.txt'):
        with open(filename, 'w') as file:
            for target in self.targets:
                file.write(f"URL: {target['url']}, Method: {target['method']}, Inputs: {target['inputs']}
")
        logging.info(f"Targets saved to {filename}")

def compile_to_bytecode(script_path):
    logging.info("Compiling script to bytecode...")
    subprocess.run(['python', '-m', 'compileall', '-b', script_path])
    logging.info("Bytecode compilation completed.")

def obfuscate_code(script_path):
    logging.info("Obfuscating script using PyArmor...")
    subprocess.run(['pyarmor', 'obfuscate', script_path])
    logging.info("Code obfuscation completed.")

def package_executable(script_path):
    logging.info("Packaging script into executable using PyInstaller...")
    subprocess.run(['pyinstaller', '--onefile', '--noconsole', script_path])
    logging.info("Executable packaging completed.")

if __name__ == "__main__":
    # Step 1: Crawl for SQL Injection Points
    base_url = input("Enter the base URL to start crawling: ")
    crawler = WebCrawler(base_url)
    crawler.start_crawl()
    crawler.save_results()

    # Step 2: Compile to Bytecode
    script_path = 'sql_injection_scanner.py'  # Replace with your script path
    compile_to_bytecode(script_path)

    # Step 3: Obfuscate Code
    obfuscate_code(script_path)

    # Step 4: Package as Executable
    package_executable(script_path)

    logging.info("All tasks completed successfully.")
