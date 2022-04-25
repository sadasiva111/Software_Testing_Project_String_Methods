#String Methods in Python

class string_methods_application:
    
    #Author : Boya Sada Siva Kumar
    #converts the first letter of the string to capital letter.
    def capitalize_string(my_string):
        return my_string.capitalize()

    #Author : Boya Sada Siva Kumar
    #Returns true if the start value is specified value
    def startswith_string(my_string):
        return my_string.startswith("Software")

    #Author : Boya Sada Siva Kumar
    #Replaces the old string with new string
    def replace_string(my_string):
        return my_string.replace("software", "unit")
        
    #Author Venkata Vamsi Krishna Teeparthi
    #Returns true if all the letters are in lowercase
    def islower_string(my_string):
        return my_string.islower()
        

    #Converts all the uppercase to lowercase
    def casefold_string(my_string):
        return my_string.casefold()

    #Returns true if the end value is a specified value
    def endswith_string(my_string):
        return my_string.endswith(".")

    #code with right functionality
    #Author Sree Chandan Kamireddi
    #Converts string into title form
    def title_string(my_string):
        return my_string.title()

    #Counts and returns the specific value in a given string
    def count_string(my_string):
        return my_string.count("Software")

    #Converts string into a encoded form
    def encode_string(my_string):
        return my_string.encode()
    
    