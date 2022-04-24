#Test case for string methods
import unittest
from String_Methods_Application import string_methods_application

class TestStringMethods(unittest.TestCase):

    #Autour : Boya Sada Siva Kumar
    #Unit Test Case 1
    #Test passes when the first letter of the string is converted to capital letter.    
    def test_capitalize_string(self):
        output = string_methods_application.capitalize_string("software testing")
        self.assertEqual(output, "Software testing")

    #Autour : Boya Sada Siva Kumar
    #Unit Test Case 2
    #Test passes if it returns true when start value is a specified value   
    def test_startswith_string(self):
        output = string_methods_application.startswith_string("Software Testing.")
        self.assertTrue(output)

    #Autour : Boya Sada Siva Kumar
    #Unit Test Case 3
    #Test passes when the old string is replaced with new string
    def test_replace_string(self):
        output = string_methods_application.replace_string("software testing")
        self.assertEqual(output, "unit testing")
