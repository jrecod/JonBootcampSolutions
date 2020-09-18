# LCR is a dice game, one of pure chance. Therefore, we can write a simulator to avoid wasting the time playing it ourselves.

# Each player begins with 3 chips. Players take turns rolling three six-sided dice, each of which is marked with "L", "C", "R" on one side, and a single dot on the three remaining sides. For each "L" or "R" thrown, the player must pass one chip to the player to their left or right, respectively. A "C" indicates a chip to the center (pot). A dot has no effect.

# If a player has fewer than three chips left, they're still in the game but their number of chips is the number of dice they roll on their turn, rather than rolling all three. When a player has zero chips, they pass the dice on their turn, but may receive chips from others and take their next turn accordingly. The winner is the last player with chips left, and wins the center pot.

# When the program starts, it should ask for the names of the players, until the user enters 'done'. Then it should run the simulation, tell the user who won, and ask the player whether they'd like to play again. We can represent the players as a list of dictionaries with each dictionary containing two key-value pairs: player's name and the number of chips they have, e.g. {'name': 'Billy', 'chips': 3}.

import random

def player_rolls(player):
    if player['chips'] > 2:
        return 3
    else:
        return player['chips']

def check_winner(playerlist, pot):
    #loop over list of players
    for player in playerlist:
    #if any players chips + pot is equals 3 times the number of players, they won
        if player['chips'] + pot == 3*len(playerlist):
            return player
    #if we get through all the players and none return, return 'none'
    return None

    # output = None
    # for player in playerlist:
    #     if player['chips'] > 0:
    #         if output is None:
    #             output = player
    #         else:
    #             return None
    # return output


    # found_player = False
    # for player in playerlist:
    #     if player['chips'] > 0:
    #         if found_player:
    #             return False
    #         found_player = True
    # return found_player


# print(check_winner([{'name': 'Bill', 'chips': 3}, {'name': 'Larry', 'chips': 3}, {'name': 'Bob', 'chips': 3}],0))
# print(check_winner([{'name': 'Bill', 'chips': 4}, {'name': 'Larry', 'chips': 0}, {'name': 'Bob', 'chips': 0}],5))
# exit()

#Get players
playername = ''
playerlist = []

while True:
    playername = input('What is the player name? Type done when there are no more players: ')
    if playername == 'done':
        break
    playerlist.append({'name' : playername, 'chips' : 3})
print(playerlist)

# Game Loop
dice_roll = ['L', 'R', 'C', 'dot', 'dot', 'dot']
pot = 0
currrent_player_index = 0
while True:
    # find the number of dice rolls from players chip count
    num_player_rolls = player_rolls(playerlist[currrent_player_index])
    # Roll the dice that many times
    for i in range(num_player_rolls):
        current_roll = random.choice(dice_roll)
        # if die rolls an 'L' move a chip to the player on the left
        if current_roll == 'L':
            if currrent_player_index == 0:
                playerlist[len(playerlist)-1]['chips'] += 1
            else:
                playerlist[currrent_player_index-1]['chips'] += 1
            playerlist[currrent_player_index]['chips'] -= 1
        # if die rolls an 'R' move a chip to the player on the right
        elif current_roll == 'R':
            if currrent_player_index == len(playerlist)-1:
                playerlist[0]['chips'] += 1
            else:
                playerlist[currrent_player_index + 1]['chips'] += 1
            playerlist[currrent_player_index]['chips'] -= 1
        # if die rolls a 'C' move a chip to the center pot
        elif current_roll == 'C':
            pot += 1
            playerlist[currrent_player_index]['chips'] -= 1
        # if die rolls a dot do nothing
        print(current_roll, playerlist, pot)

        
    # check and see if a player has won
    winner = check_winner(playerlist, pot)
    if winner is not None:
        winner['chips'] += pot
        print(winner['name']+ ' won with ' + str(winner['chips'])+ ' chips.')
        break
    currrent_player_index += 1
    #currrent_player_index %= len(playerlist) 
    if currrent_player_index == len(playerlist):
        currrent_player_index = 0
    

