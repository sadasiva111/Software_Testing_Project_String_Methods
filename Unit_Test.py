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
    
    #Author Venkata Vamsi Krishna Teeparthi
    #Unit Test of Task_4
    #Test passes if all the letters are in lowercase
    def test_islower_string(self):
        output = string_methods_application.islower_string("software testing")
        self.assertTrue(output)

    #Unit Test of Task_5
    #Test passes if it converts all the uppercase to lowercase
    def test_casefold_string(self):
        output = string_methods_application.casefold_string("SOFTWARE TESTING.")
        self.assertEqual(output, "software testing.")
    
    #Unit Test of Task_6
    #Test passes if it returns true when the end value is specified value
    def test_endswith_string(self):
        output = string_methods_application.endswith_string("Software Testing.")
        self.assertTrue(output, ".")

    #Unit test without functionality
    #Author Sree Chandan Kamireddi
    #Unit Test of Task_7
    #Test passes if it counts and returns the specific value in a given string
    def test_count_string(self):
        output = string_methods_application.count_string("Software testing")
        self.assertEqual(output, 1)
    
    #Unit Test of Task_8
    #Test passes when string is converted into a title form.
    def test_title_string(self):
        output = string_methods_application.title_string("software testing")
        self.assertEqual(output, "Software Testing")

    #Unit Test of Task_9
    #Test case passes when the string is encoded.
    def test_encode_string(self):
        output = string_methods_application.encode_string("Software")
        self.assertEqual(output,b'Software')