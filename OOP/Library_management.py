"""
1, A method to display the books available
2, A method to lend a book
3, A method to add donated books
4, A method for returned book
"""
import time
def get_time():
    print(time.asctime())
get_time()

class Library:
    lst_books = ["a", "b", "c", "d", "e"]
    data_lib = {}
    dntr_dtl = {}
    def __init__(self, name):
        self.name = name

    def dplay_books(self):
        return self.lst_books

    def lnd_books(self):
        print("Please Enter the name of book you wish to borrow.")
        wish = input()
        if wish in self.lst_books:
            self.data_lib.setdefault(wish, self.name)
            self.lst_books.remove(wish)
        else:
            print(f"Unavailable.!!\n{self.data_lib[wish]} currently owns this book.")
        return f"Thank You {self.name} for choosing us."

    def add_book(self):
        print("Please Enter the name of the book you wish to donate.")
        n_book = input()
        self.dntr_dtl.setdefault(self.name, n_book)
        return  "We are grateful for your generosity.!"

    def rtrn_book(self):
        print("Please Enter the name of the book.")
        nm_book = input()
        self.lst_books.append(nm_book)
        self.data_lib.pop(nm_book)
        return "We are grateful for your honesty.!"

name = input()
roc = Library(name)
while True:
    print("Press 's' to see books available.\nPress 'b' to borrow a book.\nPress 'r' to return\nPress 'd' to donate a book.\nPress 'Enter' to exit.")
    wish_cstmr = input()
    if wish_cstmr == "s":
        print(roc.lst_books)
    elif wish_cstmr == "b":
        print(roc.lnd_books())
    elif wish_cstmr == "r":
        print(roc.rtrn_book())
    elif wish_cstmr == "d":
        print(roc.add_book())
    elif wish_cstmr == "":
        break
    else:
        continue
print(roc.data_lib)
print(roc.dntr_dtl)








