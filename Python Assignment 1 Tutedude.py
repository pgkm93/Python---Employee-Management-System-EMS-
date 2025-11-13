# first assignment Tutedude
# Employee Management System (EMS)

p = print

emps = {}

def add_emp(emp_id ,emp_name,age,dep, salary):
    
    if emp_id in emps:
        p("Employee id is allready existing! Try again")
    
    else : 
         emps[emp_id] ={"Employee Name": emp_name,"Employee age":age ,"Employee department":dep,"Employee Salary":salary}
         p("Employee added successfully for test")
        
def view_emps():
    for emp_id in emps:
        p(f"Employee id:{emp_id}")
        p(f"Employee Name:{emps[emp_id]['Employee Name']}")
        p(f"Employee age:{emps[emp_id]['Employee age']}")
        p(f"Employee department:{emps[emp_id]['Employee department']}")
        p(f"Employee salary:{emps[emp_id]['Employee Salary']}")
        p("---------------")

def display_employee(emp_id):

    if emp_id in emps:
        p(f"Employee id:{emp_id}")
        p(f"Employee Name:{emps[emp_id]['Employee Name']}")
        p(f"Employee age:{emps[emp_id]['Employee age']}")
        p(f"Employee department:{emps[emp_id]['Employee department']}")
        p(f"Employee salary:{emps[emp_id]['Employee Salary']}")
        p("---------------")

    else:
        print("Employee not found")


add_emp(106,"A",23,"Manger",45000)
add_emp(107,"B",23,"Assistance",20000)
add_emp(108,"C",23,"A Team Head",30000)
add_emp(109,"D",23,"Article student",15000)


def add_Employee():
    add_emp( int(input("Enter Employee id:")),
            input("Enter Employee Name:"),
            int(input("Enter Employee age:")),
            input("Enter Employee department:"),
            int(input("Enter Employee Salary:")))
    return
    
def view_Employees():
    view_emps()
    return

def search_Employee():
    emp_id = int(input("Enter Employee id to search:"))
    display_employee(emp_id)
    return

def displya_menu():
    p("--------Welcome to the Preethan Employee Management System (EMS)----------")
    p("1.Add Employee")
    p("2.View All Employee")
    p("3.Search for Employee")
    p("4.Exit")

while(True):
    displya_menu()

    choice = int(input("choose the option:"))

    if choice == 1:
        p("you choose:",add_Employee())

    elif choice == 2:
           p("you choose:",view_emps())

    elif choice == 3:
         p("you choose:",search_Employee())


    elif choice == 4:
        p("exit")
        break

    else:
        p("*********choose the correct option********")
        p("---------------------------")