#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: ossdev

import unittest
from ossdev import Vector


class VectorTest(unittest.TestCase):
    """Simple vector tests"""

    def __init__(self, *args, **kwargs):
        super(VectorTest, self).__init__(*args, **kwargs)

    def test_from_arr(self):
        self.assertEqual(Vector.from_arr([0, 1, 2]).get(), [0, 1, 2])

    def test_from_size(self):
        self.assertEqual(Vector.from_size(3).get(), [0, 0, 0])

    def test_set(self):
        arr = [1, 2, 3]
        vec = Vector()

        self.assertListEqual(vec.set(arr).get(), arr)

    def test_get(self):
        arr = [3, 4, 5]
        vec = Vector(arr)

        self.assertEqual(vec.get(), arr)

    def test_len(self):
        self.assertEqual(len(Vector([1, 2, 3])), 3)

    def test_repr(self):
        self.assertEqual(Vector([0, 1, 2]).__repr__(), "[0, 1, 2]")

    def test_getitem(self):
        self.assertEqual(Vector([0, 2, 1, 3])[2], 1)

    def test_hash(self):
        self.assertEqual(Vector([2, 6, 5]).__hash__(), 13)

    def test_setitem(self):
        vec1 = Vector([4, 2, 1, 5])
        vec1[2] = 10

        self.assertListEqual(vec1.get(), [4, 2, 10, 5])

        vec2 = Vector([1, 2, 3])
        vec2[5] = 7

        self.assertListEqual(vec2.get(), [1, 2, 3, 0, 0, 7])

    def test_neg(self):
        self.assertEqual((-Vector([1, 1, 1])).get(), [-1, -1, -1])

    def test_reversed(self):
        vec = Vector([1, 5, 6])
        self.assertEqual(list(reversed(vec)), [6, 5, 1])

    def test_add(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([3, 2, 1, 0])
        c = a + b

        self.assertEqual(c.get(), [3, 3, 3, 3])

    def test_dot(self):
        a = Vector([1, 2])
        b = Vector([2, -1])
        self.assertEqual(a.dot(b), 0)

    def test_sub(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([3, 2, 1, 0])
        c = a - b

        self.assertListEqual(c.get(), [-3, -1, 1, 3])

    def test_mul(self):
        vec = Vector([0, 1, 2, 3])

        self.assertListEqual((vec * 2).get(), [0, 2, 4, 6])

    def test_xor(self):
        arr = [0, 1, 2, 3]
        vec = Vector(arr)

        self.assertListEqual((vec ^ 7).get(), [x ^ 7 for x in vec])

    def test_length(self):
        vec1 = Vector([0, 3, 4])
        vec2 = Vector([10, 0, 0])

        self.assertEqual(vec1.length(), 5)
        self.assertEqual(vec2.length(), 10)


class MatrixTest(unittest.TestCase):
    def __inti__(self):
        self.sorry = "again here should be some tests for Matrix but I didn't really have time for that at this point"


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
    test = VectorTest()

    test.test_from_arr()
    test.test_from_size()
    test.test_set()
    test.test_get()
    test.test_len()
    test.test_repr()
    test.test_getitem()
    test.test_hash()
    test.test_setitem()
    test.test_neg()
    test.test_reversed()
    test.test_add()
    test.test_sub()
    test.test_mul()
    test.test_xor()
    test.test_length()
