known_users =["John","Ronaldo","Bobby","Lliam","Danny","Griz","Hector","Goku"]

while True:
	print("Hi! My name is travis")
	name =input("What is your name:").strip().capitalize()

	if name in known_users:
		print("Hello{}!".format(name))
		remove = input("would you like to be removed from the system (y/n)?:").strip().lower()
		if remove == "y":
			known_users.remove(name)
		elif remove == "n":
			print("No problem, I didn't want you to leave anyway")
			
			

	else:
		print("hmmmm I dont think I have met you yet {}".format(name))
		add_me = input("would you like to be added to the system (y/n)?:").strip().lower()
		if add_me == "y":
			known_users.append(name)
		elif add_me	== "n":
			print("No worries,see you around!")
