from user import User
from credential import UserCredential
def main():
    count = 0
    print ("do you have an account")
    print("y - Yes\nn - No")
    answer = input().lower()


    if answer =="n":
        print("Create an account\n")
        print("Enter your full name:")
        f_name = input()
        print("Enter prefered username:")
        user_name = input()
        print("Enter email:")
        email = input()
        print("Enter Phone No.:")
        phone = input()
        print("Enter password")
        pWord = input()
        credential = []


        newUser = create_user(f_name,user_name,email,phone,pWord,credential)

        print("\n")
        print("Please Login to continue...")
        print("Enter UserName:")
        user_name = input()
        print("Enter Password:")
        p_word = input()

        current_user = log_in(user_name,p_word)










   