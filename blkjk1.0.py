def cards():
	print("+--------+  +--------+  +--------+  +--------+")
	print("| 4      |  | A      |  | J      |  | 10     |")
	print("|        |  |        |  |        |  |        |")
	print("|   *    |  |   *    |  |   *    |  |   *    |")
	print("|        |  |        |  |        |  |        |")
	print("|      4 |  |      A |  |      J |  |     10 |")
	print("+--------+  +--------+  +--------+  +--------+")

import random
import os
import time

money = 500

gamenumber = 0

breakcheck = False

dealerwinner = 0

def clearing():
	os.system('cls' if os.name == 'nt' else 'clear')

cardlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]



def rules():
	print("blkjk1.0 of blackjack.\n\nYou get an initial budget of 100,\nand if you beat the dealer without busting, you win the amount you bet.\nTry surviving as long as you can!\n\n")
	print("Type b to go back to the beginning, x to exit.\n")
	s1 = input()

	if s=="x":
		breakcheck = true

def start():
	global gamenumber
	gamenumber += 1

	clearing()
	cards() #prerequisite
	global money

	print("\n\nEnter your bet: ")
	temp = input()
	s1 = int(temp)

	#dealer turn!
	nonbust = False
	dealernumber = 0

	print("DEALER TURN\n")

	onecheck = False
	
	while nonbust == False:

		if onecheck == False:
			tmp = random.choice(cardlist)
			print ("Dealer chose: " + str(tmp)) 
			print (" ")
			dealernumber += tmp
			if dealernumber >= 13 and dealernumber <= 21:
				print("DEALER DONE: " + str(dealernumber))
				xdealerwinner = dealernumber
				print("\n")
				break
			elif dealernumber > 21:
				print("DEALER BUST\nDEALER HAS "+str(dealernumber)+"\n")
				nonbust = True
				break;
			onecheck = True

		tmp = random.choice(cardlist)
		print ("Dealer chose: REDACTED")
		print (" ")
		dealernumber += tmp
		if dealernumber >= 13 and dealernumber <= 21:
			print("DEALER DONE.")
			dealerwinner = dealernumber
			print("\n")
			break
		elif dealernumber > 21:
			print("DEALER BUST\nDEALER HAS "+str(dealernumber)+"\n")
			nonbust = True
			break;

	if nonbust:
		money += s1
		print("YOU WIN!")
		print("Current money: " + str(money))
		print ("\n")
		print("Loading back to main screen...")
		time.sleep(5)


	else:
		playernumber = 0
		#now it's time for the hit and stand
		playerbust = False
		while playerbust == False:
			tmp = random.choice(cardlist)
			#print(tmp + "\n")
			print("HIT(h) OR BUST(b)?\n")
			s2 = input()
			if s2 == "h":
				playernumber += tmp
				print("You got: "+str(tmp)+"\n"+"Your total: "+str(playernumber)+"\n") 
				print("\n")
				if(playernumber > 21):
					playerbust = True
			else:
				break

		if playerbust == True:
			print ("you lost!\n")
			print("The dealer's score: " + str(dealerwinner) + "\n")
			money -= s1
			print("Loading back to main screen...")

			time.sleep(5)
			
			
		else:
			if playernumber > dealernumber:
				print ("YOU WON\n")
				print("The dealer's score: " + str(dealerwinner) + "\n")
				money += s1
				print("Loading back to main screen...")
				time.sleep(5)
				

			elif playernumber == dealernumber:
				print("TIE\n")
				print("The dealer's score: " + str(dealerwinner) + "\n")
				print("Loading back to main screen...")
				time.sleep(5)
				

			else:
				print("YOU LOST\n")
				print("The dealer's score: " + str(dealerwinner) + "\n")
				print("Loading back to main screen...")
				time.sleep(5)
				





#start of program
while True:
	clearing()
	cards()
	print("blkjk1.0 by jcho49614\n")
	print("a simple blackjack game\n")
	print("type s to start, x to quit, r for rules\n")
	print("Current Money: " + str(money) + "\n")
	print("Current Round Number: " + str(gamenumber) + "\n")

	s = input()

	if s == "x" or money <= 0:
		if money <= 0:
			print ("sorry, you dont have money! Try again!")
		else:
			print ("Do you want to save your score? y/n\n")
			s4 = input()
			if s4 == 'y':
				myfile = open("score.txt", "w")
				myfile.write("Your score was: " + str(money) + "\n")
				myfile.write("Your total round number was: " + str(gamenumber) + "\n")
				myfile.close()
				print("File located at same directory as the application.\n")
				print("Goodbye!\n")
				time.sleep(5)

			else:
				print("Goodbye!\n")
				time.sleep(3)

		break

	elif s=="r":
		rules()
		if breakcheck:
			break
		
	elif s == "s" :
		start()
		

