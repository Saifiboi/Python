# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# {"A": "Alfa", "B": "Bravo"}
import pandas

with open("nato_phonetic_alphabet.csv", mode="r") as file:
    panda_frame = pandas.read_csv(file)
    new_dict = {row.letter: row.code for (index, row) in panda_frame.iterrows()}
user_str = input("Please Enter a word.")
is_repeat = True
while is_repeat:
    try:
        new_list = [new_dict[alph.upper()] for alph in user_str]
    except KeyError:
        print("Please Enter Valid string:")
        user_str = input("Please Enter a word.")
        is_repeat = True
    else:
        is_repeat = False
print(new_list)
