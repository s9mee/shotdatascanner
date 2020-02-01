import json
import requests
import constants
import csv

def main():
    teams = importplayerteams()
    players  = importplayerrates()

    #csv = []

    for item in players:
        for team in teams:
            playerid = (team[0])[:7]
           # print(playerid)
            if playerid == item[0]:
                playersteam = team[0][-3:]
                print (playersteam)
                item.append(playersteam)

    rewrite(players)

def importplayerrates():

    ee = []

    csv.register_dialect('myDialect',
    delimiter = ',',
    skipinitialspace=True)

    with open('/Users/samee/Documents/Shot Danger Project/per20playerspureshots.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, dialect='myDialect')
        for row in reader:
            if not row:
                e = 1
            else:
                ee.append(row)

    csvFile.close()

    return ee

def importplayerteams():
    ee = []

    csv.register_dialect('myDialect',
    delimiter = ',',
    skipinitialspace=True)

    with open('/Users/samee/Documents/Shot Danger Project/playerteams201819.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, dialect='myDialect')
        for row in reader:
            if not row:
                e = 1
            else:
                ee.append(row)

    csvFile.close()

    return ee

def rewrite(data):
    with open('/Users/samee/Documents/Shot Danger Project/per20playerspureshotsteams.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data)

    csvFile.close()


if __name__ == '__main__':
    main()