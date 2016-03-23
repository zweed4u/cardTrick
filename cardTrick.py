import random
def define_cards():
	rank_string = ("Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King")
	suit_string = ("Clubs","Diamonds","Hearts","Spades")
	cards = []
    	for suit in range(4):
    		for rank in range(13):
            		card_string = rank_string[rank] + " of " + suit_string[suit]
           		cards.append(card_string)
    	return cards


def shuffle_deck(deck):
	random.shuffle(deck)
    	return

def deal_card(deck):
	return deck.pop(0)

deck=[]
deck = define_cards()
shuffle_deck(deck)

gameBase=[]
for i in range(27):
    	gameBase.append(deal_card(deck))

print '\nPick a card and remember it:'
#Makes a list of lists (each split respectively)
split=[gameBase[i:i+len(gameBase)/3] for i in range(0,len(gameBase),len(gameBase)/3)]
for row in zip(*split):
	print "".join(str.ljust(i,20) for i in row)
print '\n'
raw_input('Press ENTER to continue')



print 'Shuffling...'
shuffle_deck(gameBase)
pick=raw_input('What is your favorite number? (1-27) ')
#catch if invalid input
#       	 1   3   9
#*2= 	 2   6   18   = 26
#0=top 	1=middle       2=bottom
'''
j of diamonds 
12-1 = 11 
start with 1s 2 1s  0 3s  1 9s
bottom top middle
card is the var => pick pop
'''

def numDecomp(baseNum):
	global firstNum,secNum,lastNum
	baseNum=int(baseNum)-1
	lastNum=int(baseNum/9)
	numLeftAfter9=baseNum-(9*lastNum)

	secNum=numLeftAfter9/3
	numLeftAfter3=numLeftAfter9-(3*secNum)

	firstNum=int(numLeftAfter3/1)
	#Decision
	print firstNum,secNum,lastNum

numDecomp(pick)

print '\nWhich column is your card in?:'
split=[gameBase[i:i+len(gameBase)/3] for i in range(0,len(gameBase),len(gameBase)/3)]

for row in zip(*split):
	print "".join(str.ljust(i,20) for i in row)
print '\n'

firstColumn=raw_input('Column? (L,M,R) ')

if firstColumn=='L':
	placeColumn=split[0]
elif firstColumn=='M':
	placeColumn=split[1]
elif firstColumn=='R':
	placeColumn=split[2]
else:
	print 'pick correct params'

newHand=[]
split.remove(placeColumn)
if firstNum==0:
	#put placeColumn on top
	for card in placeColumn:
		newHand.append(card)
	for card in split[0]:
		newHand.append(card)
	for card in split[1]:
		newHand.append(card)
			

elif firstNum==1:
	#put placeColumn on middle
	for card in split[0]:
		newHand.append(card)
	for card in placeColumn:
		newHand.append(card)
	for card in split[1]:
		newHand.append(card)
	

else:
	#put place Column on bottom
	for card in split[0]:
		newHand.append(card)
	for card in split[1]:
		newHand.append(card)
	for card in placeColumn:
		newHand.append(card)

print newHand




'''
SECOND ROUND
'''
split=[newHand[::3],newHand[1::3],newHand[2::3]]

for row in zip(*split):
	print "".join(str.ljust(i,20) for i in row)
print '\n'

secColumn=raw_input('Column? (L,M,R) ')

if secColumn=='L':
	placeColumn=split[0]
elif secColumn=='M':
	placeColumn=split[1]
elif secColumn=='R':
	placeColumn=split[2]
else:
	print 'pick correct params'

newHand=[]
split.remove(placeColumn)
if secNum==0:
	#put placeColumn on top
	for card in placeColumn:
		newHand.append(card)
	for card in split[0]:
		newHand.append(card)
	for card in split[1]:
		newHand.append(card)
			

elif secNum==1:
	#put placeColumn on middle
	for card in split[0]:
		newHand.append(card)
	for card in placeColumn:
		newHand.append(card)
	for card in split[1]:
		newHand.append(card)
	

else:
	#put place Column on bottom
	for card in split[0]:
		newHand.append(card)
	for card in split[1]:
		newHand.append(card)
	for card in placeColumn:
		newHand.append(card)

print newHand

'''
THIRD ROUND
'''
split=[newHand[::3],newHand[1::3],newHand[2::3]]

for row in zip(*split):
	print "".join(str.ljust(i,20) for i in row)
print '\n'

secColumn=raw_input('Column? (L,M,R) ')

if secColumn=='L':
	placeColumn=split[0]
elif secColumn=='M':
	placeColumn=split[1]
elif secColumn=='R':
	placeColumn=split[2]
else:
	print 'pick correct params'

newHand=[]
split.remove(placeColumn)
if lastNum==0:
	#put placeColumn on top
	for card in placeColumn:
		newHand.append(card)
	for card in split[0]:
		newHand.append(card)
	for card in split[1]:
		newHand.append(card)
			

elif lastNum==1:
	#put placeColumn on middle
	for card in split[0]:
		newHand.append(card)
	for card in placeColumn:
		newHand.append(card)
	for card in split[1]:
		newHand.append(card)
	

else:
	#put place Column on bottom
	for card in split[0]:
		newHand.append(card)
	for card in split[1]:
		newHand.append(card)
	for card in placeColumn:
		newHand.append(card)

print newHand

print '\n'
for count in range(int(pick)):
	if (count+1)==int(pick):
		print 'Your card is ('+str(count+1) +') cards from the top and is the ' +deal_card(newHand)
	else:
		print '('+str(count+1) +') ' +deal_card(newHand)
	

