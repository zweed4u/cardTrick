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


def cardCollate(decision,split,newHand):
	#global newDeck
	if decision==0:
		#put placeColumn on top
		for card in placeColumn:
			newHand.append(card)
		for card in split[0]:
			newHand.append(card)
		for card in split[1]:
			newHand.append(card)
	elif decision==1:
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


def dealDisplay(arg):
	for row in zip(*arg):
		print "".join(str.ljust(i,20) for i in row)
	print '\n'

def pickPile(arg,split):
	global placeColumn
	if arg=='L' or arg=='l':
		placeColumn=split[0]
	elif arg=='M' or arg=='m':
		placeColumn=split[1]
	elif arg=='R' or arg=='r':
		placeColumn=split[2]
	else:
		print 'pick correct params'

deck=[]
deck = define_cards()
shuffle_deck(deck)

gameBase=[]
for i in range(27):
    	gameBase.append(deal_card(deck))

print '\nPick a card and remember it:'
#Makes a list of lists (each split respectively)
split=[gameBase[i:i+len(gameBase)/3] for i in range(0,len(gameBase),len(gameBase)/3)]
dealDisplay(split)

raw_input('Press ENTER to continue')

print 'Shuffling...'
shuffle_deck(gameBase)
pick=raw_input('What is your favorite number? (1-27) ')

numDecomp(pick)

print '\nWhich column is your card in?:'
split=[gameBase[i:i+len(gameBase)/3] for i in range(0,len(gameBase),len(gameBase)/3)]



dealDisplay(split)
firstColumn=raw_input('Column? (L,M,R) ')

pickPile(firstColumn,split)

newHand=[]
split.remove(placeColumn)
cardCollate(firstNum,split,newHand)


#print newHand




'''
SECOND ROUND
'''
split=[newHand[::3],newHand[1::3],newHand[2::3]]

dealDisplay(split)
secColumn=raw_input('Column? (L,M,R) ')

pickPile(secColumn,split)

newHand=[]
split.remove(placeColumn)

cardCollate(secNum,split,newHand)

#print newHand

'''
THIRD ROUND
'''
split=[newHand[::3],newHand[1::3],newHand[2::3]]

dealDisplay(split)

lastColumn=raw_input('Column? (L,M,R) ')

pickPile(lastColumn,split)

newHand=[]
split.remove(placeColumn)
cardCollate(lastNum,split,newHand)

#print newHand
proof=[]
for card in newHand:
	proof.append(card)

print '\n'
for count in range(int(pick)):
	if (count+1)==int(pick):
		print 'Hmmm... What number is next? '+str(count+1)+"?\nThat's the number you chose, isn't it?"
		print 'Your card is ('+str(count+1) +') cards from the top and is the ==> ' +deal_card(newHand)
	else:
		print '('+str(count+1) +') ' +deal_card(newHand)

'''
print "\nHere's the proof: \n"
step=1
for card in proof:
	print str(step)+'.) '+card
	step+=1
'''
