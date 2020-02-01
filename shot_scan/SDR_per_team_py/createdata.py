import json
import requests
import constants
import csv

def main():

    csvdata = [["playerid", "S+", "S", "A", "B", "C" ,"D", "E", "F", "S+Rel", "SRel", "ARel", "BRel", "CRel" ,"DRel", "ERel", "FRel"]]

    csv.register_dialect('myDialect',
    delimiter = ',',
    skipinitialspace=True)

    with open('/Users/samee/Documents/Shot_Danger_Project/pure_shot_data/per20playerspureshotsteams.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, dialect='myDialect')
        for row in reader:
            if not row:
                e = 1
            else:
                if row[0] != "playerid":
                    id = row[0]

                    playerdata = getplayerdata(id)
                    name = playerdata[0] + ' ' + playerdata[1]
                    position = playerdata[2]
                    TOI = playerdata[3]
               #     print(TOI)

                    season = "18-19"

                    SS = float(row[1])
                    S = float(row[2])
                    A = float(row[3])
                    B = float(row[4])
                    C = float(row[5])
                    D = float(row[6])
                    E = float(row[7])
                    F = float(row[8])
                    #G = float(row[9])

                    teams = []
                    for item in row:
                        if row[0] != "playerid":
                            if '.' not in item:
                                if len(item) == 3:
                                    if '0' not in item:
                                        teams.append(item)
                    
                    for item in teams:
                        team = item
                        teamdata = getteamdata(team)

                        SSrel = round(SS - float(teamdata[1]), 3)
                        Srel = round(S - float(teamdata[2]), 3)
                        Arel = round(A - float(teamdata[3]), 3)
                        Brel = round(B - float(teamdata[4]), 3)
                        Crel = round(C - float(teamdata[5]), 3)
                        Drel = round(D - float(teamdata[6]), 3)
                        Erel = round(E - float(teamdata[7]), 3)
                        Frel = round(F - float(teamdata[8]), 3)

                        csvdata.append([id, name, position, team, TOI,  SS, S, A, B, C, D, E, F, SSrel, Srel, Arel, Brel, Crel, Drel, Erel, Frel])

    csvFile.close()

    writecsv(csvdata)

    print("Process Complete")


def getteamdata(team):
    data = []
    csv.register_dialect('myDialect',
    delimiter = ',',
    skipinitialspace=True)

    with open('/Users/samee/Documents/Shot_Danger_Project/pure_shot_data/per20teamspureshots.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, dialect='myDialect')
        for row in reader:
            if not row:
                e = 1
            else:
                if row[0] == team:
                    data.append(row[0])
                    data.append(row[1])
                    data.append(row[2])
                    data.append(row[3])
                    data.append(row[4])
                    data.append(row[5])
                    data.append(row[6])
                    data.append(row[7])
                    data.append(row[8])

    #print(data)

    return(data)

def getplayerdata(id):
    print(id)
    #print(playerid)
    playerinfo = requests.get(constants.API_URL + constants.PEOPLE_ENDPOINT + str(id)).json()
    #print(id)

    firstname = playerinfo["people"][0]["firstName"]
    lastname = playerinfo["people"][0]["lastName"]
    position = playerinfo["people"][0]["primaryPosition"]["code"]

    playerstats = requests.get(constants.API_URL + constants.PEOPLE_ENDPOINT + str(id) + constants.STATS_ENDPOINT).json()

    shift_clock = " "

    for item in playerstats['stats'][0]['splits']:
       # print("??")
        if not item:
          #  print('??')
            shift_clock = "N/A"
        else:
            
            if 'stat' in playerstats['stats'][0]['splits'][0]:
                #print('??')
                shift_clock = playerstats["stats"][0]["splits"][0]['stat']['evenTimeOnIce']

    print(shift_clock)
    data = [firstname, lastname, position, shift_clock]

    return data

def writecsv(array):
    with open('/Users/samee/Documents/Shot_Danger_Project/html_csv/playerspureshots.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        for item in array:
            writer.writerows([item])

    csvFile.close()

if __name__ == '__main__':
    main()