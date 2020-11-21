#get users cards
card_input = input("Enter your 3 cards seperated by a space ").upper()

#print player cards
card_list = card_input.split()
print("Your cards are ", card_list)

#get the sum
sum = 0
for card in card_list:
    if card == "A":
        card = 1
    elif card == "J" or card == "Q" or card == "K":
        card = 10
    sum += int(card)

#print sum and advice
if sum < 17:
    print("Hit! Your card total is ", sum)
elif sum < 21:
    print("Stay! Your card total is ", sum)
elif sum == 21:
    print("Blackjack! Your card total is ", sum)
else:
    print("Already Busted! Your car total is ", sum)
    