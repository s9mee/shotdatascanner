import json
import requests
import constants
import csv

def main():
    shot_info = [["X", "Y", "Result", "Strength"]]

    #create array list containing shot information
    for x in range(2017020001, 2017021271):

        game_id = str (x)
        game_info = getGameInfo(game_id)

        for item in game_info:
            shot_info.append(item)

        print(x)

    for x in range(2018020001, 2018021271):

        game_id = str (x)
        game_info = getGameInfo(game_id)

        for item in game_info:
            shot_info.append(item)

        print(x)

    for x in range(2016020001, 2016021230):

        game_id = str (x)
        game_info = getGameInfo(game_id)

        for item in game_info:
            shot_info.append(item)

        print(x)
    
    for x in range(2015020001, 2015021230):

        game_id = str (x)
        game_info = getGameInfo(game_id)

        for item in game_info:
            shot_info.append(item)

        print(x)

    for x in range(2014020001, 2014021230):

        game_id = str (x)
        game_info = getGameInfo(game_id)

        for item in game_info:
            shot_info.append(item)

        print(x)

    #writes the array into a csv file.
    with open('/Users/samee/Documents/Shot Danger Project/shots_data.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(shot_info)
    
    csvFile.close()

def main2():
    shot_info = []
    #getGameInfo("2016020180")
    #getGameInfo('2018030187')
    #getGameInfo('2016020145')
    #getGameInfo('2018020394')
    getGameInfo('2016020154')

#gets information for shots in a game
def getGameInfo(id):
    for x in range (1, 3):
        try:
            game_json = requests.get(constants.API_URL + constants.GAMES_ENDPOINT + id + constants.FEED_ENDPOINT).json()
            #game_json = json.loads(game.text)
            game_list = []
            x = 4
        except:
            x = 2


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

    for item in game_json["liveData"]["plays"]["allPlays"]:
        if "x" in item["coordinates"]:
            if "y" in item["coordinates"]:
                if item["result"]["event"] == "Shot":
                    x = abs(item["coordinates"]["x"])
                    y = item["coordinates"]["y"]
                    result = "shot"
                    period = item["about"]["period"]
                    tos = item["about"]["periodTimeRemaining"]
                    tos1 = float(tos.split(':')[0])
                    tos2 = float(tos.split(':')[1])

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
                        game_list.append([x, y, result, strength])

                    else:
                        strength = "even"
                        game_list.append([x, y, result, strength])

                    #for item in penaltyranges:

                else:
                    if item["result"]["event"] == "Goal":
                        x = abs(item["coordinates"]["x"])
                        y = item["coordinates"]["y"]
                        result = "goal"
                        strength = item["result"]["strength"]["name"]
                        game_list.append([x, y, result, strength])
                    else:
                        if item["result"]["event"] == "Missed Shot":
                            x = abs(item["coordinates"]["x"])
                            y = item["coordinates"]["y"]
                            result = "shot"
                            period = item["about"]["period"]
                            tos = item["about"]["periodTimeRemaining"]
                            tos1 = float(tos.split(':')[0])
                            tos2 = float(tos.split(':')[1])

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
                                game_list.append([x, y, result, strength])

                            else:
                                strength = "even"
                                game_list.append([x, y, result, strength])
    
    #print (game_list)
    return game_list

#def evenstrength(penalties, shottime):


if __name__ == '__main__':
    main()