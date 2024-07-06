import random as rd

words = "maman datascience competences voyage changement restaurant musee exposition"
words_list = words.split()
random_number = rd.randint(0, len(words_list) - 1)
secret_word = words_list[random_number]

game = {
    "secret_word": secret_word,
    "guess_word": "." * len(secret_word),
    "nb_life": 10
}

print(f"Lenght of the word : {len(game['secret_word'])}")
print(f"{game['guess_word']} - Life : {game['nb_life']}")


print("Bienvenu dans le jeu du pendu")

while True:
    letter = input(" ? > ")
    if letter in game["secret_word"] and letter not in game["guess_word"]:
        guess_word_list = list(game["guess_word"])
        for index, current_letter in enumerate(game["secret_word"]):
            if current_letter == letter:    
                guess_word_list[index] = current_letter
        game["guess_word"] = "".join(guess_word_list)          
    elif letter not in game["secret_word"]:
        game["nb_life"] -= 1
    print(f"{game['guess_word']} - Life : {game['nb_life']}")
    
    if "." not in game["guess_word"]:
        print("You win!")
        break
    elif game["nb_life"] < 1:
        print("You loose!")
        break