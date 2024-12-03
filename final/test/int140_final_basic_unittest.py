import unittest

from int140_final_basic import *

class TestINT140FinalBasic(unittest.TestCase):

    @staticmethod
    def _cases_testing(assertion, func, cases, expected=True):
        for case in cases:
            assertion(func(*case),
                msg=f"input: {case if len(case) > 1 else case[0]} -> expected: {expected}")

    @staticmethod
    def _cases_comparing(assertion, func, cases):
        for expected, case in cases:
            assertion(expected, func(*case),
                msg=f"input: {case if len(case) > 1 else case[0]} -> expected output: {expected}")

    def _cases_raising(self, exception, func, cases):
        for case in cases:
            with self.assertRaises(exception,
                    msg=f"input: {case if len(case) > 1 else case[0]} -> expected: {exception.__name__}"):
                func(*case)

    def test_func01(self):
        # func01(num1, num2) # num1 less than num2
        true_cases = [
            (1.1, 9.9),  # funct01(1.1, 9.9) returns True
            (-19, -2),
            (4, 12.0),
            (0, 3)
        ]
        false_cases = [
            (0, 0),  # func01(0, 0) return False
            (3.0, 3),
            (-3, -9),
            (9.9, 7.11)
        ]
        self._cases_testing(self.assertTrue, func01, true_cases)
        self._cases_testing(self.assertFalse, func01, false_cases, False)

    def test_func02(self):
        # func02(str1, str2) # str1 is a part of str2
        true_cases = [
            ('', ''),   # func02('', '') returns True
            ('', ' '),
            (' ', 'in between'),
            ('lie', 'believe')
        ]
        false_cases = [
            (' ', ''),  # func02(' ', '') returns False
            ('ive', 'retrieve'),
            ('eve', 'archive'),
            ('ive', 'achieve')
        ]
        self._cases_testing(self.assertTrue, func02, true_cases)
        self._cases_testing(self.assertFalse, func02, false_cases, False)

    def test_func03(self):
        # func03(side1, side2) # Pythagoras triangle
        test_cases = [
            (5.0, (3.0, 4)),  # func03(3.0, 4) returns 5.0
            (13.0, (12, 5)),
            (25.0, (24.0, 7.0))
        ]
        raise_cases = [
            (0, 0),  # func03(0, 0) raise ValueError
            (-1, 3),
            (0, -4),
            (-3, -4),
            (4, 0)
        ]
        self._cases_comparing(self.assertAlmostEqual, func03, test_cases)
        self._cases_raising(ValueError, func03, raise_cases)

    def test_func04(self):
        # func04(list) # counts the number of even numbers
        test_cases = [
            (0, ([],)),  # func04([]) returns 0
            (0, ([3],)),
            (1, ([4],)),
            (1, ([-3, -8],)),  # func04([-3, -8]) returns 1
            (4, ([3, -2, 7, 0, 12, 6, -9],)),
        ]
        self._cases_comparing(self.assertEqual, func04, test_cases)


    def test_func05(self):
        # func05(list, value) # counts the number of list members less than value
        test_cases = [
            (0, ([], 5)),  # func05([], 5) returns 0
            (4, ([20, 70, -30, 40, 20], 50)),
            (2, (['p', 'y', 'a', 'w', 'f', 'x'], 'k')),
            (3, ([6, -12.5, 71, 4, 10], 9.9)),
        ]
        self._cases_comparing(self.assertEqual, func05, test_cases)

    def test_func06(self):
        # func06(num) # returns a list of [0, ..., num]
        test_cases = [
            ([0], (0,)),  # func06(0) returns [0]
            ([0, -1], (-1,)),
            ([0, -1, -2], (-2,)),  # func06(-2) returns [0, 1, 2]
            ([0, -1, -2, -3], (-3,)),
            ([0, 1], (1,)),
            ([0, 1, 2], (2,)),
            ([0, 1, 2, 3, 4], (4,)),
        ]
        self._cases_comparing(self.assertEqual, func06, test_cases)

    def test_func07(self):
        # func07(list) # returns the sum of all string length
        test_cases = [
            (0, ([],)),  # func07([]) returns 0
            (0, ([''],)),
            (0, (['', '', ''],)),
            (3, (['a', 'b', '', 'c'],)),  # func07(['a', 'b', '', 'c']) returns 3
            (11, (['one', 'two', 'three'],)),
        ]
        self._cases_comparing(self.assertEqual, func07, test_cases)

    def test_func08(self):
        # func08(list) # returns the concatenation of the first letter of all strings
        test_cases = [
            ('', ([],)),
            ('', ([''],)),
            ('', (['', ''],)),
            ('ae', (['abcd', 'efg'],)),  # func08(['abcd', 'efg']) returns 'ae'
            ('i o', (['ijk', ' ', 'opqr', ''],)),
        ]
        self._cases_comparing(self.assertEqual, func08, test_cases)

    def test_func09(self):
        # func09(list) # returns the occurrences of the smallest values
        test_cases = [
            (0, ([],)),
            (1, ([''],)),
            (4, (['g', 'g', 'g', 'g'],)),  # func09(['g', 'g', 'g', 'g']) returns 4
            (1, ([' ', '', ' ', 'a', 'a'],)),
            (3, ([-7, -12, 8, -12, -7, 9, -12],)),
            (3, (['abcd', 'efg', 'a', 'efg', 'a', 'a', 'abcd'],)),
        ]
        self._cases_comparing(self.assertEqual, func09, test_cases)

    def test_func10(self):
        # func1(list) # returns the second-smallest value
        test_cases = [
            (None, ([],)),
            (None, (['x'],)),
            (None, ([5, 5],)),
            (4, ([3, 4],)),
            ('b', (['b', 'a'],)),
            (-11, ([300, -11, -20, -11, 300, -20, 50000, 300, 4000],)),
            ('c', (['pqr', '', 'pqr', 'c', '', 'st', '', 'c', 'st', 'c', 'xyz'],)),
        ]
        self._cases_comparing(self.assertEqual, func10, test_cases)


if __name__ == '__main__':
    unittest.main()