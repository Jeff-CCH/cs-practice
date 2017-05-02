"""
Write a Python program that simulates a system that supports the func- tions of an e-book reader. You should include methods for users of your system to "buy" new books, view their list of purchased books, and read their purchased books. Your system should use actual books, which have expired copyrights and are available on the Internet, to populate your set of available books for users of your system to "purchase" and read
"""

class Book(object):
    def __init__(self, title, expired_date, content, price, expired=False):
        self._title = title
        self._expired_d = expired_date
        self._content = content
        self._price = price
        self._expired = expired

    def purchase(self):
        print "cost you %s dollars" % self._price

    def read(self):
        return self._content

    def get_title(self):
        return self._title

    def is_expired(self):
        return self._expired
        
class EBookReader(object):
    def __init__(self, book_list=[]):
        self._book_list = book_list

    def purchase(self, book):
        book.purchase()
        self._book_list.append(book)

    def view(self):
        for book in self._book_list:
            if self._is_expired(book) is True:
                print "%s is expired and is removed from your list" % book.get_title()
                self._book_list.remove(book)
            else: print book.get_title()

    def read(self, book):
        print book.read()

    def _is_expired(self, book):
        return True if book.is_expired() else False

def main():
    b1 = Book("Formosa", "2017-10-26", "Hello, my love.", "25.0") 
    b2 = Book("Wars", "1990-10-26", "Hello, my love.", "25.0", True) 
    b3 = Book("3D Anime", "1987-10-26", "Hello, my love.", "25.0", True) 

    book_list = []
    book_list.append(b1)
    book_list.append(b2)

    e = EBookReader(book_list)
    e.purchase(b3)
    e.read(b1)
    e.view()

if __name__ == '__main__':
    main()
