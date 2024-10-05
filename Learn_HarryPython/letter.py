letter = '''Dear<|NAME|>
Yor are selected

Date<|DATE|>
'''
name=input("Enter your name\n")
date=input("Enter the date\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)

