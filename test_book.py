import unittest
from book import total_pages

class TestBookFunctions(unittest.TestCase):
    def test_total_pages(self):
        books = [
            {"title": "Book A", "author": "A", "pages": 100},
            {"title": "Book B", "author": "B", "pages": 200}
        ]
        result = total_pages(books)
        self.assertEqual(result, 300)

    def test_wrong_total(self):
        books = [
            {"pages": 100},
            {"pages": 200}
        ]
        result = total_pages(books)
        self.assertNotEqual(result, 500)
        

if __name__ == "__main__":
    unittest.main()