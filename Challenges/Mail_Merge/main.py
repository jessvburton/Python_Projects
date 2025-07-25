# my solution
PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt", "r") as invited_names:
    for line in invited_names:
        name = line.strip("\n")

        with open("Input/Letters/starting_letter.txt", "r") as f:
            starting_letter = f.read()

            print(f"Writing letter for {name}")
            with open(f"Output/ReadyToSend/letter_to_{name}.txt", "w") as output:
                output.write(starting_letter.replace(PLACEHOLDER, name))


## course solution
# PLACEHOLDER = "[name]"
#
# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()
#
# with open("./Input/Letters/starting_letter.txt") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
#             completed_letter.write(new_letter)
