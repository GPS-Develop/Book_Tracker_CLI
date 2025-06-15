import unittest
from book import get_book_titles

class TestBookTitles(unittest.TestCase):
    def test_returns_title_from_books(self):
        books = [
            {"title": "test1"},
            {"title": "test2"}
        ]
        result = get_book_titles(books)
        self.assertEqual(result,  ["test1", "test2"])
        
if __name__ == "__main__":
    unittest.main()
