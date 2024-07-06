import random as rd

words = "maman datascience competences voyage changement restaurant musee exposition"
words_list = words.split()
random_number = rd.randint(0, len(words_list) - 1)
secret_word = words_list[random_number]

game = {
    "secret_word": secret_word,
    "guess_word": "_ " * len(secret_word),
    "nb_life": 10
}

print(f"Lenght of the word : {len(game['secret_word'])}")
print(f"{game['guess_word']} - Life : {game['nb_life']}")


print("Bienvenu dans le jeu du pendu")
print("pour arrêter le jeu : soit vous gagnez soit vous écrivez 'stop'")

while True:
    mot = input(" ? > ")
    if mot == "stop":
        break