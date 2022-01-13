                                                  #ASSIGNMENT 1 

#PROGRAM 1
#Finding The Average of 3 Numbers

number_1=int(input("enter number1:"))
number_2=int(input("enter number2:"))
number_3=int(input("enter number3:"))

Average=(number_1+number_2+number_3)/3
print("Average of 3 numbers=",Average)


#PROGRAM 2
#Finding a person's income tax
#All the values are in $s

gross_income=input("Enter the gross income:")
gross_income=float(gross_income)
standard_deduction=10000
dependents=int(input("Enter the no. of dependents:"))
#There is a deduction of $3000 for each dependent
dependent_deduction=3000

taxable_income=gross_income-standard_deduction-(dependents*dependent_deduction)
print("Taxable Income:", taxable_income)
#Tax Rate=20%
tax=(taxable_income*20)/100
print("Tax:", tax)



#PROGRAM 3
#Making a list of NAME,SID,GENDER COURSE NAME,CGPA

name=input("Enter your Name:")
sid=int(input("Enter student id:"))
gender=input("Enter your gender:")
course_name=input("Enter your Course name:")
cgpa=float(input("Enter your cgpa:"))
#Name of our list:Student_info
data=['Name','SID','Gender','Course name','CGPA']
print("Data:",data)
student_info=[name,sid,gender,course_name,cgpa]
print("Student_Info:",student_info)


#PROGRAM 4
#Make a list of marks of 5 students and arrange in a sorted manner

student_1marks=int(input("Enter student 1 marks:"))
student_2marks=int(input("Enter student 2 marks:"))
student_3marks=int(input("Enter student 3 marks:"))
student_4marks=int(input("Enter student 4 marks:"))
student_5marks=int(input("Enter student 5 marks:"))
#list of marks of students
list_marks=[student_1marks,student_2marks,student_3marks,student_4marks,student_5marks]
print("Marks list:",list_marks)
list_marks.sort()
list_marks.reverse()
print("Marks list:",list_marks)




#PROGRAM 5
#Making a list of colours

#(a)Removing a colour from a list 
colour=['Red','Green','White','Black','Pink','Yellow']
print("Colour:",colour)
#Removing Black colour of index 3
colour.pop(3)
print("Colour:",colour)

#(b)Removing a colour and inserting a new colour
colour=['Red','Green','White','Black','Pink','Yellow']
print("Colour:",colour)
#Replacing Black and Pink with Purple
colour[3:5]=['Purple']
print("New colour list:",colour)







 

