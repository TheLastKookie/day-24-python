# Creating Birthday Invites for Team Avatar aka The Gaang
with open("./Input/Names/invited_names.txt") as invited_names:
    invited_names_list = invited_names.readlines()

final_invites = [name.strip() for name in invited_names_list]

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    for name in final_invites:
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as final_letter:
            for line in starting_letter:
                final_letter.write(line.replace("[name]", f"{name}"))
            starting_letter.seek(0)
