from mongoengine import connect, disconnect
from models import Author, Quote

# Відключення від бази даних, якщо вже є активне з'єднання
disconnect()

# Підключення до бази даних
connect('web_hw8', host='mongodb+srv://OlgaSHell:PgkhuKA3k2dqHPE@cluster0.ayzqqtl.mongodb.net')


def search_quotes():
    while True:
        user_input = input("Введіть команду (наприклад, name: Steve Martin, tag:life, tags:life,live, або exit): ")

        if user_input.startswith('name:'):
            author_name = user_input[5:].strip()
            author = Author.objects(fullname__icontains=author_name).first()
            if author:
                quotes = Quote.objects(author=author)
                for quote in quotes:
                    print(quote.quote)
            else:
                print("Немає цитат для цього автора.")

        elif user_input.startswith('tag:'):
            tag = user_input[4:].strip()
            quotes = Quote.objects(tags__icontains=tag)
            for quote in quotes:
                print(quote.quote)

        elif user_input.startswith('tags:'):
            tags = user_input[5:].strip().split(',')
            quotes = Quote.objects(tags__in=tags)
            for quote in quotes:
                print(quote.quote)

        elif user_input == 'exit':
            print("Завершення пошуку.")
            break

        else:
            print("Невідома команда. Будь ласка, використовуйте name:, tag: або tags: для пошуку цитат, або введіть exit для виходу.")

if __name__ == "__main__":
    search_quotes()
