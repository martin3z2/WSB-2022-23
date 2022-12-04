import unittest

class MyTestCase(unittest.TestCase):
    def test_one3(self):
        print("test: test_one3")
        pass

    def test_one2(self):
        print("test: test_one2")
        pass

    def test_one(self):
        print("test: test_one")
        pass

    def test_2(self):
        print("test: test_2")
        pass

    def notest(sef):
        print("test: notest")
        pass

class MyTestCase2(unittest.TestCase):
    def test_one3b(self):
        print("test: test_one3b")
        pass

    def test_one2b(self):
        print("test: test_one2b")
        pass

    def test_one_b(self):
        print("test: test_oneb")
        pass

    def test_2b(self):
        print("test: test_2b")
        pass

    def notest_b(sef):
        print("test: notestb")
        pass

if __name__ == "__main__":
    unittest.main()
