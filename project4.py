# entering data in csv file
import csv

def write_csv(info_added): # w+ - write mode # name of file # for new line # a- append mode
    
    with open('student_info.csv', 'a',newline='')as csv_file: # variable holding file object
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0: # to check whether file is empty or not
            writer.writerow(["First_name", "Last_name", "Class", "Age", "Mobile_no", "E-mail"])
        
        writer.writerow(info_added)


if __name__ == '__main__':
    # input
    condition = True
    student_num = 1

    while (condition):
        print('Entered Student #{} info: '.format(student_num))
        stu_firstname = input('First Name: ')
        stu_lastname = input('Last Name: ')
        stu_class = input('Class: ')
        stu_age = input('Age: ')
        stu_mob = input('Mobile No.: ')
        stu_mail = input('E-mail: ')

        # entered info
        print('\nEntered info: ')
        print("First Name: " + stu_firstname)
        print("Last Name: " + stu_lastname)
        print("Class: " + stu_class)
        print("Age: " + stu_age)
        print("Mobile No.: " + stu_mob)
        print("E-mail: " + stu_mail)

        # entering the  data in a single string
        ent_info = stu_firstname +" " +  stu_lastname + " " + stu_class + " "  + stu_age + " "  + stu_mob + " "  + stu_mail

        #split to create list
        entered_info = ent_info.split(' ')
        # print(entered_info)

        choice = input('\nIs the entered info is correct ? (yes/no) : ')

        if choice == 'yes' or choice == 'YES':
            # function call - add info
            write_csv(entered_info)

            addstu = input('Do you want to add new student info ? Type - yes/no: ')
            if addstu == 'yes' or addstu == 'YES':
                condition = True
                student_num = student_num + 1

            elif addstu == 'no' or addstu == 'NO':
                condition = False
            else:
                print('Please enter a valid info !!')
        
        elif choice == 'no' or choice == 'NO':
            print('Please re-enter the values!!')
        
        else:
            print('Please enter the correct value!!')