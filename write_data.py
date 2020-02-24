import csv
import difflib

with open('tmp.txt', 'r') as town:
	with open('dataminer_0.csv', 'r') as file:
		town_reader = csv.reader(town, delimiter=',')
		csv_reader = csv.reader(file, delimiter=',')
		line_count = 0
		town_lines = town.readlines()
		with open('sims.txt', 'a') as sims:
			for row in csv_reader:
				for town in town_lines:
					try:
						item = row[0].split(' ')
						try:
							if (difflib.SequenceMatcher(None, item[-2]+' '+item[-1], town.split(',')[0]).ratio()) > 0.6:
								try:
									a = town.split(',')
									if difflib.get_close_matches('furnished', item):
										sims.write(f"{a[0]},{a[1]},{a[2]},{a[3]},{a[4]},{a[5]},{a[6]},{row[1]},{row[2]},{row[3]},{row[4]},{int(row[5].replace(',',''))},1\n")
									else:
										sims.write(f"{a[0]},{a[1]},{a[2]},{a[3]},{a[4]},{a[5]},{a[6]},{row[1]},{row[2]},{row[3]},{row[4]},{int(row[5].replace(',',''))},0\n")
								except:
									pass
						except:
							pass
					except:
						pass

			sims.close()
