# Library Management System

<img src="https://img.shields.io/badge/build-passing-success"> <img src="https://img.shields.io/badge/Python-3.8.10-blueviolet"> <img src="https://img.shields.io/badge/Django-3.2.6-blue"> <img src="https://img.shields.io/badge/SQLite-9cf"> <img src="https://img.shields.io/badge/Bootstrap--4-blueviolet"> <img src="https://img.shields.io/badge/LMS-red">




## Installation

Clone this repo or just download directly from github and activate virtualenv.<br> 
if you are in mac or linux then

```bash
source venv/bin/activate
```
if you are in windows then
```
venv\Scripts\activate
```
## Required Packages

Install all required packages via
```
pip install -r requirements.txt
```
## Usage

Then type this command in your terminal/command prompt
```
python manage.py runserver
```
go to the link http://127.0.0.1:8000 and Boooom welcome to fully functional LMS

## LMS Functionalities
 - Sign up, Sign in and Logout
 - Password and Email reset/change (used - django.contrib.auth.urls)
 - A special Admin Dashboard to view everything and perform CRUD operations (not default django admin panel)
 - User can issue and return books by just a single click of Issue and Return buttons
 - Search functionality for both books along with already issued books and can be searched by ISBN number, book name, user id number and category title
 - Books will be expired within 30 days
 - Some necessary functionalities will be added soon...
 
## Roles

 <b>Readers</b>:
  - Sign up, Sign in, log out, reset password and email, 
  - View all the books
  - Search for a book and view a book info
  - Issue books
  - Return books 
  - View all his/her issued books

 <b>Admin</b>:
  - Anything that readers can do
  - Perform CRUD operations on books and categories

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
