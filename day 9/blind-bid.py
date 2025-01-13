bids = {}

print('Welcome to the bidding system!')
name = input("What's your name? \n")
bid = int(input("Ok! Good. So, how much are you bidding? \n"))

bids[name] = bid
keep_bidding = input("Is anyone else going to bid? Type yes or no!\n").lower()
go_on = True

while go_on:
    print("\n" * 100)

    if keep_bidding == 'yes':
        name = input("What's your name? \n")
        bid = int(input("Ok! Good. So, how much are you bidding? \n"))
        bids[name] = bid
        keep_bidding = input("Is anyone else going to bid? Type yes or no!\n").lower()
    elif keep_bidding == 'no':
        print('Ok! Going on.')
        go_on = False
    else:
        print('Please type yes or no.')

maximum_bid = 0
winner = ''
for bid in bids:

    if bids[bid] > maximum_bid:
        maximum_bid = bids[bid]
        winner = next((k for k, v in bids.items() if v == maximum_bid), None)
if winner is not None:
    print(f'The winner was {winner} with their ${maximum_bid} bid! Congrats.')

