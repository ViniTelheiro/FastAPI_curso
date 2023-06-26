
BOOKS = [
    {"title": "Title One", "author": "Author One", "category":"science"},
    {"title": "Title Two", "author": "Author Two", "category":"science"},
    {"title": "Title Three", "author": "Author Three", "category":"history"},
    {"title": "Title Four", "author": "Author Four", "category":"math"},
    {"title": "Title Five", "author": "Author Five", "category":"math"},
    {"title": "Title Six", "author": "Author Six", "category":"math"}
]


if __name__ == '__main__':
    category = 'math'
    books_to_return = list(filter(lambda x:x.get('category').casefold() == category.casefold(), BOOKS))
    print(books_to_return)