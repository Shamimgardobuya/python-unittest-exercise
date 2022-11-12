import unittest
from python_unittest_exercise.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test0(self):
        data=Calculator(77,8)
        result=data.add()
        self.assertEqual(result,95)

    def test1(self):
        data=Calculator("34")
        result2=data.subtract()
        self.assertEqual(result2,34)
    def test3(self):
        data=Calculator(22,3.4)
        result3=data.divide()
        self.assertEqual(result3,6.47058823529)

    def test4(self):
        data=Calculator(18,9)
        result3=data.multiply()
        self.assertEqual(result3,162)





if __name__ == '__main__':  #entry point for calling function
    unittest.main()