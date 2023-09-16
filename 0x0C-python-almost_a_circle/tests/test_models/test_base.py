import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(12)
        self.rect_1 = Rectangle(5, 7, 2, 3, 8)

    def test_checkId(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 12)

    def test_save_to_file(self):
        Rectangle.save_to_file([self.rect_1])
        with open("Rectangle.json") as file:
            content = file.read()
        expected= '[{"x": 2, "y": 3, "id": 8, "width": 5, "height": 7}]'
        self.assertEqual(content, expected)


if __name__ == "__main__":
    unittest.main()
