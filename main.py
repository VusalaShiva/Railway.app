from database import get_connection, setup_database
from user import signin, signup

def start():
    mycon = get_connection()
    cursor = mycon.cursor()
    mycon.autocommit = True
    setup_database(cursor)

    print("Welcome to Railway Reservation System".center(100))
    while True:
        print("\t\t\t-------------------------------------------------------------------------------------------")
        print('\t\t\t\t\t1. SIGN IN')
        print('\t\t\t\t\t2. SIGN UP')
        print('\t\t\t\t\t3. EXIT')
        print("\t\t\t-------------------------------------------------------------------------------------------")
        ch = input("\t\t\t\tEnter your choice: ")
        if ch == "1":
            signin(cursor)
        elif ch == "2":
            signup(cursor)
        elif ch == "3":
            print("Exiting... Thank you for using the system!".center(100))
            break
        elif ch =="":
            pass
        else:
            print("Invalid choice. Please try again.".center(100))

if __name__ == "__main__":
    start()

