###FUNCTIONS###
#jeu de black jack
import random
points_actuels = 0
points_actuels_croupier = 0
message = "voulez vous tirez une autre carte ? (1:oui/2:non)"
mise = 0
total = 0
i = 0
bjack = False

#Fonction de pioche, d'un tour du jeu
def carte():
    global points_actuels, i, limite_depassé, bjack
    carte_possible = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
    nbrcarte_depart = random.randint(0, 11)
    if nbrcarte_depart == 8:
        carte_depart = "un valet !"
        points_actuels += 10
    elif nbrcarte_depart == 9:
        carte_depart = "une dame !"
        points_actuels += 10
    elif nbrcarte_depart == 10:
        carte_depart = "un roi !"
        points_actuels += 10
    elif nbrcarte_depart == 11:
        carte_depart = "un AS"
        points_actuels += 11
    else :
        carte_depart = f"un {carte_possible[nbrcarte_depart]}"
        points_actuels += carte_possible[nbrcarte_depart]
    print("------------------------")
    print ("Vous avez obtenue", carte_depart)
    print ("Vos points actuels :", points_actuels, "points.")
    print("                    ")

#fonction de tour du croupier
def carte_croupier():
    global carte_depart_croupier
    global points_actuels_croupier
    carte_possible = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
    nbrcarte_depart_croupier = random.randint(0, 11)
    if nbrcarte_depart_croupier == 8:
        carte_depart_croupier = "un valet !"
        points_actuels_croupier += 10
    elif nbrcarte_depart_croupier == 9:
        carte_depart_croupier = "une dame !"
        points_actuels_croupier += 10
    elif nbrcarte_depart_croupier == 10:
        carte_depart_croupier = "un roi !"
        points_actuels_croupier += 10
    elif nbrcarte_depart_croupier == 11:
        carte_depart_croupier = "un AS"
        points_actuels_croupier += 11
    else :
        carte_depart_croupier = f"un {carte_possible[nbrcarte_depart_croupier]}"
        points_actuels_croupier += carte_possible[nbrcarte_depart_croupier]
    print("------------------------")
    print (f"Le croupier a obtenu {carte_depart_croupier}")
    print("Le croupier totalise donc", points_actuels_croupier, "points.")
    print("                    ")

#fonction de blackjack
def blackjack():
    total = (mise * 1.5)+ mise
    print("------------------------")
    print ("BLACK JACK !!!")
    print("Bravo", username, "vous avez gagné !")
    print("                        ")
    print("Vous remporté 1.5 fois votre mis de", mise, "$ !")
    print("Cela vous fait un total de", total, "$ !")
    print("                    ")
    print ("Merci d'avoir joué", username, "à bientôt !")
    print("------------------------")
    exit()  

def blackjack_croupier():
    total = 0
    print("------------------------")
    print ("Le croupier a obtenue un BLACK JACK !!!")
    print("Dommage", username, "vous avez été battus !")
    print("                        ")
    print("Vous perdez votre mise de", mise, "$ !")
    print("Cela vous fait un total de", total, "$.")
    print("                    ")
    print ("Merci d'avoir joué", username, "à bientôt !")
    print("------------------------")
    exit()  

def fin_partie():
    global total
    if points_actuels == 21:
        blackjack()
    elif points_actuels < 21:
        #croupier pioche tant que il n'as pas au - 17
        while points_actuels_croupier < 17:
            carte_croupier()
        #si croupier depasse, user gagne sa mise
        if points_actuels_croupier > 21:
            total = mise*2
            print("------------------------")
            print("Vous avez donc gagné !! Car le croupier a dépasser la limite, bravo !")
            print ("Le croupier a dépassé la limite ! Il totalise", points_actuels_croupier, "points !")
            print("                    ")
            print("Vous gagné votre mise soit", mise, "$ !")
            print("Vous avez maintenant", total, "$ au total.")
            print("                    ")
            print("Vous terminez a", points_actuels, "points !")
            print("                    ")
            print ("Merci d'avoir joué", username, "à bientôt !")
            print("------------------------")
            exit()
        #Sinon si le croupier est dans les points comme user
        else:
            #si le user a plus de points que le croupier
            if points_actuels_croupier < points_actuels:
                total += mise*2
                print("------------------------")
                print("Vous avez gagné !! Vous avez fait mieux que le croupier sans dépasser la limite, bravo !")
                print("                    ")
                print("Vous gagné votre mise soit", mise, "$ !")
                print("Vous avez maintenant", total, "$ au total.")
                print("                    ")
                print("Vous terminez a", points_actuels, "points !")
                print ("Merci d'avoir joué", username, "à bientôt !")
                print("------------------------")
                exit()
            #si le croupier et le user sont a égalités
            if points_actuels_croupier == points_actuels:
                total = mise
                print("------------------------")
                print("Egalitée ! Dommage vous et le croupier avez fait le meme score.")
                print("                    ")
                print("Vous recupéré votre mise de", total, "$")
                print("                    ")
                print("Vous et le croupiez avez terminez a", points_actuels, "points !")
                print ("Merci d'avoir joué", username, "à bientôt !")
                print("------------------------")
                exit()
            #sinon, si le croupier a plus de points que le user
            else:
                total = 0
                print("------------------------")
                print("Dommage ! Vous n'avez pas réussi a battre le croupier !")
                print("                    ")
                print("Vous perdez votre mise soit", mise, "$.")
                print("Vous posser maintenant", total, "$ au total.")
                print("                    ")
                print("Vous avez tout de meme su rester en dessous de la limite, bravo !")
                print("Vous terminez a", points_actuels, "points !")
                print("                    ")
                print ("Merci d'avoir joué", username, "à bientôt !")
                print("------------------------")
                exit() 
    else:
        total = 0
        print ("----------------------")
        print("Dommage ! Vous avez dépassé la limite...")
        print("Vous perdez votre mis de", mise, "$")
        print("Merci d'avoir joué", username, "à bientot !")
        print ("----------------------")
        exit()

def tour():
    if points_actuels == 21:
        blackjack()
    elif points_actuels < 21:
            carte()
            if points_actuels == 21:
                blackjack()
            elif points_actuels < 21:
                if points_actuels_croupier < 17:
                    carte_croupier()
            else:
                total = 0
                print ("----------------------")
                print("Dommage ! Vous avez dépassé la limite...")
                print("Vous perdez votre mis de", mise, "$")
                print("Merci d'avoir joué", username, "à bientot !")
                print ("----------------------")
                exit()
    else :
        print ("----------------------")
        print("Dommage ! Vous avez dépassé la limite...")
        print("Vous perdez votre mis de", mise, "$")
        print("Merci d'avoir joué", username, "à bientot !")
        print ("----------------------")
        exit()








###MAIN ALGO###
#Logique de la partie
print("------------------------")
username = input("Entrer votre nom d'utilisateur")
mise = int(input("Entrer votre mise"))
print("------------------------")
print ("Bienvenue sur mon jeux de Black Jack", username, "!")
carte()
carte_croupier()
reponse = int(input(message))
while reponse == 1:
    tour()
    reponse = int(input(message))
    if points_actuels_croupier > 21:
        fin_partie()
    elif points_actuels_croupier == 21:
        blackjack_croupier()
fin_partie()


