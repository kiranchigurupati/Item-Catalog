# Item Catalog Project-428
The 4th projects made as a part of Udacity Full Stack Web Development Nanodegree.
Project represents a an application that provides a list of items as well as a user registration and authentication system.
Registered users have the ability to use CRUD functionallity, or `post`, `delete`, `edit`.
For User Registration `Google+ Authentification and Authorization service`. `Local Permissions System` was implemented to prevent other user's changes to items uploaded by someone.
# How to start
* Run the project through Flask-env
    `source Flask-env/bin/activate`
* Run the python script `application.py` with the following command:
    `Python populate_book.py`
    `python application.py`
* Access an application by visiting `http://localhost:5000/` locally 
# BookShelf Item Catalog Application
Database contains three tables: 
`genre`, `user`, `book_item`.
Each BookItem belongs to specific Genre, while each User can create both Genre and BookItem in it. Different Users can add BookItems to the Genre,
however, only creator can edit or delete created Genres and BookItems. Not registered users are not able to add, delete or edit anything, but they can see publicly available list of items, which are rendered with `public_genres.html` and `public_books.html`. If authentificated user tries to edit or delete items that were added by another user, alertwindow is shown and the action is aborted.

Each BookItem contains the following attributes: ID (Primary Key), Name, Author, Description, Price, Type (either eBook or HardCopy), GenreID(ForeignKey), UserID(ForeignKey), while Genre has ID (Primary Key), Description, UserID (ForeignKey), User has ID (Primary), Name, Email and Picture that are taken from Google+ account after authentification. 

Python file `populate_book.py` was used to add items to the `new_book_catalog.db` file.
