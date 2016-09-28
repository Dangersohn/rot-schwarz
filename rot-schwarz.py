import random



rot = 16
schwarz	 = 16

def alles():
	global rot 
	global schwarz
	print(rot)  #für debugging
	print(schwarz)
	if  rot > 0 and schwarz > 0:
		choice = random.randrange(1,3)
		print(choice)
		if choice == 1:
			rot = rot - 1
			print("Rot")
		else:
			schwarz = schwarz - 1
			print("schwarz")
	else:
		if input("Es gibt keine Karten mehr noch mal Spielen? Type \"Yes\"") == "yes":
			rot = 16
			schwarz = 16
		else:
			print("okay dann nicht")

if __name__ == "__main__":
	while True:
		if int(input("Karzezihen = 1 ")) == 1:
			alles()
		else:
			print("falschetaste")