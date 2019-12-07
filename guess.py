#!/usr/bin/python
import sys

def help():
	print("Hello, I'm a guess-computer!")
	print("I can guess any number from 1 to n.")
	print("And I can do it quickly (in not more then log2(n)+1 steps)!")
	print("You have to answer my questions in the following way:")
	print("	h - my guess is to high")
	print("	l - my guess is to low")
	print("	c - my guess is corrrect")
	

def main(argv):
	games = 0
	totalSteps = 0
	help()
	print("Please enter a number n:", end='')	
	n = int(input())
	while True:
		games += 1
		totalSteps += game(n)
		print("I averaged %f guesses per game for %d game(s)." % (totalSteps/games, games))
		answer = ask("Play again (y/n)?",["y","n"])
		if answer == "n":
			break;
		
def ask(question,answers):
	while True:
		print(question, end='')
		answer = input().lower()
		if answer in answers: break
	return answer
		

def game(n):
	steps = 0
	min = 0
	max = n+1
	while True:
		steps += 1
		guess = int((min + max)/2)
		if (min+1 == guess and max-1 == guess):
			break;
		answer = ask(str(guess)+"?",["h","l","c"])
		if answer == "h":
			max = guess
		elif answer == "l":
			min = guess
		else:
			break
	print("Your number is %d." % (guess))
	print("It took me %d guesses." % (steps))
	
	return steps
	

if __name__ == "__main__":
   main(sys.argv[1:])