import unittest 
import requests
from python_unittest_exercise.employee import Employee

class TestEmployee(unittest.TestCase):
    def test0(self):

        data=Employee("Shamim","Gard",3400,"August")
        result=data.email()
        self.assertEqual(result,'Shamim.Gard@email.com')

    def test1(self):
        data=Employee("Ashley","Ochwada",3900,"October")
        result2=data.fullname()
        self.assertEqual(result2,'Ashley Ochwada')
    def test3(self):
        data=Employee("Ashley","Ochwada",1000.90,"June")
        result3=data.apply_raise()
        self.assertEqual(result3,1050)



if __name__ == '__main__':  #entry point for calling function
    unittest.main()