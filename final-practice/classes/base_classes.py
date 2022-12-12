from abc import ABCMeta, abstractmethod


class Book(metaclass=ABCMeta):

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self):
        """ implement printing on the class """


class MyBook(Book):

    def __init__(self, title: str, author: str, price: float):
        Book.__init__(self, title, author)
        self.price = price

    def display(self):
        print(
            f'Title: {self.title}\nAuthor: {self.author}\nPrice: {self.price}')


novel = MyBook('jack reacher', 'lee childs', 15.99)
novel.display()
