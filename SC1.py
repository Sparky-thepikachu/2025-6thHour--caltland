#Name: Connor Altland
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#It is up to you to decide what properties are important and the theme of the game.

Enemys = {
    "Goomba": {
        "Health" : 1,
        "Damage" : 1,
        "Move" : ("Tackle"),
},
    "Fire Bro" : {
        "Health" : 7,
        "Damage" : 3,
        "Move" : ("Shoot fire balls"),
},
    "Bomb omb" : {
        "Health" : 11,
        "Damage" : 8,
        "Move" : ("Blow up"),
},
    "Spike" : {
        "Health" : 32,
        "Damage" : 6 ,
        "Move" : ("fire spike balls"),
    },
    "Bowser" :{
        "Health" : 100,
        "Damage" : 30,
        "Move" : ("fire breath, spin on shell,and mega punch")
    }
      }

Enemys["Goomba"]["Damage"] = int(input("How much damage do you have?"))
print(Enemys["Goomba"])

Enemys["Fire Bro"]["Damage"] = int(input("How much damage do you have?"))
print(Enemys["Fire Bro"])

Enemys["Bomb omb"]["Damage"] = int(input("How much damage do you have?"))
print(Enemys["Bomb omb"])

Enemys["Spike"]["Damage"] = int(input("How much damage do you have?"))
print(Enemys["Spike"])

Enemys["Bowser"]["Damage"] = int(input("How much damage do you have?"))
print(Enemys["Bowser"])