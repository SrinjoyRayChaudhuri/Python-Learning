myDict = {
    "fast":"In a quick manner",
    "Srinjoy":"A learner",
    "Marks":["98,78,86"],
    "anotherdict":{'harry':'Player'}
}
print(myDict['fast'])
print(myDict['Srinjoy'])
print(myDict['Marks'])
print(myDict['anotherdict']['harry'])
print(myDict.get("Srinjoy5"))#does not throes a error a error as Srinjoy5 is noit present in the dictionary
print(myDict['Srinjoy5'])#throws a error