import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

alpha_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(alpha_dict)

word = input("Enter a Word: ").upper()
output_list = [alpha_dict[letter] for letter in word]
print(output_list)