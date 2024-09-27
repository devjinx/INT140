# submit 2 files with the following names 
# by replacing 00 with your group number
# c07_thu11_unittest.py --> your unit test of your previous submission
# c07_thu11_review.py --> modify from your previous submission
# include all student id and name in both files as follow:
# Thanakorn Chareonlertkamol 081
# Bannawit Sanngern 095
# Napat Adam 129
# Natthawat Suwansupawong 130

from c07_thu11_unittest import *
import unittest

class TestReview(unittest.TestCase):

    def test_km_to_mile_valid(self):
        testdata = [5, 3.5, 8.2, 0, 6795.33646]
        for i in testdata:
            print(f"km_to_mile({i})")
            self.assertAlmostEqual(km_to_mile(i), i * 0.621371192, 5)

    def test_km_to_mile_neg(self):
        testdata = [-0.4, -3.6, -0.0001]
        for i in testdata:
            print(f"km_to_mile({i})")
            with self.assertRaises(ValueError):
                km_to_mile(i)

    def test_km_to_mile_invalid(self):
        testdata = ['a', "xyz", [1, 2, 3]]
        for i in testdata:
            print(f"km_to_mile({i})")
            with self.assertRaises(TypeError):
                km_to_mile(i)

    def test_consecutive_char(self):
        testdata = ["hello", "world", "a", "aa", 123, ['hello']]
        for i in testdata[:4]:
            print(f"consecutive_char({i})")
            if i in ["hello", "aa"]:
                self.assertTrue(consecutive_char(i))
            else:
                self.assertFalse(consecutive_char(i))

        for i in testdata[4:]:
            print(f"consecutive_char({i})")
            with self.assertRaises(TypeError):
                consecutive_char(i)

    def test_duplicate(self):
        testdata = ["hello", "world", "aabbcc", "abc", 123, ['hello']]
        for i in testdata[:4]:
            print(f"duplicate({i})")
            if i in ["hello", "aabbcc"]:
                self.assertTrue(duplicate(i))
            else:
                self.assertFalse(duplicate(i))

        for i in testdata[4:]:
            print(f"duplicate({i})")
            with self.assertRaises(TypeError):
                duplicate(i)

    def test_max_value(self):
        testdata = [(1, 2, 3), (10, 5, 2), (1, 1, 1), (-5, -10, -3), (1, 2, "three"), ([1], 2, 3)]
        for i in testdata[:4]:
            print(f"max_value({i})")
            self.assertEqual(max_value(*i), max(i))  

        for i in testdata[4:]:
            print(f"max_value({i})")
            with self.assertRaises(TypeError):
                max_value(*i)

if __name__ == "__main__":
    unittest.main()