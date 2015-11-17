choice = None

print("==Library==")
print(" Choose Action :")
print("1) Add new book")
print("2) Show book")
choice = input()
title = None
author = None
year = None

if choice == '1':
    print("==New book==")
    print("Enter title:")
    title = input()
    print("Enter author:")
    author = input()
    print("Enter year: ")
    year = input()
    print("Do you want to add one more book? [Yes|No]")
    want = input()
   










"""
class Book:
     title = None
     author = None
     year = None

bookOfFarzona = Book()

books = []

title = input('Name of book: ')
author = input('Author name: ')

bookOfFarzona.title = title
bookOfFarzona.author = author
bookOfFarzona.year = 2123

books.append(bookOfFarzona)

print("Nazvanie knigi Farzony:" + bookOfFarzona.title + "Nazvanie avtora:" + bookOfFarzona.author)


bookOfTimur = Book()

title = input('Name of book: ')
author = input('Author name: ')

bookOfTimur.title = title
bookOfTimur.author = author
bookOfTimur.year = 2014

books.append(bookOfTimur)

print("Nazvanie knigi Timura:" + bookOfFarzona.title + "Nazvanie avtora:" + bookOfFarzona.author)
"""