statuses = {
	"Alice": "online",
	"Bob": "offline",
	"Eve": "online",
}

def online_count(dictionary):

	people_online = 0
	for p in dictionary:
		if dictionary[p] == "online":
			people_online += 1
	return people_online

print(f"People online: {online_count(statuses)}")



