import unittest

from int140_final_functional import *

class TestINT140FinalFunctional(unittest.TestCase):

    @staticmethod
    def _cases_comparing(assertion, func, cases):
        for expected, case in cases:
            assertion(expected, func(*case),
                msg=f"input: {case if len(case) > 1 else case[0]} -> expected output: {expected}")

    def test_func01(self):
        # func01(list) # counts the number of even numbers
        test_cases = [
            (0, ([],)),  # func01([]) returns 0
            (0, ([3],)),
            (1, ([4],)),
            (1, ([-3, -8],)),  # func01([-3, -8]) returns 1
            (4, ([3, -2, 7, 0, 12, 6, -9],)),
        ]
        self._cases_comparing(self.assertEqual, func01, test_cases)


    def test_func02(self):
        # func02(list, value) # counts the number of list members less than value
        test_cases = [
            (0, ([], 5)),  # func02([], 5) returns 0
            (4, ([20, 70, -30, 40, 20], 50)),
            (2, (['p', 'y', 'a', 'w', 'f', 'x'], 'k')),
            (3, ([6, -12.5, 71, 4, 10], 9.9)),
        ]
        self._cases_comparing(self.assertEqual, func02, test_cases)

    def test_func03(self):
        # func03(num) # returns a list of [0, ..., num]
        test_cases = [
            ([0], (0,)),  # func03(0) returns [0]
            ([0, -1], (-1,)),
            ([0, -1, -2], (-2,)),  # func03(-2) returns [0, 1, 2]
            ([0, -1, -2, -3], (-3,)),
            ([0, 1], (1,)),
            ([0, 1, 2], (2,)),
            ([0, 1, 2, 3, 4], (4,)),
        ]
        self._cases_comparing(self.assertEqual, func03, test_cases)

    def test_func04(self):
        # func04(list) # returns the sum of all string length
        test_cases = [
            (0, ([],)),  # func04([]) returns 0
            (0, ([''],)),
            (0, (['', '', ''],)),
            (3, (['a', 'b', '', 'c'],)),  # func04(['a', 'b', '', 'c']) returns 3
            (11, (['one', 'two', 'three'],)),
        ]
        self._cases_comparing(self.assertEqual, func04, test_cases)

    def test_func05(self):
        # func05(list) # returns the concatenation of the first letter of all strings
        test_cases = [
            ('', ([],)),
            ('', ([''],)),
            ('', (['', ''],)),
            ('ae', (['abcd', 'efg'],)),  # func05(['abcd', 'efg']) returns 'ae'
            ('i o', (['ijk', ' ', 'opqr', ''],)),
        ]
        self._cases_comparing(self.assertEqual, func05, test_cases)

    def test_func06(self):
        # func06(list) # returns the occurrences of the smallest values
        test_cases = [
            (0, ([],)),
            (1, ([''],)),
            (4, (['g', 'g', 'g', 'g'],)),  # func06(['g', 'g', 'g', 'g']) returns 4
            (1, ([' ', '', ' ', 'a', 'a'],)),
            (3, ([-7, -12, 8, -12, -7, 9, -12],)),
            (3, (['abcd', 'efg', 'a', 'efg', 'a', 'a', 'abcd'],)),
        ]
        self._cases_comparing(self.assertEqual, func06, test_cases)

    def test_func07(self):
        # func07(list, func) # returns the count of func(value) equal to true
        test_cases = [
            (0, ([], lambda _: True)),
            (0, (['anything', 100.0, 'everything'], lambda _: False)),
            (4, ([8, -3, 6, -2, 7, 6, 1, 7, 9, -23], lambda x: x % 2 == 0)),
            (3, (['alive', 'nothing', 'ocean', 'another', 'no one'], lambda x: 'a' in x)),
        ]
        self._cases_comparing(self.assertEqual, func07, test_cases)

    def test_func08(self):
        # func07(list) # returns the second-smallest value
        test_cases = [
            (None, ([],)),
            (None, (['x'],)),
            (None, ([5, 5],)),
            (4, ([3, 4],)),  # func08([3, 4]) returns 4
            ('b', (['b', 'a'],)),
            (-11, ([300, -11, -20, -11, 300, -20, 50000, 300, 4000],)),
            ('c', (['pqr', '', 'pqr', 'c', '', 'st', '', 'c', 'st', 'c', 'xyz'],)),
        ]
        self._cases_comparing(self.assertEqual, func08, test_cases)


if __name__ == '__main__':
    unittest.main()
