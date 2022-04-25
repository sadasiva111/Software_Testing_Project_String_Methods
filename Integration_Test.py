#Lets Start with integration tests
#Integration test cases for string methods
import unittest
from String_Methods_Application import string_methods_application

class TestStringMethods(unittest.TestCase):
    
    #Author : Boya Sada Siva Kumar
    #Integration Test Case 1
    #Integrating startswith and replace string methods

    def test_integration_test_case_1(self):
        output = string_methods_application.startswith_string(string_methods_application.capitalize_string("software testing."))
        self.assertTrue(output)

    #Author : Vamsi Krishna Teeparthi
    #Integration Test Case 2
    #Integrating endswith and casefold string methods
    def test_integration_Task_2(self):
        output = string_methods_application.endswith_string(string_methods_application.casefold_string("SOFTWARE TESTING."))
        self.assertTrue(output, ".")