class Book:
     title = None
     author = None
     year = None


books = []


def convertable_to_int(a):
    try:
        int(a)
        return True
    except:
        return False


choice = None
add = None
while choice != '0':
    print("== Library ==")
    print("Choose Action :")
    print("0) Exit")
    print("1) Add new book")
    print("2) Find book")
    print("3) Books")

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

            newBook = Book()
            newBook.author = author
            newBook.title = title
            newBook.year = year            

            books.append(newBook)
        
            print("Do you want to add one more book? [Yes|No]") 
            more_book = input()
            more_book = more_book.lower()
            more_book = more_book.strip()
            if more_book == 'no' or more_book == 'n':
                 more_book = 'no'
            title = ''
            author = ''
            year = None

    elif choice == '2':
        search = None 
        while search != 'no':
            print("== Find book ==")
            print("Choose Action :")
            print("0) Back to main menu")
            print("1) Search by author")
            print("2) Search by title")
            print("3) Search by year")

            search_choice = input()

            if search_choice == '0':
                search = 'no'
         
            if search_choice == '1':
                print('Enter the author of book: ')
                author = input()

                for book in books:
                    if book.author == author:
                        print('Nashli')
                    elif book.author != author:
                        print('Book with such author not found')

            if search_choice == '2':
                print('Enter the title of book: ')
                title = input()

                for book in books:
                    if book.title == title:
                        print('We found out the book you re seaching')
                    elif book.title != title: 
                        print('Book with such title  not found')


            if search_choice == '3':
                print('Enter the year of book: ')
                year = input()

                for book in books:
                    if book.year == year:
                        print('Nashli')
                    elif book.year != year:
                        print('Book with such year not found') 

    elif  choice == '3':
        print('== Books list ==')
        print('title \t\t author \t year')
        
        if len(books) > 0:
            for book in books:
                row = book.title + '\t' + book.author + '\t' + str(book.year)
                print(row)
                #print(book.title + '\t' + book.author + '\t' + str(book.year))
        input()


    elif  choice == '0':
        print('Are you sure? [Yes|No]')
        sure = input() # sure => 'Y'
        sure = sure.lower() # sure => 'y'

        if sure == 'y' or sure == 'yes': # 'y' != 'Y'
            print('Bye!!')
        elif sure == 'n' or sure == 'no':
            choice = None









"""


bookOfFarzona = Book()



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