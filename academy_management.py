# file = open("text_file",'x')
def student_admission():
    name = input("Please enter the name of the student:  ")
    student_class = input("Please enter the student class:  ")
    phone_no = int(input("Please eneter the phone number of student:  "))
    address = input("Please enter the address of the student:  ")
    section = input("Please enter the section of student:  ")
    roll_no  = int(input("please enter the roll no of the student:  "))
    with open("text_file","a") as f:
        print(name, student_class,  phone_no,  address,  section,roll_no, file=f)
        f.close()
def student_record_view():
    with open("text_file","r") as f:
        print(f.read())
        f.close()

user_access = int(input("""Please tell which function you want to choose
1 for entering data
2 for view data\n"""))
if user_access==1:
    student_admission()
elif user_access==2:
    student_record_view()