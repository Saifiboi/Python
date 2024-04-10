# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# names = []

with open("Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()
    for i in range(0, len(names)):
        names[i] = names[i].strip()
with open("Input/Letters/starting_letter.txt", mode="r") as f2:
    content = f2.read()

for i in names:
    new_content = content.replace("[name]", i)
    with open(f"Output/ReadyToSend/letter_to_{i}.txt", mode="w") as f3:
        f3.write(new_content)
