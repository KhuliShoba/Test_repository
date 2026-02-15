num_of_students  = int(input("How many students are registering: "))
with open ("reg_form.txt", "w") as output_file:
    for index in range (num_of_students):
        student_id = int(input(" Enter the student ID: "))
       
        print(student_id)
        output_file.write(f" {student_id} .....................\n")
