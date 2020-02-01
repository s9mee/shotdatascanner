import json
import requests
import constants
import csv

OTT = []
cecishots = []
location_ratings = []

#shift_json = '0'

playershots = [{'playerid': [{'SS' : 'S+', 'S': 'S', 'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F' : 'F', 'G' : 'G'}]}]
teamshots = [{'OTT': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}], 'TOR': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}], 'TBL': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}], 'BOS': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}], 'MTL': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}], 'BUF': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}], 'FLA': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}], 'DET': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],
'WSH': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],'PHI': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],'PIT': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],'NJD': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],'NYR': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],'CBJ': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],'NYI': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],'CAR': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],
'VGK': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],'SJS': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],'CGY': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],'EDM': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],'ARI': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],'ANA': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],'LAK': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],'VAN': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],
'STL': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],'DAL': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],'CHI': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],'WPG': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],'MIN': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],'NSH': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}],'COL': [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}]}]


def main2():

    read_ratings()
    for x in range(2018020001, 2018021271):
        #str(x)
        shotdatapergameshift(str(x))

    data = []
    F = 0
    E = 0
    D = 0
    C = 0
    B = 0
    A = 0
    S = 0
    SS = 0 
    home_shots = 0

    for x in range (0, 10):
        value = 0
        for item in OTT:
            value += item[x]
        data.append(value)

    print(data)

    print()
    print()
    print()
    #aa = data[8]-582
    #bb = data[0]-162
    #cc = data[1]-89
   # dd = data[2]-55
   # ee = data[3]-107
  #  ff = data[4]-73
  #  hh = data[5]-37
  #  ii = data[6]-106
  #  jj = data[7]-123

   # print("G = " + str(aa) + ' - ' + str(round((aa/g)*20, 2)) + ' shots against/20')
   # print("F = " + str(bb) + ' - ' + str(round((bb/g)*20, 2)) + ' shots against/20')
   # print("E = " + str(cc) + ' - ' + str(round((cc/g)*20, 2)) + ' shots against/20')
   # print("D = " + str(dd) + ' - ' + str(round((dd/g)*20, 2)) + ' shots against/20')
   # print("C = " + str(ee) + ' - ' + str(round((ee/g)*20, 2)) + ' shots against/20')
   # print("B = " + str(ff) + ' - ' + str(round((ff/g)*20, 2)) + ' shots against/20')
   # print("A = " + str(hh) + ' - ' + str(round((hh/g)*20, 2)) + ' shots against/20')
   # print("S = " + str(ii) + ' - ' + str(round((ii/g)*20, 2)) + ' shots against/20')
   # print("S+ = " + str(jj) + ' - ' + str(round((jj/g)*20, 2 )) + ' shots against/20')

    #print("F = " + str(data[0]) + ' - ' + str(round(data[0]/data[8], 2)) + '% - ' + str(round(data[0]/82, 2)) + ' Shots/GP')
    #print("E = " + str(data[1]) + ' - ' + str(round(data[1]/data[8], 2)) + '% - ' + str(round(data[1]/82, 2)) + ' Shots/GP')
    #print("D = " + str(data[2]) + ' - ' + str(round(data[2]/data[8], 2)) + '% - ' + str(round(data[2]/82, 2)) + ' Shots/GP')
    #print("C = " + str(data[3]) + ' - ' + str(round(data[3]/data[8], 2)) + '% - ' + str(round(data[3]/82, 2)) + ' Shots/GP')
    #print("B = " + str(data[4]) + ' - ' + str(round(data[4]/data[8], 2)) + '% - ' + str(round(data[4]/82, 2)) + ' Shots/GP')
    #print("A = " + str(data[5]) + ' - ' + str(round(data[5]/data[8], 2)) + '% - ' + str(round(data[5]/82, 2)) + ' Shots/GP')
    #print("S = " + str(data[6]) + ' - ' + str(round(data[6]/data[8], 2)) + '% - ' + str(round(data[6]/82, 2)) + ' Shots/GP')
    #print("S+ = " + str(data[7]) + ' - ' + str(round(data[7]/data[8], 2)) + '% - ' + str(round(data[7]/82, 2)) + ' Shots/GP')
    #print("Total Shots = " + str(data[8]))

