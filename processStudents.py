''' 
*   Professor B would like to know which of his student have a GPA below 3.0.
    To accomplish this, read the file - students.csv into the program. The program
    should evaluate the GPA to see if it is higher or lower than 3.0. If it is,
    then it should be written out to the file - processedStudents.csv. (This file
    already contains headers and the headers should NOT be overwritten.) 

*   Create a dictionary of each student where the student ID is the key
    and the GPA is the value.

*  print out the dictionary

*  print out the corresponding GPA for student - 567890123

I have outlined comments for each step of the program. You are
not required to use them but it is provided to help you work
through the logic of the problem.


'''


import csv


# create a file object to open the file in read mode
infile = open('students.csv', 'r')


# create a csv object from the file object
students = csv.reader(infile, delimiter=',')

#skip the header row
next(students)

#create an outfile object for the pocessed record
outfile = open('processedStudents.csv', 'w')


#create a new dictionary named 'student_dict'
student_dict = {}

outfile.write('stud_id,firstname,lastname,major,classification,gpa\n')
#use a loop to iterate through each row of the file
for row in students:
    
    #check if the GPA is below 3.0. If so, write the record to the outfile
    if row[8] < '3.00':
       
        outfile.write(row[0] + ',' + row[1] + ',' + row[2] + ',' + row[3] + ',' + row[4] + ',' + row[5] + ',' + row[6] + ',' + row[7] + ',' + row[8] + '\n')
    


    # append the record to the dictionary with the student id as the Key
    # and the value as the GPA
    student_dict[row[0]] = row[8]





#print the entire dictionary
print()
print(student_dict)
print()

#Print the student id 
print('Student ID and GPA:')
#for key,value in student_dict.items():
 #   print(key)
  #  print(value)
   # print()
#print(student_dict['stud_id'])
#for key,value in student_dict['567890123']:
 #   print(key)
  #  print(value)
#print(student_dict[])

#print out the corresponding GPA from the dictionary
print(student_dict['567890123'])


#close the outfile
outfile.close()







