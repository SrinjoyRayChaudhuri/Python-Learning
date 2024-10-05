#Write a program to find out whether a given username has less than 10 characters or not
username=input("Enter the user name")
if len(username)>10:
    print("More than 10 characters")
else:
    print("Less than 10 chracters")