def main():
    read_ratings()
    for x in range(2018020001, 2018021271): #2018021271
    #str(x)
        print(x)
        #print(playershots)
        shotdatapergame(str(x))
    
    #print(playershots)


    with open('/Users/samee/Documents/Shot Danger Project/shot_data_teams.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        for item in teamshots[0]:
            #writer.writerows([[item, playershots[0][item][0]['SS'], playershots[0][item][0]['S'], playershots[0][item][0]['A'], playershots[0][item][0]['B'], playershots[0][item][0]['C'], playershots[0][item][0]['D'], playershots[0][item][0]['E'], playershots[0][item][0]['F'], playershots[0][item][0]['G']]])
            writer.writerows([[item, teamshots[0][item][0]['SS'], teamshots[0][item][0]['S'], teamshots[0][item][0]['A'], teamshots[0][item][0]['B'], teamshots[0][item][0]['C'], teamshots[0][item][0]['D'], teamshots[0][item][0]['E'], teamshots[0][item][0]['F'], teamshots[0][item][0]['G']]])

            #print(OTT)

    csvFile.close()

    #data = []
   # for x in range (0, 10):
    #    value = 0
    #    for item in OTT:
     #       value += item[x]
    #    data.append(value)

  #  print (data)

def createGameList():
    game_list = []
    for x in range(2018020001, 2018021271):

        game_id = str (x)
        game = []

        game.append(game_id)

        game_json = requests.get(constants.API_URL + constants.GAMES_ENDPOINT + game_id + constants.FEED_ENDPOINT).json()
        
        game.append(game_json["gameData"]["teams"]["away"]["abbreviation"])
        game.append(game_json["gameData"]["teams"]["home"]["abbreviation"])

        print(game)
        game_list.append(game)


    with open('/Users/samee/Documents/Shot Danger Project/games_201819.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(game_list)
    
    csvFile.close()

    print("created game list successfully")

def shotdataplayers(id):

    game_json = requests.get(constants.API_URL + constants.GAMES_ENDPOINT + id + constants.FEED_ENDPOINT).json()
    shift_json = requests.get(constants.SHIFTS_STARTPOINT + id).json()

    away = game_json["gameData"]["teams"]["away"]["triCode"]
    home = game_json["gameData"]["teams"]["home"]["triCode"]


    for player in game_json["gameData"]["players"]:
        playerid = game_json["gameData"]["players"][player]['id']
        if game_json["gameData"]["players"][player]["primaryPosition"]["type"] != "Goalie":
            #checking when PPGs were
            PPG = []
            for item in game_json["liveData"]["plays"]["allPlays"]:
                if item["result"]["event"] == "Goal":
                    if item["result"]["strength"]["code"] == "PPG":
                        timeofgoal = item["about"]["periodTimeRemaining"]
                        period = item["about"]["period"]
                        goalt1 = float(timeofgoal.split(':')[0])
                        goalt2 = float(timeofgoal.split(':')[1])
                        PPG.append([timeofgoal, goalt1, goalt2, period])

            # print(PPG)
            penaltyranges = []

            #creating penalty time ranges
            for item in game_json["liveData"]["plays"]["allPlays"]:
                if item["result"]["event"] == "Penalty":
                    if item["result"]["secondaryType"] != "Fighting":

                        if item["result"]["penaltySeverity"] == "Major":
                            time = item["about"]["periodTimeRemaining"]
                            floattime1 = float(time.split(':')[0])

                            if floattime1 < 5:

                                eop = 4 - floattime1

                                nextperiod = item["about"]["period"] + 1
                                time2 = "0"+(str(19 - eop)).split('.')[0] + ":" + time.split(":")[1]
                                penaltyranges.append(["20:00", time2, nextperiod])

                            else:
                                secondtime = "0"+(str(floattime1 - 5)).split('.')[0] + ":" + time.split(':')[1]
                                penaltyranges.append([time, secondtime, item["about"]["period"]])
                                #print(penaltyranges)

                        if item["result"]["penaltySeverity"] == "Minor":
                            time = item["about"]["periodTimeRemaining"]
                            time1 = float(time.split(':')[0])
                            time2 = float(time.split(':')[1])
                            period = item["about"]["period"]

                            if time1 < 2:
                                eop = 0
                                penb4end = 0

                                for goal in PPG:
                                    if goal[3] == period:
                                        if eop <= goal[1] <= time1:
                                            if goal[1] == time1:
                                                if goal[2] <= time2:
                                                    penaltyranges.append([time, goal[0], period])
                                                    penb4end = 1
                                            else:
                                                if goal[1] == eop:
                                                    if goal[2] >= time2:
                                                        penaltyranges.append([time, goal[0], period])
                                                        penb4end = 1
                                                else:
                                                    penaltyranges.append([time, goal[0], period])
                                                    penb4end = 1

                                if penb4end != 1:
                                    #print(time)
                                    penaltyranges.append([time, "00:00", period])
                                    timep2 = "20:00"

                                    nextperiod = period+1

                                    eop2 = 1 - time1

                                    eopp = 19 - eop2
                                    
                                    penb4end2 = 0

                                    for goal in PPG:
                                        if goal[3] == nextperiod:
                                            if eopp <= goal[1] <= 20:
                                                if goal[1] == eopp:
                                                    if goal[2] >= time2:
                                                        penaltyranges.append([timep2, goal[0], nextperiod])
                                                        penb4end2 = 1
                                                else:
                                                    penaltyranges.append([timep2, goal[0], nextperiod])
                                                    penb4end2 = 1
                                    
                                    if penb4end2 != 1:
                                        penaltytimeleft = 1 - time1
                                        endofpenalty = (str(19-penaltytimeleft)).split('.')[0] + ":" + time.split(':')[1]
                                        penaltyranges.append(["20:00", endofpenalty, nextperiod])


                            

                            #make exception for double minors fuck

                            #print(time + " - " + str(eop))
                            else:
                                eop = time1 - 2
                                wasthereagoal = 0
                                for goal in PPG:
                                    if goal[3] == period:
                                        if eop <= goal[1] <= time1:
                                            if goal[1] == time1:
                                                if goal[2] <= time2:
                                                    penaltyranges.append([time, goal[0], period])
                                                    wasthereagoal = 1
                                            else:
                                                if goal[1] == eop:
                                                    if goal[2] >= time2:
                                                        penaltyranges.append([time, goal[0], period])
                                                        wasthereagoal = 1
                                                else:
                                                    penaltyranges.append([time, goal[0], period])
                                                    wasthereagoal = 1
                                
                                if wasthereagoal != 1:
                                    eop = (str(time1 - 2)).split('.')[0] + ":" + time.split(':')[1]
                                    penaltyranges.append([time, eop, period])


           # game_data = []
            #print (penaltyranges)

            #reading shotsplayerlist = 

            #if playerid == 8476879:
            
           # cc = playerid

            playerteam = '0'
            playershifts = []
            for item in shift_json["data"]:
                if item["playerId"] == playerid:
                    playerteam = item["teamAbbrev"]
                    playershifts.append([item["startTime"], item["endTime"], item["period"], item["teamAbbrev"]])

           # print([item["startTime"], item["endTime"], item["period"]])
            #playershifts = getcodyceci(id, playerid, shift_json)
            #print(playerinfo[1])

            stringid = str(playerid)

            if (stringid) in playershots[0]:
                yay = 1
            else:
                #if away == "OTT" or home == 'OTT':
                # if playerinfo[1] == "EDM":
                playershots[0][stringid] = [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}]
                print("ayomyn")

                #game_data.append([(str(x)), (str(y)), period, tpp, tpp1, tpp2, teamshooting, result, strength])

            game_data = []
            for item in game_json["liveData"]["plays"]["allPlays"]:
                if "x" in item["coordinates"]:
                    if "y" in item["coordinates"]:
                        if item["result"]["event"] == "Shot":
                            if "secondaryType" in item["result"]:
                                if item['result']['secondaryType'] != "Tip-In":
                                    if item['result']['secondaryType'] != "Deflected":
                                        teamshooting = item["team"]["triCode"]
                                        x = abs(item["coordinates"]["x"])
                                        y = item["coordinates"]["y"]
                                        result = "shot"
                                        period = item["about"]["period"]
                                        tos = item["about"]["periodTimeRemaining"]
                                        tos1 = float(tos.split(':')[0])
                                        tos2 = float(tos.split(':')[1])

                                        tpp = item["about"]["periodTime"]
                                        tpp1 = float(tpp.split(':')[0])
                                        tpp2 = float(tpp.split(':')[1])

                                        evenstrength = 0

                                        for item in penaltyranges:
                                            if item[2] == period:
                                                PPstart1 = float(item[0].split(':')[0])
                                                PPstart2 = float(item[0].split(':')[1])
                                                PPend1 = float(item[1].split(':')[0])
                                                PPend2 = float(item[1].split(':')[1])


                                                if PPend1 <= tos1 <=PPstart1:
                                                    if PPstart1 == tos1:
                                                        if tos2 <= PPstart2:
                                                            #strength = "uneven"
                                                            evenstrength = 1
                                                    else:
                                                        if PPend1 == tos1:
                                                            if tos2 >= PPend2:
                                                                #strength = "uneven"
                                                                evenstrength = 1
                                                        else:
                                                            #strength = "uneven"
                                                            evenstrength = 1

                                        if evenstrength == 1:
                                            strength = "uneven"

                                        else:
                                            on_ice = 0
                                            for item in playershifts:
                                                if item[2] == period:
                                                    shiftstart1 = float(item[0].split(':')[0])
                                                    shiftstart2 = float(item[0].split(':')[1])
                                                    shiftend1 = float(item[1].split(':')[0])
                                                    shiftend2 = float(item[1].split(':')[1])    

                                                    if shiftend1 >= tpp1 >= shiftstart1:
                                                        if shiftstart1 == tpp1:
                                                            if tpp2 >= shiftstart2:
                                                                on_ice = 1
                                                        else:
                                                            if shiftend1 == tpp1:
                                                                if tpp2 <= shiftend2:
                                                                    on_ice = 1
                                                            else:
                                                                on_ice = 1

                                            if on_ice == 1:
                                                strength = "even"
                                                game_data.append([(str(x)), (str(y)), teamshooting, result, strength])

                                #for item in penaltyranges:

                        else:
                            if item["result"]["event"] == "Goal":
                                if "secondaryType" in item["result"]:
                                    if item['result']['secondaryType'] != "Tip-In":
                                        if item['result']['secondaryType'] != "Deflected":
                                            x = abs(item["coordinates"]["x"])
                                            y = item["coordinates"]["y"]
                                            teamshooting = item["team"]["triCode"]
                                            result = "goal"
                                            strength = item["result"]["strength"]["name"]
                                            tos = item["about"]["periodTimeRemaining"]
                                            tos1 = float(tos.split(':')[0])
                                            tos2 = float(tos.split(':')[1])

                                            tpp = item["about"]["periodTime"]
                                            tpp1 = float(tpp.split(':')[0])
                                            tpp2 = float(tpp.split(':')[1])
                                            if strength == "Even": 
                                                on_ice = 0
                                                for item in playershifts:
                                                    if item[2] == period:
                                                        shiftstart1 = float(item[0].split(':')[0])
                                                        shiftstart2 = float(item[0].split(':')[1])
                                                        shiftend1 = float(item[1].split(':')[0])
                                                        shiftend2 = float(item[1].split(':')[1])

                                                        if shiftend1 >= tpp1 >= shiftstart1:
                                                            if shiftstart1 == tpp1:
                                                                if tpp2 >= shiftstart2:
                                                                    on_ice = 1
                                                            else:
                                                                if shiftend1 == tpp1:
                                                                    if tpp2 <= shiftend2:
                                                                        on_ice = 1
                                                                else:
                                                                    on_ice = 1

                                                if on_ice == 1:
                                                    strength = "even"
                                                    game_data.append([(str(x)), (str(y)), teamshooting, result, strength])
                            
            #print(game_data)

            away_ratings = []
            home_ratings = []

            #print(id)
            for row in location_ratings:    
                for item in game_data:
                    #if item[3] == "goal":
                    if item[0] == (row[0]+'.0'):
                        if item[1] == (row[1]+'.0'):
                            #print(item)
                            #print(row[7])
                            if item[2] == home:
                                home_ratings.append([item[0], item[1], row[6]])
                            else:
                                away_ratings.append([item[0], item[1], row[6]])
            # print(playerinfo[1])
            #if playerinfo[1] == "EDM":
            Gh = 0
            Fh = 0
            Eh = 0
            Dh = 0
            Ch = 0
            Bh = 0
            Ah = 0
            Sh = 0
            SSh = 0
            thefuckyoumissedmycall = 0
            home_shots = 0

            for item in home_ratings:
                home_shots += 1
                shot_rating = float(item[2])
                if 0 <= shot_rating <= 0.05:
                    #store in F class
                    Fh += 1
                else:
                    if 0.05 < shot_rating <= 0.08:
                        #store in D class
                        Eh += 1
                    else:
                        if 0.08 < shot_rating <= 0.1:
                            #store in C class
                            Dh += 1
                        else:
                            if 0.1 < shot_rating <= 0.12:
                                #store in B class
                                Ch += 1
                            else:
                                if 0.12 < shot_rating <= 0.15:
                                    #store in A class
                                    Bh += 1
                                else:
                                    if 0.15 < shot_rating <= 0.175:
                                        #store in A+ class
                                        Ah += 1
                                    else:
                                        if 0.175 < shot_rating <= 0.225:
                                            #store in S class
                                            Sh += 1
                                        else:
                                            if 0.225 < shot_rating <= 0.25:
                                                #store in S+ class
                                                SSh += 1
                                            else:
                                                thefuckyoumissedmycall +=1

            Ga = 0
            Fa = 0
            Ea = 0
            Da = 0
            Ca = 0
            Ba = 0
            Aa = 0
            Sa = 0
            SSa = 0 
            away_shots = 0
            noididnt = 0

            for item in away_ratings:
                away_shots += 1
                shot_rating = float(item[2])
                if 0 <= shot_rating <= 0.05:
                    #store in F class
                    Fa += 1
                else:
                    if 0.05 < shot_rating <= 0.08:
                        #store in D class
                        Ea += 1
                    else:
                        if 0.08 < shot_rating <= 0.1:
                            #store in C class
                            Da += 1
                        else:
                            if 0.1 < shot_rating <= 0.12:
                                #store in B class
                                Ca += 1
                            else:
                                if 0.12 < shot_rating <= 0.14:
                                    #store in A class
                                    Ba += 1
                                else:
                                    if 0.14 < shot_rating <= 0.175:
                                        #store in A+ class
                                        Aa += 1
                                    else:
                                        if 0.175 < shot_rating <= 0.225:
                                            #store in S class
                                            Sa += 1
                                        else:
                                            if 0.225 < shot_rating:
                                                #store in S+ class
                                                SSa += 1
                                            else:
                                                noididnt += 1
            

            if home == "OTT":
                OTT.append([Ga, Fa, Ea, Da, Ca, Ba, Aa, Sa, noididnt, away_shots])
            else:
                if away == "OTT":
                    OTT.append([Gh, Fh, Eh, Dh, Ch, Bh, Ah, Sh, thefuckyoumissedmycall, home_shots])

            if home == playerteam:
                SS = float(playershots[0][stringid][0]['SS']) + SSa
                S = float(playershots[0][stringid][0]['S']) + Sa
                A = float(playershots[0][stringid][0]['A']) + Aa
                B = float(playershots[0][stringid][0]['B']) + Ba
                C = float(playershots[0][stringid][0]['C']) + Ca
                D = float(playershots[0][stringid][0]['D']) + Da 
                E = float(playershots[0][stringid][0]['E']) + Ea
                F = float(playershots[0][stringid][0]['F']) + Fa
                G = float(playershots[0][stringid][0]['G']) + Ga

                playershots[0][stringid][0]['SS'] = SS
                playershots[0][stringid][0]['S'] = S
                playershots[0][stringid][0]['A'] = A
                playershots[0][stringid][0]['B'] = B
                playershots[0][stringid][0]['C'] = C
                playershots[0][stringid][0]['D'] = D
                playershots[0][stringid][0]['E'] = E
                playershots[0][stringid][0]['F'] = F
                playershots[0][stringid][0]['G'] = G

            # print("done")


            else:
                if away == playerteam:
                    SS = float(playershots[0][stringid][0]['SS']) + SSh 
                    S = float(playershots[0][stringid][0]['S']) + Sh
                    A = float(playershots[0][stringid][0]['A']) + Ah
                    B = float(playershots[0][stringid][0]['B']) + Bh
                    C = float(playershots[0][stringid][0]['C']) + Ch
                    D = float(playershots[0][stringid][0]['D']) + Dh
                    E = float(playershots[0][stringid][0]['E']) + Eh
                    F = float(playershots[0][stringid][0]['F']) + Fh
                    G = float(playershots[0][stringid][0]['G']) + Gh

                    playershots[0][stringid][0]['SS'] = SS
                    playershots[0][stringid][0]['S'] = S
                    playershots[0][stringid][0]['A'] = A
                    playershots[0][stringid][0]['B'] = B
                    playershots[0][stringid][0]['C'] = C
                    playershots[0][stringid][0]['D'] = D
                    playershots[0][stringid][0]['E'] = E
                    playershots[0][stringid][0]['F'] = F
                    playershots[0][stringid][0]['G'] = G

                        #  print("done")
    
def shotdatapergame(id):
    
    game_json = requests.get(constants.API_URL + constants.GAMES_ENDPOINT + id + constants.FEED_ENDPOINT).json()

    away = game_json["gameData"]["teams"]["away"]["triCode"]
    home = game_json["gameData"]["teams"]["home"]["triCode"]
    

    #checking when PPGs were
    PPG = []
    for item in game_json["liveData"]["plays"]["allPlays"]:
        if item["result"]["event"] == "Goal":
            if item["result"]["strength"]["code"] == "PPG":
                timeofgoal = item["about"]["periodTimeRemaining"]
                period = item["about"]["period"]
                goalt1 = float(timeofgoal.split(':')[0])
                goalt2 = float(timeofgoal.split(':')[1])
                PPG.append([timeofgoal, goalt1, goalt2, period])

    # print(PPG)
    penaltyranges = []
    penaltyrangess = []

    #creating penalty time ranges
    for item in game_json["liveData"]["plays"]["allPlays"]:
        if item["result"]["event"] == "Penalty":
            if item["result"]["secondaryType"] != "Fighting":

                if item["result"]["penaltySeverity"] == "Major":
                    time = item["about"]["periodTimeRemaining"]
                    floattime1 = float(time.split(':')[0])

                    if floattime1 < 5:

                        eop = 4 - floattime1

                        nextperiod = item["about"]["period"] + 1
                        time2 = "0"+(str(19 - eop)).split('.')[0] + ":" + time.split(":")[1]
                        penaltyranges.append(["20:00", time2, nextperiod])

                    else:
                        secondtime = "0"+(str(floattime1 - 5)).split('.')[0] + ":" + time.split(':')[1]
                        penaltyranges.append([time, secondtime, item["about"]["period"]])
                        #print(penaltyranges)

                if item["result"]["penaltySeverity"] == "Minor":
                    time = item["about"]["periodTimeRemaining"]
                    time1 = float(time.split(':')[0])
                    time2 = float(time.split(':')[1])
                    period = item["about"]["period"]

                    if time1 < 2:
                        eop = 0
                        penb4end = 0

                        for goal in PPG:
                            if goal[3] == period:
                                if eop <= goal[1] <= time1:
                                    if goal[1] == time1:
                                        if goal[2] <= time2:
                                            penaltyranges.append([time, goal[0], period])
                                            penb4end = 1
                                    else:
                                        if goal[1] == eop:
                                            if goal[2] >= time2:
                                                penaltyranges.append([time, goal[0], period])
                                                penb4end = 1
                                        else:
                                            penaltyranges.append([time, goal[0], period])
                                            penb4end = 1

                        if penb4end != 1:
                            #print(time)
                            penaltyranges.append([time, "00:00", period])
                            timep2 = "20:00"

                            nextperiod = period+1

                            eop2 = 1 - time1

                            eopp = 19 - eop2
                            
                            penb4end2 = 0

                            for goal in PPG:
                                if goal[3] == nextperiod:
                                    if eopp <= goal[1] <= 20:
                                        if goal[1] == eopp:
                                            if goal[2] >= time2:
                                                penaltyranges.append([timep2, goal[0], nextperiod])
                                                penb4end2 = 1
                                        else:
                                            penaltyranges.append([timep2, goal[0], nextperiod])
                                            penb4end2 = 1
                            
                            if penb4end2 != 1:
                                penaltytimeleft = 1 - time1
                                endofpenalty = (str(19-penaltytimeleft)).split('.')[0] + ":" + time.split(':')[1]
                                penaltyranges.append(["20:00", endofpenalty, nextperiod])


                    

                    #make exception for double minors fuck

                    #print(time + " - " + str(eop))
                    else:
                        eop = time1 - 2
                        wasthereagoal = 0
                        for goal in PPG:
                            if goal[3] == period:
                                if eop <= goal[1] <= time1:
                                    if goal[1] == time1:
                                        if goal[2] <= time2:
                                            penaltyranges.append([time, goal[0], period])
                                            wasthereagoal = 1
                                    else:
                                        if goal[1] == eop:
                                            if goal[2] >= time2:
                                                penaltyranges.append([time, goal[0], period])
                                                wasthereagoal = 1
                                        else:
                                            penaltyranges.append([time, goal[0], period])
                                            wasthereagoal = 1
                        
                        if wasthereagoal != 1:
                            eop = (str(time1 - 2)).split('.')[0] + ":" + time.split(':')[1]
                            penaltyranges.append([time, eop, period])

    #print (penaltyranges)

    #reading shots
    game_data = []
    for item in game_json["liveData"]["plays"]["allPlays"]:
        if "x" in item["coordinates"]:
            if "y" in item["coordinates"]:
                if item["result"]["event"] == "Shot":
                    if "secondaryType" in item["result"]:
                        if item['result']['secondaryType'] != "Tip-In":
                            if item['result']['secondaryType'] != "Deflected":
                                teamshooting = item["team"]["triCode"]
                                x = abs(item["coordinates"]["x"])
                                y = item["coordinates"]["y"]
                                result = "shot"
                                period = item["about"]["period"]
                                tos = item["about"]["periodTimeRemaining"]
                                tos1 = float(tos.split(':')[0])
                                tos2 = float(tos.split(':')[1])

                                tpp = item["about"]["periodTime"]
                                tpp1 = float(tpp.split(':')[0])
                                tpp2 = float(tpp.split(':')[1])

                                evenstrength = 0

                                for item in penaltyrangess:
                                    if item[2] == period:
                                        PPstart1 = float(item[0].split(':')[0])
                                        PPstart2 = float(item[0].split(':')[1])
                                        PPend1 = float(item[1].split(':')[0])
                                        PPend2 = float(item[1].split(':')[1])


                                        if PPend1 <= tos1 <=PPstart1:
                                            if PPstart1 == tos1:
                                                if tos2 <= PPstart2:
                                                    #strength = "uneven"
                                                    evenstrength = 1
                                            else:
                                                if PPend1 == tos1:
                                                    if tos2 >= PPend2:
                                                        #strength = "uneven"
                                                        evenstrength = 1
                                                else:
                                                    #strength = "uneven"
                                                    evenstrength = 1

                                if evenstrength == 1:
                                    strength = "uneven"

                                else:
                                    strength = "even"
                                    game_data.append([(str(x)), (str(y)), teamshooting, result, strength])

                    #for item in penaltyranges:

                else:
                    if item["result"]["event"] == "Goal":
                        x = abs(item["coordinates"]["x"])
                        y = item["coordinates"]["y"]
                        teamshooting = item["team"]["triCode"]
                        result = "goal"
                        strength = item["result"]["strength"]["name"]
                        tos = item["about"]["periodTimeRemaining"]
                        tos1 = float(tos.split(':')[0])
                        tos2 = float(tos.split(':')[1])

                        tpp = item["about"]["periodTime"]
                        tpp1 = float(tpp.split(':')[0])
                        tpp2 = float(tpp.split(':')[1])
                        if strength == "Even": 
                            strength = "even"
                            game_data.append([(str(x)), (str(y)), teamshooting, result, strength])
                   # else:
                    #    if item["result"]["event"] == "Missed Shot":
                     #       x = abs(item["coordinates"]["x"])
                      #      y = item["coordinates"]["y"]
                       #     result = "shot"
                        #    period = item["about"]["period"]
                         #   tos = item["about"]["periodTimeRemaining"]
                          #  teamshooting = item["team"]["triCode"]
                           # tos1 = float(tos.split(':')[0])
                           # tos2 = float(tos.split(':')[1])

                            #tpp = item["about"]["periodTime"]
                            #tpp1 = float(tpp.split(':')[0])
                            #tpp2 = float(tpp.split(':')[1])

                   #         evenstrength = 0

                    #        for item in penaltyrangess:
                     #           if item[2] == period:
                      #              PPstart1 = float(item[0].split(':')[0])
                       #             PPstart2 = float(item[0].split(':')[1])
                        #            PPend1 = float(item[1].split(':')[0])
                         #           PPend2 = float(item[1].split(':')[1])


                          #          if PPend1 <= tos1 <=PPstart1:
                           #             if PPstart1 == tos1:
                            #                if tos2 <= PPstart2:
                             #                   #strength = "uneven"
                              #                  evenstrength = 1
                               #         else:
                                #            if PPend1 == tos1:
                                 #               if tos2 >= PPend2:
                                  #                  #strength = "uneven"
                                   #                 evenstrength = 1
                                    #        else:
                                     #           #strength = "uneven"
                                      #          evenstrength = 1

                       #     if evenstrength == 1:
                        #        strength = "uneven"

                         #   else:
                          #      strength = "even"
                           #     game_data.append([(str(x)), (str(y)), teamshooting, result, strength])

    #print(game_data)

    away_ratings = []
    home_ratings = []

    #print(id)
    for row in location_ratings:    
        for item in game_data:
            #if item[3] == "goal":
            if item[0] == (row[0]+'.0'):
                if item[1] == (row[1]+'.0'):
                    #print(item)
                    #print(row[7])
                    if item[2] == home:
                        home_ratings.append([item[0], item[1], row[6]])
                    else:
                        away_ratings.append([item[0], item[1], row[6]])
    
    Gh = 0
    Fh = 0
    Eh = 0
    Dh = 0
    Ch = 0
    Bh = 0
    Ah = 0
    Sh = 0
    SSh = 0
    thefuckyoumissedmycall = 0
    home_shots = 0

    for item in home_ratings:
        home_shots += 1
        shot_rating = float(item[2])
        if 0 <= shot_rating <= 0.05:
            #store in F class
            Fh += 1
        else:
            if 0.05 < shot_rating <= 0.08:
                #store in D class
                Eh += 1
            else:
                if 0.08 < shot_rating <= 0.1:
                    #store in C class
                    Dh += 1
                else:
                    if 0.1 < shot_rating <= 0.12:
                        #store in B class
                        Ch += 1
                    else:
                        if 0.12 < shot_rating <= 0.15:
                            #store in A class
                            Bh += 1
                        else:
                            if 0.15 < shot_rating <= 0.175:
                                #store in A+ class
                                Ah += 1
                            else:
                                if 0.175 < shot_rating <= 0.225:
                                    #store in S class
                                    Sh += 1
                                else:
                                    if 0.225 < shot_rating:
                                        #store in S+ class
                                        SSh += 1
                                    else:
                                        thefuckyoumissedmycall +=1

    Ga = 0
    Fa = 0
    Ea = 0
    Da = 0
    Ca = 0
    Ba = 0
    Aa = 0
    Sa = 0
    SSa = 0 
    away_shots = 0
    noididnt = 0

    for item in away_ratings:
        away_shots += 1
        shot_rating = float(item[2])
        if 0 <= shot_rating <= 0.05:
            #store in F class
            Fa += 1
        else:
            if 0.05 < shot_rating <= 0.08:
                #store in D class
                Ea += 1
            else:
                if 0.08 < shot_rating <= 0.1:
                    #store in C class
                    Da += 1
                else:
                    if 0.1 < shot_rating <= 0.12:
                        #store in B class
                        Ca += 1
                    else:
                        if 0.12 < shot_rating <= 0.15:
                            #store in A class
                            Ba += 1
                        else:
                            if 0.15 < shot_rating <= 0.175:
                                #store in A+ class
                                Aa += 1
                            else:
                                if 0.175 < shot_rating <= 0.225:
                                    #store in S class
                                    Sa += 1
                                else:
                                    if 0.225 < shot_rating:
                                        #store in S+ class
                                        SSa += 1
                                    else:
                                        noididnt += 1
    

    if home == "OTT":
        OTT.append([Ga, Fa, Ea, Da, Ca, Ba, Aa, Sa, noididnt, away_shots])
    else:
        if away == "OTT":
            OTT.append([Gh, Fh, Eh, Dh, Ch, Bh, Ah, Sh, thefuckyoumissedmycall, home_shots])

    #if home == playerteam:
    SSaa = float(teamshots[0][home][0]['SS']) + SSa
    Saa = float(teamshots[0][home][0]['S']) + Sa
    Aaa = float(teamshots[0][home][0]['A']) + Aa
    Baa = float(teamshots[0][home][0]['B']) + Ba
    Caa = float(teamshots[0][home][0]['C']) + Ca
    Daa = float(teamshots[0][home][0]['D']) + Da
    Eaa = float(teamshots[0][home][0]['E']) + Ea
    Faa = float(teamshots[0][home][0]['F']) + Fa
    Gaa = float(teamshots[0][home][0]['G']) + Ga

    teamshots[0][home][0]['SS'] = SSaa
    teamshots[0][home][0]['S'] = Saa
    teamshots[0][home][0]['A'] = Aaa
    teamshots[0][home][0]['B'] = Baa
    teamshots[0][home][0]['C'] = Caa
    teamshots[0][home][0]['D'] = Daa
    teamshots[0][home][0]['E'] = Eaa
    teamshots[0][home][0]['F'] = Faa
    teamshots[0][home][0]['G'] = Gaa

    # print("done")


    # else:
        # if away == playerteam:
    SShh = float(teamshots[0][away][0]['SS']) + SSh
    Shh = float(teamshots[0][away][0]['S']) + Sh
    Ahh = float(teamshots[0][away][0]['A']) + Ah
    Bhh = float(teamshots[0][away][0]['B']) + Bh
    Chh = float(teamshots[0][away][0]['C']) + Ch
    Dhh = float(teamshots[0][away][0]['D']) + Dh
    Ehh = float(teamshots[0][away][0]['E']) + Eh
    Fhh = float(teamshots[0][away][0]['F']) + Fh
    Ghh = float(teamshots[0][away][0]['G']) + Gh

    teamshots[0][away][0]['SS'] = SShh
    teamshots[0][away][0]['S'] = Shh
    teamshots[0][away][0]['A'] = Ahh
    teamshots[0][away][0]['B'] = Bhh
    teamshots[0][away][0]['C'] = Chh
    teamshots[0][away][0]['D'] = Dhh
    teamshots[0][away][0]['E'] = Ehh
    teamshots[0][away][0]['F'] = Fhh
    teamshots[0][away][0]['G'] = Ghh

def getcodyceci2(id):
    shift_json = requests.get(constants.SHIFTS_STARTPOINT + id).json()

    #print(shift_json)

    shifts = []
    for item in shift_json["data"]:
        if item["firstName"] == "Kris":
            if item["lastName"] == "Russell":
                shifts.append([item["startTime"], item["endTime"], item["period"]])

    #print(shifts)

    return(shifts)

def extras2():
            Gh = 0
            Fh = 0
            Eh = 0
            Dh = 0
            Ch = 0
            Bh = 0
            Ah = 0
            Sh = 0
            SSh = 0
            thefuckyoumissedmycall = 0
            home_shots = 0

            for item in home_ratings:
                home_shots += 1
                shot_rating = float(item[2])
                if 0 <= shot_rating <= 0.05:
                    #store in F class
                    Gh += 1
                else:
                    if 0.05 < shot_rating <= 0.08:
                        #store in D class
                        Fh += 1
                    else:
                        if 0.08 < shot_rating <= 0.1:
                            #store in C class
                            Eh += 1
                        else:
                            if 0.1 < shot_rating <= 0.12:
                                #store in B class
                                Dh += 1
                            else:
                                if 0.12 < shot_rating <= 0.15:
                                    #store in A class
                                    Ch += 1
                                else:
                                    if 0.15 < shot_rating <= 0.175:
                                        #store in A+ class
                                        Bh += 1
                                    else:
                                        if 0.175 < shot_rating <= 0.2:
                                            #store in S class
                                            Ah += 1
                                        else:
                                            if 0.2 < shot_rating <= 0.25:
                                                #store in S+ class
                                                Sh += 1
                                            else:
                                                if 0.25 < shot_rating:
                                                    SSh += 1
                                                else:
                                                    thefuckyoumissedmycall +=1

            Ga = 0
            Fa = 0
            Ea = 0
            Da = 0
            Ca = 0
            Ba = 0
            Aa = 0
            Sa = 0
            SSa = 0 
            away_shots = 0
            noididnt = 0

            for item in away_ratings:
                away_shots += 1
                shot_rating = float(item[2])
                if 0 <= shot_rating <= 0.05:
                    #store in F class
                    Ga += 1
                else:
                    if 0.05 < shot_rating <= 0.08:
                        #store in D class
                        Fa += 1
                    else:
                        if 0.08 < shot_rating <= 0.1:
                            #store in C class
                            Ea += 1
                        else:
                            if 0.1 < shot_rating <= 0.12:
                                #store in B class
                                Da += 1
                            else:
                                if 0.12 < shot_rating <= 0.15:
                                    #store in A class
                                    Ca += 1
                                else:
                                    if 0.15 < shot_rating <= 0.175:
                                        #store in A+ class
                                        Ba += 1
                                    else:
                                        if 0.175 < shot_rating <= 0.2:
                                            #store in S class
                                            Aa += 1
                                        else:
                                            if 0.2 < shot_rating <= 0.25:
                                                #store in S+ class
                                                Sa += 1
                                            else:
                                                if 0.25 < shot_rating:
                                                    SSa += 1
                                                else:
                                                    noididnt += 1

def getcodyceci(id, playerid, shiftjson):

    #print(shift_json)

    #shift_json = requests.get(constants.SHIFTS_STARTPOINT + id).json()

    team = '0'
    shifts = []
    for item in shiftjson["data"]:
        if item["playerId"] == playerid:
            team = item["teamAbbrev"]
            shifts.append([item["startTime"], item["endTime"], item["period"], item["teamAbbrev"]])
           # print([item["startTime"], item["endTime"], item["period"]])

    #print(shifts)
    #print (team)

    return([shifts, team])

def createcsv(x):

    with open('/Users/samee/Documents/Shot Danger Project/hedman.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        for item in x:
            writer.writerows(item)
    
    csvFile.close()

def read_ratings():

    csv.register_dialect('myDialect',
    delimiter = ',',
    skipinitialspace=True)

    with open('/Users/samee/Documents/Shot Danger Project/ES_pure_shots_2.csv', 'r') as csvFile:
            reader = csv.reader(csvFile, dialect='myDialect')
            for row in reader:
                #print (compiled_info)
                #print("scanning")
                if not row:
                    ripppppcity = 2
                else:
                    location_ratings.append(row)

    csvFile.close()

def shotdatapergameshift(id):
    
    game_json = requests.get(constants.API_URL + constants.GAMES_ENDPOINT + id + constants.FEED_ENDPOINT).json()

    
    away = game_json["gameData"]["teams"]["away"]["abbreviation"]
    home = game_json["gameData"]["teams"]["home"]["abbreviation"]
    
    if away == "EDM" or home == "EDM":

        cody_ceci = getcodyceci2(id)

        #checking when PPGs were
        PPG = []
        for item in game_json["liveData"]["plays"]["allPlays"]:
            if item["result"]["event"] == "Goal":
                if item["result"]["strength"]["code"] == "PPG":
                    timeofgoal = item["about"]["periodTimeRemaining"]
                    period = item["about"]["period"]
                    goalt1 = float(timeofgoal.split(':')[0])
                    goalt2 = float(timeofgoal.split(':')[1])
                    PPG.append([timeofgoal, goalt1, goalt2, period])

        # print(PPG)
        penaltyranges = []

        #creating penalty time ranges
        for item in game_json["liveData"]["plays"]["allPlays"]:
            if item["result"]["event"] == "Penalty":
                if item["result"]["secondaryType"] != "Fighting":

                    if item["result"]["penaltySeverity"] == "Major":
                        time = item["about"]["periodTimeRemaining"]
                        floattime1 = float(time.split(':')[0])

                        if floattime1 < 5:

                            eop = 4 - floattime1

                            nextperiod = item["about"]["period"] + 1
                            time2 = "0"+(str(19 - eop)).split('.')[0] + ":" + time.split(":")[1]
                            penaltyranges.append(["20:00", time2, nextperiod])

                        else:
                            secondtime = "0"+(str(floattime1 - 5)).split('.')[0] + ":" + time.split(':')[1]
                            penaltyranges.append([time, secondtime, item["about"]["period"]])
                            #print(penaltyranges)

                    if item["result"]["penaltySeverity"] == "Minor":
                        time = item["about"]["periodTimeRemaining"]
                        time1 = float(time.split(':')[0])
                        time2 = float(time.split(':')[1])
                        period = item["about"]["period"]

                        if time1 < 2:
                            eop = 0
                            penb4end = 0

                            for goal in PPG:
                                if goal[3] == period:
                                    if eop <= goal[1] <= time1:
                                        if goal[1] == time1:
                                            if goal[2] <= time2:
                                                penaltyranges.append([time, goal[0], period])
                                                penb4end = 1
                                        else:
                                            if goal[1] == eop:
                                                if goal[2] >= time2:
                                                    penaltyranges.append([time, goal[0], period])
                                                    penb4end = 1
                                            else:
                                                penaltyranges.append([time, goal[0], period])
                                                penb4end = 1

                            if penb4end != 1:
                                #print(time)
                                penaltyranges.append([time, "00:00", period])
                                timep2 = "20:00"

                                nextperiod = period+1

                                eop2 = 1 - time1

                                eopp = 19 - eop2
                                
                                penb4end2 = 0

                                for goal in PPG:
                                    if goal[3] == nextperiod:
                                        if eopp <= goal[1] <= 20:
                                            if goal[1] == eopp:
                                                if goal[2] >= time2:
                                                    penaltyranges.append([timep2, goal[0], nextperiod])
                                                    penb4end2 = 1
                                            else:
                                                penaltyranges.append([timep2, goal[0], nextperiod])
                                                penb4end2 = 1
                                
                                if penb4end2 != 1:
                                    penaltytimeleft = 1 - time1
                                    endofpenalty = (str(19-penaltytimeleft)).split('.')[0] + ":" + time.split(':')[1]
                                    penaltyranges.append(["20:00", endofpenalty, nextperiod])


                        

                        #make exception for double minors fuck

                        #print(time + " - " + str(eop))
                        else:
                            eop = time1 - 2
                            wasthereagoal = 0
                            for goal in PPG:
                                if goal[3] == period:
                                    if eop <= goal[1] <= time1:
                                        if goal[1] == time1:
                                            if goal[2] <= time2:
                                                penaltyranges.append([time, goal[0], period])
                                                wasthereagoal = 1
                                        else:
                                            if goal[1] == eop:
                                                if goal[2] >= time2:
                                                    penaltyranges.append([time, goal[0], period])
                                                    wasthereagoal = 1
                                            else:
                                                penaltyranges.append([time, goal[0], period])
                                                wasthereagoal = 1
                            
                            if wasthereagoal != 1:
                                eop = (str(time1 - 2)).split('.')[0] + ":" + time.split(':')[1]
                                penaltyranges.append([time, eop, period])

        #print (penaltyranges)

        #reading shots
        game_data = []
        for item in game_json["liveData"]["plays"]["allPlays"]:
            if "x" in item["coordinates"]:
                if "y" in item["coordinates"]:
                    if item["result"]["event"] == "Shot":
                        teamshooting = item["team"]["triCode"]
                        x = abs(item["coordinates"]["x"])
                        y = item["coordinates"]["y"]
                        result = "shot"
                        period = item["about"]["period"]
                        tos = item["about"]["periodTimeRemaining"]
                        tos1 = float(tos.split(':')[0])
                        tos2 = float(tos.split(':')[1])

                        tpp = item["about"]["periodTime"]
                        tpp1 = float(tpp.split(':')[0])
                        tpp2 = float(tpp.split(':')[1])

                        evenstrength = 0

                        for item in penaltyranges:
                            if item[2] == period:
                                PPstart1 = float(item[0].split(':')[0])
                                PPstart2 = float(item[0].split(':')[1])
                                PPend1 = float(item[1].split(':')[0])
                                PPend2 = float(item[1].split(':')[1])


                                if PPend1 <= tos1 <=PPstart1:
                                    if PPstart1 == tos1:
                                        if tos2 <= PPstart2:
                                            #strength = "uneven"
                                            evenstrength = 1
                                    else:
                                        if PPend1 == tos1:
                                            if tos2 >= PPend2:
                                                #strength = "uneven"
                                                evenstrength = 1
                                        else:
                                            #strength = "uneven"
                                            evenstrength = 1

                        if evenstrength == 1:
                            strength = "uneven"

                        else:
                            on_ice = 0
                            for item in cody_ceci:
                                if item[2] == period:
                                    shiftstart1 = float(item[0].split(':')[0])
                                    shiftstart2 = float(item[0].split(':')[1])
                                    shiftend1 = float(item[1].split(':')[0])
                                    shiftend2 = float(item[1].split(':')[1])    

                                    if shiftend1 >= tpp1 >= shiftstart1:
                                        if shiftstart1 == tpp1:
                                            if tpp2 >= shiftstart2:
                                                on_ice = 1
                                        else:
                                            if shiftend1 == tpp1:
                                                if tpp2 <= shiftend2:
                                                    on_ice = 1
                                            else:
                                                on_ice = 1

                            if on_ice == 1:
                                strength = "even"
                                game_data.append([(str(x)), (str(y)), teamshooting, result, strength])

                        #for item in penaltyranges:

                    else:
                        if item["result"]["event"] == "Goal":
                            x = abs(item["coordinates"]["x"])
                            y = item["coordinates"]["y"]
                            teamshooting = item["team"]["triCode"]
                            result = "goal"
                            strength = item["result"]["strength"]["name"]
                            tos = item["about"]["periodTimeRemaining"]
                            tos1 = float(tos.split(':')[0])
                            tos2 = float(tos.split(':')[1])

                            tpp = item["about"]["periodTime"]
                            tpp1 = float(tpp.split(':')[0])
                            tpp2 = float(tpp.split(':')[1])
                            if strength == "Even": 
                                on_ice = 0
                                for item in cody_ceci:
                                    if item[2] == period:
                                        shiftstart1 = float(item[0].split(':')[0])
                                        shiftstart2 = float(item[0].split(':')[1])
                                        shiftend1 = float(item[1].split(':')[0])
                                        shiftend2 = float(item[1].split(':')[1])

                                        if shiftend1 >= tpp1 >= shiftstart1:
                                            if shiftstart1 == tpp1:
                                                if tpp2 >= shiftstart2:
                                                    on_ice = 1
                                            else:
                                                if shiftend1 == tpp1:
                                                    if tpp2 <= shiftend2:
                                                        on_ice = 1
                                                else:
                                                    on_ice = 1

                                if on_ice == 1:
                                    strength = "even"
                                    game_data.append([(str(x)), (str(y)), teamshooting, result, strength])
                        else:
                            if item["result"]["event"] == "Missed Shot":
                                x = abs(item["coordinates"]["x"])
                                y = item["coordinates"]["y"]
                                result = "shot"
                                period = item["about"]["period"]
                                tos = item["about"]["periodTimeRemaining"]
                                teamshooting = item["team"]["triCode"]
                                tos1 = float(tos.split(':')[0])
                                tos2 = float(tos.split(':')[1])

                                tpp = item["about"]["periodTime"]
                                tpp1 = float(tpp.split(':')[0])
                                tpp2 = float(tpp.split(':')[1])

                                evenstrength = 0

                                for item in penaltyranges:
                                    if item[2] == period:
                                        PPstart1 = float(item[0].split(':')[0])
                                        PPstart2 = float(item[0].split(':')[1])
                                        PPend1 = float(item[1].split(':')[0])
                                        PPend2 = float(item[1].split(':')[1])


                                        if PPend1 <= tos1 <=PPstart1:
                                            if PPstart1 == tos1:
                                                if tos2 <= PPstart2:
                                                    #strength = "uneven"
                                                    evenstrength = 1
                                            else:
                                                if PPend1 == tos1:
                                                    if tos2 >= PPend2:
                                                        #strength = "uneven"
                                                        evenstrength = 1
                                                else:
                                                    #strength = "uneven"
                                                    evenstrength = 1

                                if evenstrength == 1:
                                    strength = "uneven"

                                else:
                                    on_ice = 0
                                    for item in cody_ceci:
                                        if item[2] == period:
                                            shiftstart1 = float(item[0].split(':')[0])
                                            shiftstart2 = float(item[0].split(':')[1])
                                            shiftend1 = float(item[1].split(':')[0])
                                            shiftend2 = float(item[1].split(':')[1])

                                            if shiftend1 >= tpp1 >= shiftstart1:
                                                if shiftstart1 == tpp1:
                                                    if tpp2 >= shiftstart2:
                                                        on_ice = 1
                                                else:
                                                    if shiftend1 == tpp1:
                                                        if tpp2 <= shiftend2:
                                                            on_ice = 1
                                                    else:
                                                        on_ice = 1

                                    if on_ice == 1:
                                        strength = "even"
                                        game_data.append([(str(x)), (str(y)), teamshooting, result, strength])

        #print(game_data)

        away_ratings = []
        home_ratings = []

        print(id)
        for row in location_ratings:    
            for item in game_data:
                #if item[3] == "goal":
                if item[0] == (row[0]+'.0'):
                    if item[1] == (row[1]+'.0'):
                        #print(item)
                        #print(row[7])
                        if item[2] == home:
                            home_ratings.append([item[0], item[1], row[6]])
                        else:
                            away_ratings.append([item[0], item[1], row[6]])
        
        Gh = 0
        Fh = 0
        Eh = 0
        Dh = 0
        Ch = 0
        Bh = 0
        Ah = 0
        Sh = 0
        SSh = 0
        thefuckyoumissedmycall = 0
        home_shots = 0

        for item in home_ratings:
            home_shots += 1
            shot_rating = float(item[2])
            if 0 <= shot_rating <= 0.05:
                #store in F class
                Gh += 1
            else:
                if 0.05 < shot_rating <= 0.08:
                    #store in D class
                    Fh += 1
                else:
                    if 0.08 < shot_rating <= 0.1:
                        #store in C class
                        Eh += 1
                    else:
                        if 0.1 < shot_rating <= 0.12:
                            #store in B class
                            Dh += 1
                        else:
                            if 0.12 < shot_rating <= 0.15:
                                #store in A class
                                Ch += 1
                            else:
                                if 0.15 < shot_rating <= 0.175:
                                    #store in A+ class
                                    Bh += 1
                                else:
                                    if 0.175 < shot_rating <= 0.2:
                                        #store in S class
                                        Ah += 1
                                    else:
                                        if 0.2 < shot_rating <= 0.25:
                                            #store in S+ class
                                            Sh += 1
                                        else:
                                            #if 0.25 < shot_rating:
                                                #SSh += 1
                                            #else:
                                            thefuckyoumissedmycall +=1


        Ga = 0
        Fa = 0
        Ea = 0
        Da = 0
        Ca = 0
        Ba = 0
        Aa = 0
        Sa = 0
        SSa = 0 
        away_shots = 0
        noididnt = 0

        for item in away_ratings:
            away_shots += 1
            shot_rating = float(item[2])
            if 0 <= shot_rating <= 0.05:
                #store in F class
                Ga += 1
            else:
                if 0.05 < shot_rating <= 0.08:
                    #store in D class
                    Fa += 1
                else:
                    if 0.08 < shot_rating <= 0.1:
                        #store in C class
                        Ea += 1
                    else:
                        if 0.1 < shot_rating <= 0.12:
                            #store in B class
                            Da += 1
                        else:
                            if 0.12 < shot_rating <= 0.15:
                                #store in A class
                                Ca += 1
                            else:
                                if 0.15 < shot_rating <= 0.175:
                                    #store in A+ class
                                    Ba += 1
                                else:
                                    if 0.175 < shot_rating <= 0.2:
                                        #store in S class
                                        Aa += 1
                                    else:
                                        if 0.2 < shot_rating <= 0.25:
                                            #store in S+ class
                                            Sa += 1
                                        else:
                                            #if 0.25 < shot_rating:
                                                #SSa += 1
                                            #else:
                                            noididnt += 1
        
        if home == "EDM":
            OTT.append([Ga, Fa, Ea, Da, Ca, Ba, Aa, Sa, noididnt, away_shots])
        else:
            if away == "EDM":
                OTT.append([Gh, Fh, Eh, Dh, Ch, Bh, Ah, Sh, thefuckyoumissedmycall, home_shots])
    
def garbage():
    print()
    #print(home)
        #print(home_ratings)
        #print(away_ratings)


        #home_total = 0
        #home_shots = 0
        #for item in home_ratings:
           # home_total += float(item[2])
           # home_shots += 1

       # away_total = 0
       # away_shots = 0
       # for item in away_ratings:
      #     away_total += float(item[2])
       #     away_shots += 1
        
      #  print(home_total)
      #  print(home_shots)

      #  print(away_total)
      #  print(away_shots)

       # if away == "TBL":
      #      OTT.append(home_total)
      #      cecishots.append(home_shots)
       # else:
        #    if home == "TBL":
       #         OTT.append(away_total)
        #        cecishots.append(away_shots)


def extras():
    
    #delet
    if away == "OTT" or home == "OTT":
        print(id)
        #checking when PPGs were
        PPG = []
        for item in game_json["liveData"]["plays"]["allPlays"]:
            if item["result"]["event"] == "Goal":
                if item["result"]["strength"]["code"] == "PPG":
                    timeofgoal = item["about"]["periodTimeRemaining"]
                    period = item["about"]["period"]
                    goalt1 = float(timeofgoal.split(':')[0])
                    goalt2 = float(timeofgoal.split(':')[1])
                    PPG.append([timeofgoal, goalt1, goalt2, period])

        # print(PPG)
        penaltyranges = []

        #creating penalty time ranges
        for item in game_json["liveData"]["plays"]["allPlays"]:
            if item["result"]["event"] == "Penalty":
                if item["result"]["secondaryType"] != "Fighting":

                    if item["result"]["penaltySeverity"] == "Major":
                        time = item["about"]["periodTimeRemaining"]
                        floattime1 = float(time.split(':')[0])

                        if floattime1 < 5:

                            eop = 4 - floattime1

                            nextperiod = item["about"]["period"] + 1
                            time2 = "0"+(str(19 - eop)).split('.')[0] + ":" + time.split(":")[1]
                            penaltyranges.append(["20:00", time2, nextperiod])

                        else:
                            secondtime = "0"+(str(floattime1 - 5)).split('.')[0] + ":" + time.split(':')[1]
                            penaltyranges.append([time, secondtime, item["about"]["period"]])
                            #print(penaltyranges)

                    if item["result"]["penaltySeverity"] == "Minor":
                        time = item["about"]["periodTimeRemaining"]
                        time1 = float(time.split(':')[0])
                        time2 = float(time.split(':')[1])
                        period = item["about"]["period"]

                        if time1 < 2:
                            eop = 0
                            penb4end = 0

                            for goal in PPG:
                                if goal[3] == period:
                                    if eop <= goal[1] <= time1:
                                        if goal[1] == time1:
                                            if goal[2] <= time2:
                                                penaltyranges.append([time, goal[0], period])
                                                penb4end = 1
                                        else:
                                            if goal[1] == eop:
                                                if goal[2] >= time2:
                                                    penaltyranges.append([time, goal[0], period])
                                                    penb4end = 1
                                            else:
                                                penaltyranges.append([time, goal[0], period])
                                                penb4end = 1

                            if penb4end != 1:
                                #print(time)
                                penaltyranges.append([time, "00:00", period])
                                timep2 = "20:00"

                                nextperiod = period+1

                                eop2 = 1 - time1

                                eopp = 19 - eop2
                                
                                penb4end2 = 0

                                for goal in PPG:
                                    if goal[3] == nextperiod:
                                        if eopp <= goal[1] <= 20:
                                            if goal[1] == eopp:
                                                if goal[2] >= time2:
                                                    penaltyranges.append([timep2, goal[0], nextperiod])
                                                    penb4end2 = 1
                                            else:
                                                penaltyranges.append([timep2, goal[0], nextperiod])
                                                penb4end2 = 1
                                
                                if penb4end2 != 1:
                                    penaltytimeleft = 1 - time1
                                    endofpenalty = (str(19-penaltytimeleft)).split('.')[0] + ":" + time.split(':')[1]
                                    penaltyranges.append(["20:00", endofpenalty, nextperiod])


                        

                        #make exception for double minors fuck

                        #print(time + " - " + str(eop))
                        else:
                            eop = time1 - 2
                            wasthereagoal = 0
                            for goal in PPG:
                                if goal[3] == period:
                                    if eop <= goal[1] <= time1:
                                        if goal[1] == time1:
                                            if goal[2] <= time2:
                                                penaltyranges.append([time, goal[0], period])
                                                wasthereagoal = 1
                                        else:
                                            if goal[1] == eop:
                                                if goal[2] >= time2:
                                                    penaltyranges.append([time, goal[0], period])
                                                    wasthereagoal = 1
                                            else:
                                                penaltyranges.append([time, goal[0], period])
                                                wasthereagoal = 1
                            
                            if wasthereagoal != 1:
                                eop = (str(time1 - 2)).split('.')[0] + ":" + time.split(':')[1]
                                penaltyranges.append([time, eop, period])

        #print (penaltyranges)

        #reading shots
        game_data = []
        for item in game_json["liveData"]["plays"]["allPlays"]:
            if "x" in item["coordinates"]:
                if "y" in item["coordinates"]:
                    if item["result"]["event"] == "Shot":
                        teamshooting = item["team"]["triCode"]
                        x = abs(item["coordinates"]["x"])
                        y = item["coordinates"]["y"]
                        result = "shot"
                        period = item["about"]["period"]
                        tos = item["about"]["periodTimeRemaining"]
                        tos1 = float(tos.split(':')[0])
                        tos2 = float(tos.split(':')[1])

                        tpp = item["about"]["periodTime"]
                        tpp1 = float(tpp.split(':')[0])
                        tpp2 = float(tpp.split(':')[1])

                        evenstrength = 0

                        for item in penaltyranges:
                            if item[2] == period:
                                PPstart1 = float(item[0].split(':')[0])
                                PPstart2 = float(item[0].split(':')[1])
                                PPend1 = float(item[1].split(':')[0])
                                PPend2 = float(item[1].split(':')[1])


                                if PPend1 <= tos1 <=PPstart1:
                                    if PPstart1 == tos1:
                                        if tos2 <= PPstart2:
                                            #strength = "uneven"
                                            evenstrength = 1
                                    else:
                                        if PPend1 == tos1:
                                            if tos2 >= PPend2:
                                                #strength = "uneven"
                                                evenstrength = 1
                                        else:
                                            #strength = "uneven"
                                            evenstrength = 1

                        if evenstrength == 1:
                            strength = "uneven"

                        else:
                            strength = "even"
                            game_data.append([(str(x)), (str(y)), teamshooting, result, strength, tpp, period])

                        #for item in penaltyranges:

                    else:
                        if item["result"]["event"] == "Goal":
                            x = abs(item["coordinates"]["x"])
                            y = item["coordinates"]["y"]
                            teamshooting = item["team"]["triCode"]
                            result = "goal"
                            strength = item["result"]["strength"]["name"]
                            tos = item["about"]["periodTimeRemaining"]
                            tos1 = float(tos.split(':')[0])
                            tos2 = float(tos.split(':')[1])

                            tpp = item["about"]["periodTime"]
                            tpp1 = float(tpp.split(':')[0])
                            tpp2 = float(tpp.split(':')[1])
                            if strength == "Even": 
                                strength = "even"
                                game_data.append([(str(x)), (str(y)), teamshooting, result, strength, tpp, period])
                        else:
                            if item["result"]["event"] == "Missed Shot":
                                x = abs(item["coordinates"]["x"])
                                y = item["coordinates"]["y"]
                                result = "shot"
                                period = item["about"]["period"]
                                tos = item["about"]["periodTimeRemaining"]
                                teamshooting = item["team"]["triCode"]
                                tos1 = float(tos.split(':')[0])
                                tos2 = float(tos.split(':')[1])

                                tpp = item["about"]["periodTime"]
                                tpp1 = float(tpp.split(':')[0])
                                tpp2 = float(tpp.split(':')[1])

                                evenstrength = 0

                                for item in penaltyranges:
                                    if item[2] == period:
                                        PPstart1 = float(item[0].split(':')[0])
                                        PPstart2 = float(item[0].split(':')[1])
                                        PPend1 = float(item[1].split(':')[0])
                                        PPend2 = float(item[1].split(':')[1])


                                        if PPend1 <= tos1 <=PPstart1:
                                            if PPstart1 == tos1:
                                                if tos2 <= PPstart2:
                                                    #strength = "uneven"
                                                    evenstrength = 1
                                            else:
                                                if PPend1 == tos1:
                                                    if tos2 >= PPend2:
                                                        #strength = "uneven"
                                                        evenstrength = 1
                                                else:
                                                    #strength = "uneven"
                                                    evenstrength = 1

                                if evenstrength == 1:
                                    strength = "uneven"

                                else:
                                    strength = "even"
                                    game_data.append([(str(x)), (str(y)), teamshooting, result, strength, tpp, period])

        for player in game_json["gameData"]["players"]:
            playerid = game_json["gameData"]["players"][player]['id']
            if game_json["gameData"]["players"][player]["primaryPosition"]["type"] != "Goalie":
                if playerid == 8476879:
                
                    shifts = getcodyceci(id, playerid, shift_json)
                    shot_data = []

                    
                    if str(playerid) in playershots[0]:
                        yay = 1
                    else:
                        #if away == "OTT" or home == 'OTT':
                            #if shifts[1] == "OTT":
                        playershots[0][str(playerid)] = [{'SS' : 0, 'S': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F' : 0, 'G' : 0}]
                        print("ayomyn")

                    for item in game_data:
                        if item[2] != shifts[1]:
                            period = item[6]
                            timeofevent = item[5]
                            toe1 = float(timeofevent.split(':')[0])
                            toe2 = float(timeofevent.split(':')[1])
                            x = item[0]
                            y = item[1]
                            
                            on_ice = 0
                            for shift in shifts[0]:
                                #if shift[3] != shift[3]:
                                if shift[2] == period:
                                    shiftstart1 = float(shift[0].split(':')[0])
                                    shiftstart2 = float(shift[0].split(':')[1])
                                    shiftend1 = float(shift[1].split(':')[0])
                                    shiftend2 = float(shift[1].split(':')[1])    

                                    if shiftend1 >= toe1 >= shiftstart1:
                                        if shiftstart1 == tpp1:
                                            if toe2 >= shiftstart2:
                                                on_ice = 1
                                        else:
                                            if shiftend1 == toe1:
                                                if toe2 <= shiftend2:
                                                    on_ice = 1
                                            else:
                                                on_ice = 1

                            if on_ice == 1:
                                shot_data.append([x, y])

                    print(playerid)
                    print(shot_data)

                    ratings = []
                    for row in location_ratings:    
                        for item in shot_data:
                            #if item[3] == "goal":
                            if item[0] == (row[0]+'.0'):
                                if item[1] == (row[1]+'.0'):
                                    ratings.append(row[6])
                                    #print (ratings)

                    print (ratings)

                    #print (playershots[0][stringid]['ss'])

                    stringid = str(playerid)

                    #print (playershots[0][stringid])

                    #print(ratings)
                    SS = float(playershots[0][stringid][0]['SS'])
                    S = float(playershots[0][stringid][0]['S'])
                    A = float(playershots[0][stringid][0]['A'])
                    B = float(playershots[0][stringid][0]['B'])
                    C = float(playershots[0][stringid][0]['C'])
                    D = float(playershots[0][stringid][0]['D'])
                    E = float(playershots[0][stringid][0]['E'])
                    F = float(playershots[0][stringid][0]['F'])
                    G = float(playershots[0][stringid][0]['G'])

                    for shottaken in ratings:
                        #home_shots += 1
                        shot_rating = float(shottaken)
                        print (shot_rating)
                        if 0 <= shot_rating <= 0.05:
                            G += 1
                        else:
                            if 0.05 < shot_rating <= 0.08:
                                #store in F class
                                F += 1
                            else:
                                if 0.08 < shot_rating <= 0.1:
                                    #store in D class
                                    E += 1
                                else:
                                    if 0.1 < shot_rating <= 0.12:
                                        #store in C class
                                        D += 1
                                    else:
                                        if 0.12 < shot_rating <= 0.15:
                                            #store in B class
                                            C += 1
                                        else:
                                            if 0.15 < shot_rating <= 0.175:
                                                #store in A class
                                                B += 1
                                            else:
                                                if 0.175 < shot_rating <= 0.2:
                                                    #store in A+ class
                                                    A += 1
                                                else:
                                                    if 0.2 < shot_rating <= 0.25:
                                                        #store in S class
                                                        S += 1
                                                    else:
                                                        if 0.25 < shot_rating:
                                                            #store in S+ class
                                                            SS += 1

                    #print(F)
                    playershots[0][stringid][0]['SS'] = SS
                    playershots[0][stringid][0]['S'] = S
                    playershots[0][stringid][0]['A'] = A
                    playershots[0][stringid][0]['B'] = B
                    playershots[0][stringid][0]['C'] = C
                    playershots[0][stringid][0]['D'] = D
                    playershots[0][stringid][0]['E'] = E
                    playershots[0][stringid][0]['F'] = F
                    playershots[0][stringid][0]['G'] = G

                    print (playershots[0][stringid])

                    


                    #[(str(x)), (str(y)), teamshooting, result, strength, tpp, period])


if __name__ == '__main__':
    main()