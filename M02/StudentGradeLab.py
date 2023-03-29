# Jonathan Leverenz
# StudentGradeLab.py
# This program will allow users to input their last name and grade to see if they made the dean list or honor roll. Program ends with a name of "ZZZ"
# Student_lastname will be a string that contains the current students last name
# Student_firstname will be a string that contains the current students last name
# grade will contain the students grade as a float

# a loop that will continue until a break statement occurs
while (1):

    # Get the student name and check for sentinal value
    student_lastname = input(
        "Please enter the students last name (enter ZZZ to quit) : ")
    if (student_lastname == "ZZZ"):
        break
    student_firstname = input("Please enter the students first name : ")

    # get grade and check that it is an integer
    grade = input("Please enter the students grade : ")
    try:
        grade = float(grade)
        if (grade >= 3.5):
            print("The student has made it on the Dean List!")

        if (grade >= 3.25):
            print("The student has made Honor Roll!")
        else:
            print("The student has not made Honor Roll or the Deans List :(")
    except:
        print("That was not a valid input, Please enter the next student...")

print("Program ended")
