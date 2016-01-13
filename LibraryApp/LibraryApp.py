import re


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


def prepare_year(year):
    if len(year) != 4:
        print('ERROR: incorrect year')
        return None

    if convertable_to_int(year) == True:
        year = int(year)
    else:
        print('ERROR: incorrect year')
        return None

    return year


def prepare_author(author):
    result = ''

    author = author.strip()

    template = '[a-zA-Z ]+'
    if re.fullmatch(template, author) != None:
        result = author

    return result


def prepare_title(title):
    result = ''

    title = title.strip()

    template = '[a-zA-Z ]+'
    if re.fullmatch(template, title ) != None: 
        result = title 

    return result


choice = None
add = None
while choice != '0':
    print("== Library ==")
    print("Choose Action :")
    print("0) Exit")
    print("1) Add new book")
    print("2) Find book")
    print("3) Books")
    print("4) Delete")
    print("5) Update")

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
                title = prepare_title(title)

            while author == '':
               print("Enter author:")
               author = input()
               author = prepare_author(author)

            while type (year).__name__ != 'int':
                print("Enter year: ")
                year = input()
                year = prepare_year(year)


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

                message = 'Book with such author was not found'

                for book in books:
                    if book.author == author:
                        message = 'Book was found'

                print(message)

            if search_choice == '2':
                print('Enter the title of book: ')
                title = input()

                message = 'Book with such title was not found'

                for book in books:
                    if book.title == title:
                       message = 'Book was found'
                    
                print(message)

            if search_choice == '3':
                print('Enter the year of book: ')
                year = input() 
                year = prepare_year(year)

                message = 'Book with such year was not found'

                for book in books:
                    if book.year == year:
                        message = 'Book was found'
                    
                        print(message)

    elif  choice == '3':
        print("== Books list ==")
        print("title \t\t author \t\t year")
        
        if len(books) > 0:
            for book in books:
                row = book.title + '\t' + book.author + '\t' + str(book.year)
                print(row)
                #print(book.title + '\t' + book.author + '\t' + str(book.year))
        input()

   
    elif choice == '4':
        print('==Delete==')
        print('Choose action:')
        print('0) Back to main menu')
        print('1) Delete by title')
        print('2) Delete by author')
        print('3) Delete by year')



        delete_choice = input()

        if delete_choice == '0':
            delete = 'no'
         
        elif delete_choice == '1':
            print('Enter the title of book: ')
            title = input()

            for book in books:
                if book.title == title:
                    row = book.title + '\t' + book.author + '\t' + str(book.year)
                    print("\ntitle \t\t author \t\t year")
                    print(row)
                    
                    print('\nDo you want to delete this book? [Yes|No] ')
                    delete_book = input()
                    
                    if delete_book == 'yes' or delete_book == 'y':
                        books.remove(book)
                        print('book was deleted')

        elif delete_choice == '2':
            print('Enter the author of book: ')
            author = input()

            for book in books:
                if book.author == author:
                    row = book.title + '\t' + book.author + '\t' + str(book.year)
                    print("\ntitle \t\t author \t\t year")
                    print(row)
                    
                    print('\nDo you want to delete this book? [Yes|No] ')
                    delete_book = input()
                    
                    if delete_book == 'yes' or delete_book == 'y':
                        books.remove(book)
                        print('book was deleted')

        elif delete_choice == '3':
            print('Enter the year of book: ')
            year = input()
            year = prepare_year(year)

            for book in books:
                if book.year == year:
                    row = book.title + '\t' + book.author + '\t' + str(book.year)
                    print("\ntitle \t\t author \t\t year")
                    print(row)
                    
                    print('\nDo you want to delete this book? [Yes|No] ')
                    delete_book = input()
                    
                    if delete_book == 'yes' or delete_book == 'y':
                        books.remove(book)
                        print('book was deleted')
    
    elif choice == '5':
        print('==Update==')
        print('Choose action:')
        print('0) Back to main menu')
        print('1) Update by title')
        print('2) Update by author')
        print('3) Update by year')

        update_choice = input()

        if update_choice == '0':
            update = 'no'
         
        elif update_choice == '1':
            print('Enter the title of book: ')
            title = input()

            for book in books:
                if book.title == title:
                    books.remove(book)
                    print("Enter new title: ")
                    title = input()
                    book.title = prepare_title(title)
                    books.append(book)
                    row = book.title + '\t' + book.author + '\t' + str(book.year)
                    print("\ntitle \t\t author \t\t year")
                    print(row)
                    break;


        elif delete_choice == '2':
            print('Enter the author of book: ')
            author = input()

            for book in books:
                if book.author == author:
                    row = book.title + '\t' + book.author + '\t' + str(book.year)
                    print("\ntitle \t\t author \t\t year")
                    print(row)
                    
                    print('\nDo you want to delete this book? [Yes|No] ')
                    delete_book = input()
                    
                    if delete_book == 'yes' or delete_book == 'y':
                        books.remove(book)
                        print('book was deleted')

        elif delete_choice == '3':
            print('Enter the year of book: ')
            year = input()
            year = prepare_year(year)

            for book in books:
                if book.year == year:
                    row = book.title + '\t' + book.author + '\t' + str(book.year)
                    print("\ntitle \t\t author \t\t year")
                    print(row)
                    
                    print('\nDo you want to delete this book? [Yes|No] ')
                    delete_book = input()
                    
                    if delete_book == 'yes' or delete_book == 'y':
                        books.remove(book)
                        print('book was deleted')               
                        
                        
                              
    elif  choice == '0':
        print('Are you sure? [Yes|No]')
        sure = input() # sure => 'Y'
        sure = sure.lower() # sure => 'y'

        if sure == 'y' or sure == 'yes': # 'y' != 'Y'
            print('Bye!!')
        elif sure == 'n' or sure == 'no':
            choice = None