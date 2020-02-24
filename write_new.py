import csv

"""
city = 1
small_town = 2
big_town = 3
village = 4
"""

towns = {
	"Greater Accra": 1,
	"Ashanti": 2,
	"Brong Ahafo": 3,
	"Central": 4,
	"Eastern Region": 5,
	"Northern": 6,
	"Volta": 7,
	"Western": 8,
	"Upper East": 9,
	"Upper West": 10
}

with open('convertcsv.csv', 'r') as file:
	with open('convert.txt', 'w') as write:
		csv_reader = csv.reader(file, delimiter=',')
		line_count = 0

		for row in csv_reader:
				if line_count == 0:
					line_count += 1
					write.write(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]}\n")
				else:
					# making city
					print(row[0])
					if int(row[6]) >= 100000:
						write.write(f"{row[0]},1,{towns[row[2]]},{row[3]},{row[4]},{row[5]},{row[6]}\n")
					elif int(row[6]) >= 25000:
						write.write(f"{row[0]},3,{towns[row[2]]},{row[3]},{row[4]},{row[5]},{row[6]}\n")
					elif int(row[6]) >= 10000:
						write.write(f"{row[0]},2,{towns[row[2]]},{row[3]},{row[4]},{row[5]},{row[6]}\n")
					else:
						print(row[2])
						write.write(f"{row[0]},4,{towns[row[2]]},{row[3]},{row[4]},{row[5]},{row[6]}\n")
					#print(f"{row}")
					line_count += 1