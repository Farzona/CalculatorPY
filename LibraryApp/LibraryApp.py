def convertable_to_int(a):
    try:
        int(a)
        return True
    except:
        return False


choice = None

while choice != '0':
    print("== Library ==")
    print("Choose Action :")
    print("0) Exit")
    print("1) Add new book")
    print("2) Show book")

    choice = input()

    title = ''
    author = ''
    year = None

    if choice == '1':
        more_book = None
        
        while more_book != 'no':
            print("== New book ==")
            while title == '':
                print("Enter title:")
                title = input()
                title = title.strip()
            while author == '':
               print("Enter author:")
               author = input()
               author  =  author.strip() 
            while type (year).__name__ != 'int':
                print("Enter year: ")
                year = input()
                if convertable_to_int(year) == True:
                    year = int(year)
            
        
            print("Do you want to add one more book? [Yes|No]")
            more_book = input()
            more_book = more_book.lower()
            if more_book == 'no' or more_book == 'n':
                more_book = 'no'
                
            title = ''
    
    elif  choice == '0':
        print('Are you sure? [Yes|No]')
        sure = input() # sure => 'Y'
        sure = sure.lower() # sure => 'y'

        if sure == 'y' or sure == 'yes': # 'y' != 'Y'
            print('Bye!!')
        elif sure == 'n' or sure == 'no':
            choice = None












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