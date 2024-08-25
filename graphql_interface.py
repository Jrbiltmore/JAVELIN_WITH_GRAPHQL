import graphene
from graphene import ObjectType, String, Int, List, Field, Schema
from crawler.web_crawler import WebCrawler
from sql_injection.sql_tester import detect_sql_injection
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define a GraphQL type for a Target
class TargetType(ObjectType):
    url = String()
    method = String()
    inputs = List(String)

# Define the Query class
class Query(ObjectType):
    crawl = List(TargetType, base_url=String(required=True), max_depth=Int(), max_pages=Int())

    def resolve_crawl(self, info, base_url, max_depth=3, max_pages=100):
        crawler = WebCrawler(base_url, max_depth=max_depth, max_pages=max_pages)
        crawler.start_crawl()
        return [TargetType(url=target['url'], method=target['method'], inputs=target['inputs']) for target in crawler.targets]

# Define the Mutation class
class DetectSQLInjection(graphene.Mutation):
    class Arguments:
        url = String(required=True)
    
    message = String()
    success = graphene.Boolean()

    def mutate(self, info, url):
        is_vulnerable = detect_sql_injection(url)
        message = f"SQL Injection vulnerability detected on {url}!" if is_vulnerable else f"No vulnerabilities found on {url}."
        return DetectSQLInjection(success=is_vulnerable, message=message)

class Mutation(ObjectType):
    detect_sql_injection = DetectSQLInjection.Field()

# Create the schema
schema = Schema(query=Query, mutation=Mutation)

if __name__ == "__main__":
    from flask import Flask
    from flask_graphql import GraphQLView

    app = Flask(__name__)
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)  # graphiql=True enables the GraphiQL interface
    )

    app.run(host='0.0.0.0', port=5000)
