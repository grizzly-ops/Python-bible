films = {
	"Spider Man":[16,4],
	"Mortal Kombat":[18,3],
	"Mad Max":[16,6],
	"Avengers":[10,9]
}

while True:
	choice = input("what film would you like to watch?:").strip().title()

	if choice in films:
		age =int(input("how old are you?:").strip())
		#check user age

		if age >= films[choice][0]:
			#check enough seats

			num_seats = films[choice][1]

			if num_seats > 0:
				print("Enjoy the film")
				films[choice][1] = films[choice][1] - 1
			else:
				print("Sorry,we are sold out!")
		else:
			print("you are too young to see that film!")
	
	else:
		print("We don't have that film....sorry")
