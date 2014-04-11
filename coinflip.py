#! /usr/bin/env python
import random

f = open("score.txt","r+")
highScore = f.read()
highScore = int(highScore)
score = 0
print "Coin Guessing Game.       All time high score: %d correct" %(highScore)

print 
	
while True:
	coin = random.randint(1,2)
	if coin == 1:
		result = "Heads"
	else:
		result = "Tails"
	
	guess = raw_input("Take a guess? Enter Heads or Tails>  ")
	
	if guess == result:
		score += 1 
		print "It is %s. Your score is %d" %(result,score)
	else:
		print "It is %s. Game Over." %(result)
		f.seek(0)
		if score > highScore:
			f.truncate()
			score = str(score)
			f.write(score) 
			f.flush()
			f.seek(0)
		break
		
print "Your Score:",score,"      High Score:",f.read()   

f.close()  
		