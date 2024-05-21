import json
from models import Author, Quote  # Ensure 'models' is a valid module with Author and Quote classes
from mongoengine import connect

# Replace the following placeholders with actual values
DATABASE_NAME = "your_database_name"
USERNAME = "your_username"
PASSWORD = "your_password"
CLUSTER_HOST = "your_cluster_host"
PORT = 27017  # Replace with your actual MongoDB port if different

# Підключення до бази даних
connect(
    db=DATABASE_NAME,
    username=USERNAME,
    password=PASSWORD,
    host=CLUSTER_HOST,
    port=PORT
)

def load_authors(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        authors_data = json.load(file)
        for author_data in authors_data:
            author = Author(**author_data)
            author.save()

def load_quotes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        quotes_data = json.load(file)
        for quote_data in quotes_data:
            author_name = quote_data.pop('author')
            author = Author.objects(fullname=author_name).first()
            if author:
                quote = Quote(author=author, **quote_data)
                quote.save()

if __name__ == "__main__":
    load_authors('authors.json')
    load_quotes('quotes.json')
