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
        """
        Get the books keywords as strings.
        :return: A list of keywords as strings
        """
        return [keyword.value for keyword in self.keywords]

    def keyword_strs_lower(self):
        """
        Get the books keywords as lower strings.
        :return: A list of keywords as lower strings
        """
        return [k.lower() for k in self.keyword_strs()]

    def __str__(self):
        keywords = f"({', '.join(self.keyword_strs())})" if len(self.keywords) > 0 else ""
        return f"{'[x]' if self.borrowed else '[v]'} {self.title} by {self.author} from {self.year} {keywords}"
