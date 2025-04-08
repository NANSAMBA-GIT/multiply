import unittest


class TestMultiply(unittest.TestCase):
    def test_first(self):
        self.assertEqual(multiplication(1,1),1)

if __name__ == "__main__":
    unittest.main()