import CRUD

def viewAll():
    books = CRUD.view()
    return books

def search(title, author, year, isbn):
    books = CRUD.search(title, author, year, isbn)
    return books

def insert(title, author, year, isbn):
    CRUD.insert(title, author, year, isbn)

def update(id, title, author, year, isbn):
    CRUD.update(id, title, author, year, isbn)

def delete(id):
    CRUD.delete(id)




