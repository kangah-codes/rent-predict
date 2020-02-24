import csv
import difflib

with open('tmp.txt', 'r') as town:
	with open('mined_data2.csv', 'r') as file:
		town_reader = csv.reader(town, delimiter=',')
		csv_reader = csv.reader(file, delimiter=',')
		line_count = 0
		town_lines = town.readlines()
		with open('sims.txt', 'a') as sims:
			for row in csv_reader:
				for town in town_lines:
					town_name = town[0]
					if line_count == 0:
						line_count += 1
					else:
						item = row[0].split(' ')
						#print(item[-2]+' '+item[-1], town.split(',')[0])
						try:
							if (difflib.SequenceMatcher(None, item[-2]+' '+item[-1], town.split(',')[0]).ratio()) > 0.6:
								print(item, town)
								try:
									a = town.split(',')
									#print(item)
									if difflib.get_close_matches('furnished', item):
										sims.write(f"{a[0]},{a[1]},{a[2]},{a[3]},{a[4]},{a[5]},{a[6]},{row[1]},{row[2]},{int(row[3].replace(',',''))},1\n")
									else:
										sims.write(f"{a[0]},{a[1]},{a[2]},{a[3]},{a[4]},{a[5]},{a[6]},{row[1]},{row[2]},{int(row[3].replace(',',''))},0\n")
									#print(f"{a[0]},{a[1]},{a[2]},{a[3]},{a[4]},{a[5]},{a[6]},{row[1]},{row[2]},{int(row[3].replace(',',''))}\n")
									#sims.write(f"{(item[-2]+' '+item[-1]).replace(',','')},{town.split(',')[0]}, {difflib.SequenceMatcher(None, item[-2]+' '+item[-1], town.split(',')[0]).ratio()}\n")
								except:
									pass
						except:
							pass
						line_count += 1
			sims.close()
 
