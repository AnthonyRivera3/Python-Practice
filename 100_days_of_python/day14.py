#higher lower game project
import random

#Function for getting a random game
def random_game_gen():
    list_of_games = list(games.keys())
    random_game = random.choice(list_of_games)
    return random_game


#Function to get the numbers
def purchases(game):
    purchases_num = games[game]
    return purchases_num
points = 0
games = {
"Call_of_duty":166000, 
"Battlefield" :234500,
"Minecraft"   :213123,
"Roblox"      :1200000,
"CSGO"        :124000,
"Valorant"    :90000
}


print("Welcome to higher-lower!")
print("In todays game we are going to guess what games have more purchases")
ans = input("Would you like to play? 'Y' or 'N'\n")
if ans == 'Y':
    print("Great lets begin!:\n")
    gamerun = 0
    while gamerun == 0:
        game1 = random_game_gen()
        game2 = random_game_gen()
        while game1 == game2:   
            game2 = random_game_gen()


        ans = input(f"Type 'A' for {game1} and Type 'B' for {game2}\n")
        gamenums1 = purchases(game1)
        gamenums2 = purchases(game2)
        if (gamenums1 > gamenums2 and ans ==  'A') or (gamenums1 < gamenums2 and ans ==  'B'):
            points+=1
            print(f"Congrats you get a point: {points}")
        else: 
            print(f"You lose! points: {points}")
            gamerun+=1
        
    

    








