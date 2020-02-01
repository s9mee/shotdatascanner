import json
import requests
import constants
import csv

def ma2in():
    print(getteamdata("OTT"))

def main():

    csv.register_dialect('myDialect',
    delimiter = ',',
    skipinitialspace=True)

    with open('/Users/samee/Documents/Shot Danger Project/pure_shot_data/per20playerspureshotsteams.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, dialect='myDialect')
        for row in reader:
            if not row:
                e = 1
            else:
                if row[0] != "playerid":
                    name = getplayername(row[0])
                    teams = []

                    statsrelative = []

                    for item in row:
                        len(item)
                        
                        if '.' not in item:
                            if len(item) == 3:
                                if '0' not in item:
                                    teams.append(item)

                    for team in teams:
                       # print(team)
                        teamdata = getteamdata(team)
                        Ssrel = str(round((float(row[1]) - float(teamdata[1])), 3))
                        Srel = str(round((float(row[2]) - float(teamdata[2])), 3))
                        Arel = str(round((float(row[3]) - float(teamdata[3])), 3))
                        Brel = str(round((float(row[4]) - float(teamdata[4])), 3))
                        Crel = str(round((float(row[5]) - float(teamdata[5])), 3))
                        Drel = str(round((float(row[6]) - float(teamdata[6])), 3))
                        Erel = str(round((float(row[7]) - float(teamdata[7])), 3))
                        Frel = str(round((float(row[8]) - float(teamdata[8])), 3))

                        statsrelative.append([teamdata[0], Ssrel, Srel, Arel, Brel, Crel, Drel, Erel, Frel])
                        
                    f = open('/Users/samee/Documents/Shot Danger Project/pure_shot_data/html/'+name[0]+'_'+name[1]+'.html','w')

                    SS = '<td>'+str(round(float(row[1]), 3))+'</td>'
                    S = '<td>'+str(round(float(row[2]), 3))+'</td>'
                    A = '<td>'+str(round(float(row[3]), 3))+'</td>'
                    B = '<td>'+str(round(float(row[4]), 3))+'</td>'
                    C = '<td>'+str(round(float(row[5]), 3))+'</td>'
                    D = '<td>'+str(round(float(row[6]), 3))+'</td>'
                    E = '<td>'+str(round(float(row[7]), 3))+'</td>'
                    F = '<td>'+str(round(float(row[8]), 3))+'</td>'
                    

                    opening = """
                    <html>
                    <head>
                    <title>""" + name[0] + ' ' + name[1] + """</title>
                    </head>
                    <body>
                    <h1>""" + name[0] + ' ' + name[1] + """</h1>
                    </br>
                    <table>
                    <tr><td>S+ shots/20</td><td>S shots/20</td><td>A shots/20</td><td>B shots/20</td><td>C shots/20</td><td>D shots/20</td><td>E shots/20</td><td>F shots/20</td><td></tr>
                    <tr>""" + SS + S + A + B + C + D + E + F + """</tr>
                    </table>
                    """

                    closing = """
                    </body>
                    </html>
                    """

                    middle = ''
                    for data in statsrelative:

                        SSr = '<td>'+data[1]+'</td>'
                        Sr = '<td>'+data[2]+'</td>'
                        Ar = '<td>'+data[3]+'</td>'
                        Br = '<td>'+data[4]+'</td>'
                        Cr = '<td>'+data[5]+'</td>'
                        Dr = '<td>'+data[6]+'</td>'
                        Er = '<td>'+data[7]+'</td>'
                        Fr = '<td>'+data[8]+'</td>'

                        middle += """
                        </br>
                        </br>
                        <h2>"""+data[0]+"""
                        <table>
                        <tr><td>S+ shots/20 REL</td><td>S shots/20 REL</td><td>A shots/20 REL</td><td>B shots/20 REL</td><td>C shots/20 REL</td><td>D shots/20 REL</td><td>E shots/20 REL</td><td>F shots/20 REL</td><td></tr>
                        <tr>""" + SSr +Sr + Ar + Br + Cr + Dr + Er + Fr + """</tr>
                        </table>
                        """
                    
                    html = opening+middle+closing
                    
                    f.write(html)
                    f.close()

    csvFile.close()

def getplayername(id):
    playerinfo = requests.get(constants.API_URL + constants.PEOPLE_ENDPOINT + str(id)).json()
    print(id)

    firstname = playerinfo["people"][0]["firstName"]
    lastname = playerinfo["people"][0]["lastName"]

    name = [firstname, lastname]

    return name

def getteamdata(team):
    data = []
    csv.register_dialect('myDialect',
    delimiter = ',',
    skipinitialspace=True)

    with open('/Users/samee/Documents/Shot Danger Project/pure_shot_data/per20teamspureshots.csv', 'r') as csvFile:
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

    print(data)

    return(data)


    

if __name__ == '__main__':
    main()


