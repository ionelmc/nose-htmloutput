import unittest


class MainTestCase(unittest.TestCase):
    def test_a(self):
        self.assertTrue(1)

    def test_b(self):
        self.assertTrue(0, "Some details")


def test_a():
    assert 1


def test_b():
    assert 0, "Some other details"
