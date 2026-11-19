# -------------------------------------------------------------------------- #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
#       with structured error handling
# Change Log: (Who, When, What)
# Long Tran, 11/17/2026, Created Script
# -------------------------------------------------------------------------- #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
menu_choice: str = ''  # Holds choice made by the user.
students: list = []  # a table of student data

# Processing -----------------------------------#
class FileProcessor:
    """
    A collection of processsing layer functions that work with JSON files
    """
    
    @staticmethod
    def read_data_from_file(file_name:str, student_data: list):
        file = None
        
        # When the program starts, read the file data into a 
        # list of lists (table)
        
        # Function extractx the data from the file
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before" 
                                      " running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file is not None and file.closed == False:
                file.close()
        return student_data
    
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        
        # Function writes data to the file
        file = None

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
        except TypeError as e:
            IO.output_error_messages("Please check that the data"
                                     "is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file is not None and file.closed == False:
                file.close()

# Presentation
class IO:
    """
    A collection of presentation functions that manage user input and output
    """

    @staticmethod
    # Function outputs error messages
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the a menu of choices to the user
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())

        return choice

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the first name, last name, and course taken.
        """

        try:
            # Asks user to input the data
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("Please enter the name of the course: ")          

            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} "
                  f"{student_last_name} for {course_name}.")            

        except ValueError as e:
            IO.output_error_messages("That value is not the" 
                                     " correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data

    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function displays the course taken by the user.
        """
        
        # Process data and display custom message.
        print("-" * 50)
        for student in student_data:
            
                print(f'Student {student["FirstName"]} {student["LastName"]} '
                      f' is enrolled in {student["CourseName"]}')            
        print("-" * 50) 
    
#  End of function definitions
students = FileProcessor.read_data_from_file(file_name=FILE_NAME,
                                             student_data=students)
# Present and Process the data
while (True):

    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        students = IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        IO.output_student_courses(students)
        continue

    elif menu_choice == "3":  # Save data in a file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, 
                                         student_data=students)
        continue

    elif menu_choice == "4":  # End the program
        break  # breaks out of the while loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
