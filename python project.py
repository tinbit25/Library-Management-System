import os
import turtle

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Book:
    def __init__(self, name, author_name, book_id, shelf, status):
        self.name = name
        self.author_name = author_name
        self.book_id = book_id
        self.shelf = shelf
        self.status = status

class Library:
    def __init__(self):
        self.book_list = []
        self.users = []
        self.current_user = None

    def register(self):
        os.system("cls")
        username = input("Enter a new username: ")
        password = input("Enter a new password: ")
        new_user = User(username, password)
        self.users.append((new_user.username, new_user.password))
        print("Registration successful!")

    def login(self):
        os.system("cls")
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            for user in self.users:
                if user[0] == username and user[1] == password:
                    self.current_user = user
                    print("Login successful!")
                    return
            print("Invalid username or password. Please try again.")

    def add_book(self):
        if not self.current_user:
            print("Please login first.")
            return
        while True:
            name = input("Enter the name of the book: ")
            author_name = input("Enter the author of the book: ")
            book_id = input("Enter the book id: ")
            shelf = int(input("Enter the shelf of the book: "))
            status = input("Enter the status of the book: ")
            book = Book(name, author_name, book_id, shelf, status)
            self.book_list.append(book)
            os.system("cls")
            ch = input("If you want to add more books, press 1. To exit, press 0: ")
            if ch == '0':
                break

    def display(self):
        if not self.current_user:
            print("Please login first.")
            return
        os.system("cls")
        for book in self.book_list:
            print(f"Name: {book.name}, Author: {book.author_name}, ID: {book.book_id}, Shelf: {book.shelf}, Status: {book.status}")

    def search(self):
        if not self.current_user:
            print("Please login first.")
            return
        os.system("cls")
        search = input("Enter the name of the book: ")
        found = False
        for book in self.book_list:
            if book.name == search:
                print(f"The book is found! \n Name: {book.name}, Author: {book.author_name}, ID: {book.book_id}, Shelf: {book.shelf}, Status: {book.status}")
                found = True
                break
        if not found:
            print("The book is not found in the library!")

    def status_of_book(self):
        if not self.current_user:
            print("Please login first.")
            return
        os.system("cls")
        search = input("Enter the name of the book to know its status: ")
        found = False
        for book in self.book_list:
            if book.name == search:
                print(f"The book status is: {book.status}")
                found = True
                break
        if not found:
            print("Invalid input!")

    def edit_book(self):
        if not self.current_user:
            print("Please login first.")
            return
        os.system("cls")
        search = input("Enter the name of the book to edit: ")
        found = False
        for book in self.book_list:
            if book.name == search:
                found = True
                while True:
                    print('''
                        Enter 1 to change book shelf
                        Enter 2 to change status
                        Enter 0 to exit
                    ''')
                    ch = input("Enter your choice: ")
                    if ch == '1':
                        new_shelf = int(input("Enter the new shelf of the book: "))
                        book.shelf = new_shelf
                        print(f"The book shelf is updated to {new_shelf} successfully!")
                    elif ch == '2':
                        new_status = input("Enter the new status of the book: ")
                        book.status = new_status
                        print("The book status is updated successfully!")
                    elif ch == '0':
                        break
                    else:
                        print("Enter a valid input!")
        if not found:
            print("The book is not found.")

    def remove_book(self):
        if not self.current_user:
            print("Please login first.")
            return
        os.system("cls")
        search = input("Enter the name of the book you want to remove: ")
        found = False
        for book in self.book_list:
            if book.name == search:
                self.book_list.remove(book)
                print("The book is removed from the library successfully!")
                found = True
                break
        if not found:
            print("The book is not found!")

    def exit_system(self):
        quit()

def draw_welcome_sign():
    screen = turtle.Screen()
    screen.bgcolor("lightblue")  # Set background color
    
    pen = turtle.Turtle()
    pen.speed(0)  # Set drawing speed to fastest
    
    # Draw "Welcome"
    pen.color("darkblue")
    pen.penup()
    pen.goto(-100, 50)
    pen.pendown()
    pen.write("Welcome", font=("Arial", 24, "bold"))
    
    # Draw "to this Library"
    pen.penup()
    pen.goto(-150, 0)
    pen.pendown()
    pen.write("to this Library", font=("Arial", 24, "bold"))
    
    # Draw "Management System"
    pen.penup()
    pen.goto(-200, -50)
    pen.pendown()
    pen.write("Management System", font=("Arial", 24, "bold"))
    
    pen.hideturtle()

    turtle.done()

def main():
    draw_welcome_sign()
    library = Library()

    while True:
        print('''WELCOME TO THIS LIBRARY MANAGEMENT SYSTEM!!!
              Press 1 to register
              Press 2 to login
              Press 3 to add new books
              Press 4 to display books
              Press 5 to search books
              Press 6 to check status of the books
              Press 7 to edit books
              Press 8 to remove books
              Press 0 to exit the program''')
        ch = input("Enter your choice: ")
        if ch == '1':
            library.register()
        elif ch == '2':
            library.login()
        elif ch == '3':
            library.add_book()
        elif ch == '4':
            library.display()
        elif ch == '5':
            library.search()
        elif ch == '6':
            library.status_of_book()
        elif ch == '7':
            library.edit_book()
        elif ch == '8':
            library.remove_book()
        elif ch == '0':
            library.exit_system()
        else:
            print("Please enter a valid input!")

if __name__ == "__main__":  
    main()