import mysql.connector

def ticket_booking(cursor):
    while True:
        try:
            nm = input("ENTER YOUR NAME: ")
            phno = input("ENTER YOUR PHONE NUMBER: ")
            age = int(input("ENTER YOUR AGE: "))
            print("M=MALE,\nF=FEMALE,\nN=NOT SPECIFIED")
            gender = input("ENTER YOUR GENDER: ").upper()
            fr = input("ENTER YOUR DEPARTURE LOCATION: ")
            to = input("ENTER YOUR DESTINATION: ")
            date = input("ENTER THE DATE OF JOURNEY (YYYY-MM-DD): ")

            gender_map = {"M": "MALE", "F": "FEMALE", "N": "NOT SPECIFIED"}
            v = gender_map.get(gender, "NOT SPECIFIED")

            sl = "INSERT INTO railway(name, phno, age, gender, from_f, to_t, date_d) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (nm, phno, age, v, fr, to, date)
            cursor.execute(sl, val)
            print("✅ YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY".center(100))
            break

        except mysql.connector.Error as e:
            print(f"⚠️ Database Error: {e}")
            print("Please re-enter the values.\n")
            break
        except ValueError:
            print("❌ Age must be a number. Try again.\n")
            break


def ticket_checking(cursor):
    phno=input("ENTER YOUR PHONE NUMBER: ")
    sl=("select * from railway where phno=%s")
    cursor.execute(sl,(phno,))
    data=cursor.fetchone()

    if data:
        print("YOUR TICKET DETAILS ARE AS FOLLOWS:".center(100))
        print("NAME: ", data[0])
        print("PHONE NUMBER: ", data[1])
        print("AGE: ", data[2])
        print("GENDER: ", data[3])
        print("DEPARTURE LOCATION: ", data[4])
        print("DESTINATION: ", data[5])
        print("DATE OF JOURNEY: ", data[6])
    else:
        print("NO TICKET FOUND FOR THIS PHONE NUMBER".center(100))


def ticket_cancelling(cursor):
    phno=input("ENTER YOUR PHONE NUMBER: ")
    sl=("delete from railway where phno=%s")
    cursor.execute(sl,(phno,))
    if cursor.rowcount > 0:
        print("YOUR TICKET HAS BEEN CANCELLED SUCCESSFULLY".center(100))
    else:
        print("NO TICKET FOUND FOR THIS PHONE NUMBER".center(100))
