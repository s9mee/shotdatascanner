import json
import requests
import constants
import csv

def main2():
    playerinfo = readcsv()

    per20data = [["playerid", 'S+', 'S', 'A', 'B', 'C', 'D', 'E', 'F']]


    for item in playerinfo:
        if item[0] != "playerid":
            esTOI = getTOI(item[0])

            SS = (float(item[1])/esTOI)* 20
            S = (float(item[2])/esTOI)* 20
            A = (float(item[3])/esTOI)* 20
            B = (float(item[4])/esTOI)* 20
            C = (float(item[5])/esTOI)* 20
            D = (float(item[6])/esTOI)* 20
            E = (float(item[7])/esTOI)* 20
            F = (float(item[8])/esTOI)* 20
            G = (float(item[9])/esTOI)* 20

            per20data.append([item[0], SS, S, A, B, C, D, E, F, G])

    writecsv(per20data)

    print("read complete")

    print('done')
            
def main():
    teamTOI = readcsv()

    per20data = [["team", 'S+', 'S', 'A', 'B', 'C', 'D', 'E', 'F']]


    for item in teamTOI:
        if item[0] != "playerid":
            print(item[0])
            esTOI = getteamsTOI(item[0])

            SS = (float(item[1])/esTOI)* 20
            S = (float(item[2])/esTOI)* 20
            A = (float(item[3])/esTOI)* 20
            B = (float(item[4])/esTOI)* 20
            C = (float(item[5])/esTOI)* 20
            D = (float(item[6])/esTOI)* 20
            E = (float(item[7])/esTOI)* 20
            F = (float(item[8])/esTOI)* 20
            G = (float(item[9])/esTOI)* 20

            per20data.append([item[0], SS, S, A, B, C, D, E, F, G])

    writecsv(per20data)

    print("read complete")

    print('done')

def readcsv():
    csvread = []

    csv.register_dialect('myDialect',
    delimiter = ',',
    skipinitialspace=True)

    with open('/Users/samee/Documents/Shot Danger Project/shot_data_teams.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, dialect='myDialect')
        for row in reader:
            if not row:
                e = 1
            else:
                csvread.append(row)
                #print(playerinfo)
    csvFile.close()

    return csvread


def getteamsTOI(team):

    csv.register_dialect('myDialect',
    delimiter = ',',
    skipinitialspace=True)

    time = 0
    with open('/Users/samee/Documents/Shot Danger Project/es_toi_per_team.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, dialect='myDialect')
        for row in reader:
            if not row:
                e = 1
            else:
                if row[0] == team:
                    time = float(row[1])
    csvFile.close()

    return time

def getTOI(playerid):
    print(playerid)
    game_json = requests.get(constants.API_URL + constants.PEOPLE_ENDPOINT + str(playerid) + constants.STATS_ENDPOINT).json()
    #print(game_json)
    returned = 0
    for item in game_json['stats'][0]['splits']:
        if not item:
            return 1
            returned = 1
        else:
            if 'stat' in game_json['stats'][0]['splits'][0]:
                shiftclock = game_json["stats"][0]["splits"][0]['stat']['evenTimeOnIce']

                seconds = float('0.' + shiftclock.split(':')[1])

                decimal = seconds/0.6

                time = decimal + float(shiftclock.split(':')[0])
                returned = 1

                return time

    if returned == 0:
        return 1
          #      print(time)
        #return time
   # else:
      #  return 0

    #print(decimal)
    #print(shiftclock)
    #print(time)

    #print (decimalplace)



def writecsv(array):
    with open('/Users/samee/Documents/Shot Danger Project/per20teamspureshots.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        for item in array:
            writer.writerows([item])
    #print(OTT)

    csvFile.close()




if __name__ == '__main__':
    main()