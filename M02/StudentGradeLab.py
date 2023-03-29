# Jonathan Leverenz
# StudentGradeLab.py
# This program will allow users to input their last name and grade to see if they made the dean list or honor roll. Program ends with a name of "ZZZ"
# Student_name will be a string that contains the current students last name
# grade will contain the students grade as a float

# a loop that will continue until a break statement occurs
while (1):

    # Get the student name and check for sentinal value
    student_name = input("Please enter your last name : ")
    if (student_name == "ZZZ"):
        break

    # get grade and check that it is an integer
    grade = input("Please enter your grade : ")
    try:
        grade = float(grade)
        if (grade >= 3.5):
            print("You have made it on the Dean List!")

        if (grade >= 3.25):
            print("You have made Honor Roll!")
        else:
            print("Maybe next time buddy :(")
    except:
        print("That was not a valid input, Please enter the next student...")

print("Program ended")
