import json
import difflib

def get_definition(*arg):
    for k in arg[1][arg[0].lower()]:
        print(f"->{k}")

def dictionary():
    data=json.load(open("data.json"))
    search_term=input("Please enter word : ")
    try:
        get_definition(search_term,data)
    except:
        sim = difflib.get_close_matches(search_term,data)
        if sim != []:
            choice=input(f"Did you mean {sim[0]} ?(Press y for yes or n to no)").lower()
            if (choice == 'y'):
                get_definition(sim[0],data)
            elif (choice == 'n'):
                print("Word not found not found")
            else:
                print("Choice invalid.Please re-enter word")
        else:
            print("Word not found not found")
dictionary()
