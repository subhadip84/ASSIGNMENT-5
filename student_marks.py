# Dictionary of Student Marks
student_name = {'John':47,'Alice':85,'Dolly':78,'Mike':40,'Allen':71}

# checking the desired output
chek = input("Enter the student's name: ")
if chek in student_name:
    value = student_name[chek]
    print(f"{chek}'s marks: {value}")
else:
    print("Student Not Found.")




