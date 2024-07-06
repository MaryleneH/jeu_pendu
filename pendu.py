import random as rd


print("Bienvenu dans le jeu du pendu")
in_game = True
while in_game:

    words = "maman datascience competences voyage changement restaurant musee exposition ambition trahison pardon"
    words_list = words.split()
    random_number = rd.randint(0, len(words_list) - 1)
    secret_word = words_list[random_number]

    game = {
        "secret_word": secret_word,
        "guess_word": "_ " * len(secret_word),
        "nb_life": 10,
        "tried_letters": set()
    }

    print(f""" 
        =================================
        Lenght of the word : {len(game['secret_word'])}
          =====================================
          """)
    print(f"""
        ======================================
        Guess that word : {game['guess_word']} - Life : {game['nb_life']}
        =====================================
        """)

    while True:
        letter = input(" Enter a letter > ")
        if letter.isalpha() and len(letter) == 1 :
            game["tried_letters"].add(letter)
            if letter in game["secret_word"] and letter not in game["guess_word"]:
                guess_word_list = list(game["guess_word"])
                for index, current_letter in enumerate(game["secret_word"]):
                    if current_letter == letter:    
                        guess_word_list[2 * index] = current_letter
                    game["guess_word"] = "".join(guess_word_list)          
            elif letter not in game["secret_word"]:
                game["nb_life"] -= 1
            print(f"""
                ------------------------------------------
                {game['guess_word']} - Life : {game['nb_life']}
                You've tried : {game['tried_letters']}
                ------------------------------------------
                """)
    
            if "_" not in game["guess_word"]:
                guess_word_str = str(game["guess_word"])
                guess_word_str = guess_word_str.replace(" ","")
                print(f"""
                    ------------------
                    You win!
                    ------------------
                    The word was : {guess_word_str}
                    ------------------
                    """)
                replay = input(" Play again ? (Y/y) : ")
                if replay not in ['Y','y']:
                    in_game = False
                break
            elif game["nb_life"] < 1:
                print(f"""
                    --------------
                    You loose!
                    --------------
                  
                    """)
                replay = input(" Play again ? (Y/y : ")
                if replay not in ['Y','y']:
                    in_game = False            
                break