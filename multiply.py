import unittest

def multiplication(a,b):
    return a*b


class TestMultiply(unittest.TestCase):
    def multiply_ones(self):
        self.assertEqual(multiplication(1,1),1)

if __name__ == "__main__":
    unittest.main()