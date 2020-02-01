import json
import requests
import constants
import csv

def main2():
    yeet = []
    for x in range(8000, 8180):
        yeet.append([x])

    createcsv(yeet)

def main3():

    threatofshot = [[["X"], ["Y"], ["Percent"], ["Total Shots"], ["Goals"]]]

    csv.register_dialect('myDialect',
    delimiter = ',',
    skipinitialspace=True)

    #shots = 0 #
    #goals = 0 #
    #threat = 0 #

    with open('/Users/samee/Documents/Shot Danger Project/ES_shot_locations.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, dialect='myDialect')
        for row in reader:
            print (row)
            shots = 0
            goals = 0
            threat = 0

            for item in row:
                if item == "shot":
                    shots += 1
                else:
                    if item == "goal":
                        goals += 1
        
            total = (goals+shots)

            if total == 0:
                threat = 0 
            else:
                threat = (goals/total)

            if item in row:
                threatofshot.append([str(row[0]), str(row[1]), str(threat), str(total), str(goals)])
                print([row[0], row[1]])

    csvFile.close()

    #total = (goals+shots) #
    #print (goals)
    #print (total)
    #print(goals/total)#

    createcsv(threatofshot)

def main():

    threatofshot = [[["X"], ["Y"], ["Percent"], ["Total Shots"], ["Goals"]]]

    csv.register_dialect('myDialect',
    delimiter = ',',
    skipinitialspace=True)

    #shots = 0 #
    #goals = 0 #
    #threat = 0 #

    with open('/Users/samee/Documents/Shot Danger Project/no_tip_compiled.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, dialect='myDialect')
        for row in reader:
            if not row:
                #print()
                gg = 1
            else:
                print (row)
                shots = 0
                goals = 0
                threat = 0

                for item in row:
                    if item == "shot":
                        shots += 1
                    else:
                        if item == "goal":
                            goals += 1

                total = (goals+shots)

                if total == 0:
                    threat = 0 
                else:
                    threat = (goals/total)

                if item in row:
                    threatofshot.append([str(row[0]), str(row[1]), str(threat), str(total), str(goals)])
                    print([row[0], row[1]])

        csvFile.close()

        #total = (goals+shots) #
        #print (goals)
        #print (total)
        #print(goals/total)#

        createcsv(threatofshot)

def createcsv(array):

    with open('/Users/samee/Documents/Shot Danger Project/ES_pure_shots.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(array)
    
    csvFile.close()

            

if __name__ == '__main__':
    main()