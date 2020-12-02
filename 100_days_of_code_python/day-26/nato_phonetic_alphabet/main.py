import pandas

def nato_phonetic_alphabet():
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    input_user =input("Enter name : ").upper()
    temp = {row.letter:row.code for (index,row) in data.iterrows()}
    new_list = [temp[k] for k in input_user]
    print(new_list)
nato_phonetic_alphabet()