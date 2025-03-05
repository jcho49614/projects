def cards():
	print("+--------+  +--------+  +--------+  +--------+")
	print("| 4      |  | A      |  | J      |  | 10     |")
	print("|        |  |        |  |        |  |        |")
	print("|   ♦    |  |   ♣    |  |   ♠    |  |   ♥    |")
	print("|        |  |        |  |        |  |        |")
	print("|      4 |  |      A |  |      J |  |     10 |")
	print("+--------+  +--------+  +--------+  +--------+")

import random
import os

def clearing():
	os.system('cls' if os.name == 'nt' else 'clear')

cardlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#start of program
while True:
	clearing()
	cards()
	money = 500
	print("blkjk1.0 by jcho49614\n")
	print("a simple blackjack game\n")
	print("type START to start, END to quit, RULES for rules\n")

	s = input()

	if s == "END":
		break

	elif s=="RULES":
		print("blkjk1.0 of blackjack.\n\nYou get an initial budget of 100 and if you beat the dealer without busting, you win the amount you bet.\nTry surviving as long as you can!\n\n")
		print("Type BEGIN to go back to the beginning, END to exit.\n")
		s1 = input()

		if s=="END":
			break
	else:
		clearing()
		cards()
		print("\n\nEnter your bet: ")
		s1 = input()
		print("DEALER TURN\n\n")
		nonbust = False
		dealernumber = 0
		while nonbust == False:
			tmp = random.choice(cardlist)
			print(tmp)
			print (" ")
			dealernumber += tmp
			if dealernumber >= 19 and dealernumber <= 21:
				print("DEALER DONE\n")
				print(dealernumber)
				print("\n")
				break
			elif dealernumber > 21:
				print("DEALER BUST\n")
				nonbust == True
				break;

		if nonbust:
			money += s1
		else:
			playernumber = 0
			#now it's time for the hit and stand
			playerbust = False
			while playerbust == False:
				tmp = random.choice(cardlist)
				#print(tmp + "\n")
				print("HIT OR BUST?\n")
				s2 = input()
				if s2 == "HIT":
					print(tmp)
					print (" ")
					playernumber += tmp
					print(playernumber)
					print("\n")
					if(playernumber > 21):
						playerbust = True
				else:
					break

			if playerbust == True:
				print ("you lost!\n")
				money -= s1
				
			else:
				if playernumber > dealernumber:
					print ("YOU WON\n")
					money += s1
				elif playernumber == dealernumber:
					print("TIE\n")
				else:
					print("YOU LOST\n")

