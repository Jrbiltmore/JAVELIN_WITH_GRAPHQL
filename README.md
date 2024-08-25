# SQL Injection Tool

A command-line tool for detecting and exploiting SQL injection vulnerabilities. This tool provides functionalities for web crawling, SQL injection testing, code obfuscation, and packaging scripts into standalone executables. It also includes a GraphQL API and a Flask-based web dashboard.

## Features

- **Web Crawler**: Crawls web pages to identify potential SQL injection points by collecting URLs and forms.
- **SQL Injection Tester**: Detects and exploits SQL injection vulnerabilities using a set of predefined payloads.
- **Code Obfuscation**: Uses PyArmor to obfuscate Python scripts, protecting them from reverse engineering.
- **Executable Packaging**: Packages scripts into standalone executables using PyInstaller.
- **GraphQL API**: Provides a flexible API for querying and mutating the state of the SQL injection tool.
- **Flask Dashboard**: Offers a user-friendly web interface to interact with the tool.

## Installation

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage

1. **Web Crawling**: Start the web crawler to identify SQL injection points.
   ```bash
   python crawler/web_crawler.py
   ```

2. **SQL Injection Testing**: Use the SQL tester to check for SQL injection vulnerabilities.
   ```bash
   python sql_injection/sql_tester.py
   ```

3. **Code Obfuscation and Packaging**: Obfuscate the code and package it into an executable.
   ```bash
   python utils/obfuscate_and_package.py
   ```

4. **Unified Script**: Run the unified script to perform all actions sequentially.
   ```bash
   python unified_script.py
   ```

5. **Running the GraphQL API**:
   ```bash
   python graphql_interface.py
   ```

   Access the GraphQL API at `http://localhost:5000/graphql`.

6. **Running the Dashboard**:
   ```bash
   export FLASK_APP=dashboard
   flask run
   ```

   Access the dashboard at `http://localhost:5000`.

## Docker Deployment

To deploy the SQL Injection Tool using Docker:

1. **Build the Docker Image**:
   ```bash
   docker-compose build
   ```

2. **Run the Docker Containers**:
   ```bash
   docker-compose up
   ```

3. **Access the Application**:
   - Visit `http://localhost:5000` for the Flask Dashboard.
   - Visit `http://localhost:5000/graphql` for the GraphQL API.

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
