#!/usr/bin/python3
import sys

sum = 0
matches = []

for line in sys.stdin:
    g = line.split(':')
    game = int(g[0].split(' ')[-1])
    nums = g[1].strip().replace('  ', ' ').split('|')
    wins = nums[0].strip().split(' ')
    count = 0
    guesses = nums[1].strip().split(' ')
#    print(f"{game}: {wins} | {guesses}")
    for i in guesses:
        if i in wins:
#            print(f"{i}")
            count += 1  # increase number of matches
    matches.append(count)

#print(matches)

# now we process the cards in order
scratchcards = {}

# in reality we renumber the cards to one less than the card number,
# but in this case we don't care.
for i in range(len(matches)):
    scratchcards[i] = 1         # set the initial cards
for i in range(len(matches)):
    count = matches[i]          # number of wins for this card
    num_insts = scratchcards[i] # number of instances of this card
#    print(f"Card {i+1}: {num_insts} instances, {count} wins")
    for n in range(num_insts):
        for c in range(count):
            scratchcards[i+c+1] += 1

for i in range(len(matches)):
    sum += scratchcards[i]
print(f"{sum}")

