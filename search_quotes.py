# search_quotes.py
from models import Author, Quote
from mongoengine import connect

# Підключення до бази даних
connect(
    db="your_database_name",
    username="your_username",
    password="your_password",
    host="your_cluster_host",
    port=your_port
)

def search_by_name(name):
    author = Author.objects(fullname=name).first()
    if author:
        quotes = Quote.objects(author=author)
        return [quote.quote for quote in quotes]
    return []

def search_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    return [quote.quote for quote in quotes]

def search_by_tags(tags):
    tags_list = tags.split(',')
    quotes = Quote.objects(tags__in=tags_list)
    return [quote.quote for quote in quotes]

if __name__ == "__main__":
    while True:
        command = input("Enter command (or 'exit' to quit): ")
        if command == "exit":
            break
        try:
            cmd, value = command.split(":")
            if cmd == "name":
                result = search_by_name(value.strip())
            elif cmd == "tag":
                result = search_by_tag(value.strip())
            elif cmd == "tags":
                result = search_by_tags(value.strip())
            else:
                print("Unknown command")
                continue

            for quote in result:
                print(quote.encode('utf-8').decode('utf-8'))
        except ValueError:
            print("Invalid command format")
