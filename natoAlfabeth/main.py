import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(data.to_dict())

phonetic_dicc = {row.letter:row.code for (index, row) in data.iterrows()}
# print(phonetic_dicc)

word = input("Type your name ").upper()

code = [phonetic_dicc[letter] for letter in word]
print(code)