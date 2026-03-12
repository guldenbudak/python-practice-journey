borrows = {}
user = {}
borrow_book = []
add_user = int(input("How many users will be added? :"))

for add in range(add_user):
    name = input("Enter your name: ")
    books = input("Enter your book: ")
    user = {
        "books": [books]
    }
    if name not in borrows:
        if books not in borrow_book:
            borrow_book = books
            borrows[name] = user
    else:
        borrows[name]["books"].append(books)
print(borrows)