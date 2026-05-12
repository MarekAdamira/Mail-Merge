#TODO: Create a letter using starting_letter.txt
#nacte soubor starting_letter, ktery pak precteme
with open("./Input/Letters/starting_letter.txt", "r") as starting_letter:
    starting_letter = starting_letter.read()


#nacte invited_names a diky readlines() to bude číst po řádcích
    with open("./Input/Names/invited_names.txt", "r") as invited_names:
        invited_names = invited_names.readlines()

# ted ti vezme kazdé jmeno v invited names, očistí ho od mezer, otevre s tím jménem soubor v nové ceste a vlož tam text
# kde pomoci .replace vymění jména a pak je zapíše
        for name in invited_names:
            clear_name = name.strip()
            with open(f"./Output/ReadyToSend/{clear_name}.txt", "w") as ready_to_send:
                personal_letter = starting_letter.replace("[name]", clear_name)
                ready_to_send.write(personal_letter)










#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp