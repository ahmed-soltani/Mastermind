import random

COLORS = ["R", "G", "B", "Y", "W", "O"] # red, blue, green, yellow, white, orange
TRIES = 5
CODE_LENGTH = 4

def generate_code():
	code = []

	for _ in range(CODE_LENGTH):
		color = random.choice(COLORS)
		code.append(color)

	return code

def guess_code():

	while True:
		guess = input("Guess:\n").upper().split(" ")

		if len(guess) != CODE_LENGTH:
			print(f"You must guess {CODE_LENGTH} colors.")
			continue

		for color in guess:
			if color not in COLORS:
				print(f"invalid color: {color}. Try again.")
				break
		else:
			break

	return guess

def check_code(guess, real_code):
	color_counts = {}
	correct_pos = 0
	incorrect_pos = 0

	for color in real_code:
		if color not in color_counts:
			color_counts[color] = 0
		color_counts[color] += 1

	for guess_color, real_color in zip(guess, real_code):
		if guess_color == real_color:
			correct_pos += 1
			color_counts[guess_color] -= 1

	for guess_color, real_color in zip(guess, real_code):
		if guess_color in color_counts and color_counts[guess_color] > 0:
			incorrect_pos += 1
			color_counts[guess_color] -= 1
	return correct_pos, incorrect_pos

def game():
	print(f"Welcome to MasterMind!\nYou have {TRIES} to guess the code...")
	print("The valid colors are", *COLORS)
	print("Write your answer follwing this example:'W W W w'\nBe careful of the whitespaces before the first characters")
	code = generate_code()
	for attempts in range(1, TRIES + 1):
		guess = guess_code()
		correct_pos, incorrect_pos = check_code(guess, code)

		if correct_pos == CODE_LENGTH:
			print(f"You guessed the code in {attempts} tries!")
			break

		print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos} | Guesses left: {TRIES - attempts}")

	else:
		print("You ran out of tries, the code was:", *code)

if __name__ == "__main__":
	game()
