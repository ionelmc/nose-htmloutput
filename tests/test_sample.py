import unittest
from nose.exc import SkipTest


class MainTestCase(unittest.TestCase):
    def test_a(self):
        self.assertTrue(1)

    def test_b(self):
        self.assertTrue(0, "Some details")


class SecondTestCase(unittest.TestCase):
    def test_a(self):
        self.assertTrue(1)

    def test_b(self):
        self.assertTrue(1)


def test_a():
    assert 1


def test_b():
    raise RuntimeError("Some other details")

def test_c():
    raise SkipTest('skipped')
