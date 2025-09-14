from ticket import ticket_booking, ticket_checking, ticket_cancelling

def display(cursor):
    a = input("ENTER YOUR USERNAME: ")
    b = input("ENTER YOUR PASSWORD: ")
    sl = "SELECT fname, lname, phno, gender, dob, age FROM user_accounts WHERE user_name=%s AND password=%s"
    cursor.execute(sl, (a, b))
    data = cursor.fetchone()
    
    if data:
        print("YOUR ACCOUNT DETAILS ARE AS FOLLOWS:".center(100))
        print("FIRST NAME: ", data[0])
        print("LAST NAME: ", data[1])
        print("PHONE NUMBER: ", data[2])
        print("GENDER: ", data[3])
        print("DATE OF BIRTH: ", data[4])
        print("AGE: ", data[5])
    else:
        print("ACCOUNT DOES NOT EXIST or WRONG CREDENTIALS".center(100))


def signin(cursor):
    a=input("ENTER YOUR USERNAME: ")
    b=input("ENTER YOUR PASSWORD: ")
    sl="select user_name from user_accounts where user_name=%s and password=%s"
    cursor.execute(sl,(a,b))
    data=cursor.fetchone()
    if data and data[0]==a:
        print("Login successful!".center(100))
        main(cursor)
    else:
        print("ACCOUNT DOES NOT EXIST or WRONG CREDENTIALS".center(100))


import mysql.connector

def signup(cursor):
    while True:
        try:
            f = input("ENTER YOUR FIRST NAME: ")
            l = input("ENTER YOUR LAST NAME: ")
            a = input("ENTER YOUR USERNAME: ")
            b = input("ENTER YOUR PASSWORD: ")
            c = input("CONFIRM YOUR PASSWORD: ")
            ph = input("ENTER YOUR PHONE NUMBER: ")
            print("M=MALE,\nF=FEMALE,\nN=NOT SPECIFIED")
            gender = input("ENTER YOUR GENDER: ").upper()
            dob = input("ENTER YOUR DATE OF BIRTH (YYYY-MM-DD): ")
            age = int(input("ENTER YOUR AGE: "))
            
            gender_map = {"M": "MALE", "F": "FEMALE", "N": "NOT SPECIFIED"}
            gen = gender_map.get(gender, "NOT SPECIFIED")

            if b != c:
                print("❌ Passwords do not match. Try again.\n")
                continue

            sl = """INSERT INTO user_accounts(fname, lname, user_name, password, phno, gender, dob, age) 
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
            val = (f, l, a, b, ph, gen, dob, age)
            cursor.execute(sl, val)
            print("✅ ACCOUNT CREATED SUCCESSFULLY".center(100))
            break

        except mysql.connector.Error as e:
            print(f"⚠️ Database Error: {e}")
            print("Please re-enter values.\n")
            break
        except ValueError:
            print("❌ Age must be a valid number.\n")
            break


def main(cursor):
    while True:
        print("\t\t\t-------------------------------------------------------------------------------------------")
        print('\t\t\t\t\t1. TICKET BOOKING')
        print('\t\t\t\t\t2. TICKET CHECKING')
        print('\t\t\t\t\t3. TICKET CANCELLING')
        print('\t\t\t\t\t4. ACCOUNT PROFILE')
        print('\t\t\t\t\t5. LOG OUT')
        print("\t\t\t-------------------------------------------------------------------------------------------")
        ch = input("\t\t\t\tENTER YOUR CHOICE: ")
        if ch == "1":
            ticket_booking(cursor)
        elif ch == "2":
            ticket_checking(cursor)
        elif ch == "3":
            ticket_cancelling(cursor)
        elif ch == "4":
            display(cursor)
        elif ch == "5":
            print("LOGGING OUT...".center(100))
            break
        elif ch == "":
            pass
        else:
            print("INVALID CHOICE. PLEASE TRY AGAIN.".center(100))
