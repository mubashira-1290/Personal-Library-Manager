 

---

### 📚 Personal Library Manager (Beginner Version)

A simple console-based app to manage your personal book collection. You can add, view, search, and delete books.

---

### ✅ Features

- Add a new book (title, author, year, genre)
- View all books
- Search for a book by title
- Delete a book by title
- Save all books in a JSON file

---

### 🛠 Requirements

- Python 3.7+
- No extra libraries required (only built-in modules)

---

### 📁 Project Structure

```
personal_library_manager/
│
├── library_manager.py
├── books.json
└── README.md
```

---

### 🧠 Code: `library_manager.py`

```python
import json
import os

BOOKS_FILE = "books.json"

def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_books(books):
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)

def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = input("Enter year: ")
    genre = input("Enter genre: ")

    books.append({
        "title": title,
        "author": author,
        "year": year,
        "genre": genre
    })
    print(f"✅ Book '{title}' added.")

def view_books(books):
    if not books:
        print("No books in your library.")
    else:
        for i, book in enumerate(books, start=1):
            print(f"\n📖 Book {i}")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Year: {book['year']}")
            print(f"Genre: {book['genre']}")

def search_book(books):
    keyword = input("Enter title to search: ").lower()
    found = False
    for book in books:
        if keyword in book["title"].lower():
            print(f"\n✅ Found: {book['title']} by {book['author']}")
            found = True
    if not found:
        print("❌ No book found with that title.")

def delete_book(books):
    title = input("Enter title of the book to delete: ").lower()
    for book in books:
        if book["title"].lower() == title:
            books.remove(book)
            print(f"🗑️ Book '{book['title']}' deleted.")
            return
    print("❌ Book not found.")

def menu():
    books = load_books()
    while True:
        print("\n📚 Personal Library Manager")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_book(books)
            save_books(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            delete_book(books)
            save_books(books)
        elif choice == "5":
            save_books(books)
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please choose from 1-5.")

if __name__ == "__main__":
    menu()
```

---

### 📘 Create a file: `books.json`

Just add an empty list to start:

```json
[]
```

---

### 📝 README.md (optional)

```markdown
# 📚 Personal Library Manager

A beginner-friendly Python app to manage your personal book collection.

## Features

- Add books
- View all books
- Search books
- Delete books
- Save to `books.json`

## How to Run

1. Make sure you have Python installed.
2. Open the folder in VS Code.
3. Run the app:
   ```bash
   python library_manager.py
   ```

Have fun managing your library!
```

---

