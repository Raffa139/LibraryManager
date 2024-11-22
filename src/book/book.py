class Book:
    def __init__(self, title, author, year, borrowed, keywords=()):
        self.title = title
        self.author = author
        self.year = year
        self.borrowed = borrowed
        self.keywords = keywords

    def borrow(self):
        """
        Mark the book as borrowed.
        """
        self.borrowed = True

    def give_back(self):
        """
        Mark the book as returned.
        :return:
        """
        self.borrowed = False

    def keyword_strs(self):
        return [keyword.value for keyword in self.keywords]

    def __str__(self):
        keywords = f"({', '.join(self.keyword_strs())})" if len(self.keywords) > 0 else ""
        return f"{'[x]' if self.borrowed else '[v]'} {self.title} by {self.author} from {self.year} {keywords}"
