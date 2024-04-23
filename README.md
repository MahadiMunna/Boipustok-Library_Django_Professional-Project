# Boipustok-Library_Django_Professional-Project

This project is based on Library Management System where users can see books, borrow books, see book details, and review that book. <b>4 apps (books, core, users, transactions)</b> used here to build this system.
# Books
Every book has title, description, category, image, borrowing price and user reviews. There is a functionality where user can filter books based on categories.
# Users
Here a user can create an account, Can login, logout,can borrow and return books. Users can deposit money to his account. After successfull deposit a confirmation email sent to the user. Using the deposit money user can borrow books. After success user get a completion email. Suppose a user has 1000 taka in his account. He borrowed a book that cost 200 taka. After borrowing the book he will have 800 taka. The system also keep track all the transaction and able to see borrowing history report inside user profile.After borrowing a book, the user can review that book. When a user returned book, the book borrowed amount will be given to the user. This record also kept in the database.
# Transactions
Transaction app used here to keep record of user transaction. When user deposit money, borrow book and return book, in those time this app keep track of amount, balance after transaction, user information, book information and date-time.
# Core
This app is the core of this project. All the basic templates rendered from here. Contact method implemented here. User can give feedback to the developer.
# Used Technologies
1. Django
2. Bootstrap
3. Crispy Form
4. db.sqlite3
5. smtp.EmailBackend
6. host: on-render

# live: https://boipustok-library.onrender.com/
NB: You may need to wait upto 1minute to render live link!

