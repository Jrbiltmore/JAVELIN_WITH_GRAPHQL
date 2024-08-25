from dashboard import app
from flask import render_template, request, jsonify
from crawler.web_crawler import WebCrawler
from sql_injection.sql_tester import detect_sql_injection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crawl', methods=['POST'])
def crawl():
    data = request.json
    base_url = data.get('base_url')
    max_depth = data.get('max_depth', 3)
    max_pages = data.get('max_pages', 100)
    
    crawler = WebCrawler(base_url, max_depth=max_depth, max_pages=max_pages)
    crawler.start_crawl()
    
    return jsonify({'targets': crawler.targets})

@app.route('/test_sql_injection', methods=['POST'])
def test_sql_injection():
    data = request.json
    url = data.get('url')
    
    is_vulnerable = detect_sql_injection(url)
    message = "SQL Injection vulnerability detected!" if is_vulnerable else "No vulnerabilities found."
    
    return jsonify({'success': is_vulnerable, 'message': message})
