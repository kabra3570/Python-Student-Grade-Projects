import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Hello, proctor! Your students have recently finished taking an exam.")
print("In this program you shall enter the quiz results of your students, ")
print("and a graph shall appear showing you the results visually.")

grades = []
student_names = []
exam_subject = input("To start, enter the subject of the exam: ")
print("Next, enter in the exam grades, one by one.")
print("How many exam grades do you have to enter? ")
num = int(input())

counter = 0
while (counter < num):
    user_input = float(input("Enter exam grade " + str(counter + 1) + ": "))
    grades.append(user_input)
    counter += 1


print("Next, enter the names of the " + str(num) + " students ")
print("in the same order you entered in their exam grades.")
print()

counter = 0
while (counter != len(grades)) :
    user_input = input("Enter student " + str(counter + 1) + "\'s name: ")
    student_names.append(user_input)
    counter += 1


# first create a data frame using a dictionary
# the keys in the dictionary represent the column names in the DataFrame
# the value corresponding to each key within the dictionary should be a list
# which shall correspond to each Series within the DataFrame

# if using a dictionary to create a DataFrame, you must supply the row labels
# of the dataFrame by using the index attribute of the DataFrame

# the two ways to create a dataframe are from a dictionary and from a csv file

letter = []


for s in student_names :
    if s == ' ' :
        del(s)

for grade in grades :
    if grade >= 90 :
        letter.append("A")
    elif grade >= 80 :
        letter.append("B")
    elif grade >= 70 :
        letter.append("C")
    elif grade >= 60 :
        letter.append("D")
    else :
        letter.append("F")

exam = {"Exam 1 Grades": grades, "Letter Grade": letter}
exam_data_frame = pd.DataFrame(exam)
exam_data_frame.index = student_names

print(exam_data_frame)

# second create a histogram and show it to the user

plt.hist(exam_data_frame['Exam 1 Grades'], bins=2)
plt.title("Student Grades for the " + exam_subject + " exam")
plt.xlabel("Grade as a percentage")
plt.ylabel("Count (number of students)")

plt.show()
plt.clf()

print("Thank you for using this data to view information about your students' ")
print(" test grades. Press enter to exit/close the program.")

exit = input()
