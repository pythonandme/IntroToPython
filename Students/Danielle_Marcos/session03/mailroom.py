def printDonorList(donors):
	for donor in donors:
		print donor

donors = [["Anne", 50, 100, 150], 
["Bob", 25, 50],
["Debbie", 5, 15, 30],
["Eric", 65, 75, 100],
["Fran", 250]]

userInput = raw_input("(1) Send a Thank You (2) Create a Report: ")

if userInput == "1":
	name = raw_input("What is the name? ")
	while name.lower() == "list":
		printDonorList(donors)
		name = raw_input("What is the name? ")

	found = False
	for donor in donors:
		if name == donor[0]:
			found = True
			donationUser = donor
	print found

	if found == False:
		newDonor = [name]
		donors.append(newDonor)
		donationUser = donors[-1]

	money = raw_input("Show me the money: ")
	donationUser.append(money)

	printDonorList(donors)


	


