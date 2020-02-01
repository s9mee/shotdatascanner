import json
import requests
import constants
import csv

def mai4n():
    getplayers("OTT")

def main():

    csv.register_dialect('myDialect',
    delimiter = ',',
    skipinitialspace=True)

    with open('/Users/samee/Documents/Shot Danger Project/pure_shot_data/per20teamspureshots.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, dialect='myDialect')
        for row in reader:
            if not row:
                e = 1
            else:
                if row[0] != 'team':
                    f = open('/Users/samee/Documents/Shot Danger Project/pure_shot_data/teamshtml/'+row[0]+'.html','w')

                    SS = '<td>'+str(round(float(row[1]), 3))+'</td>'
                    S = '<td>'+str(round(float(row[2]), 3))+'</td>'
                    A = '<td>'+str(round(float(row[3]), 3))+'</td>'
                    B = '<td>'+str(round(float(row[4]), 3))+'</td>'
                    C = '<td>'+str(round(float(row[5]), 3))+'</td>'
                    D = '<td>'+str(round(float(row[6]), 3))+'</td>'
                    E = '<td>'+str(round(float(row[7]), 3))+'</td>'
                    F = '<td>'+str(round(float(row[8]), 3))+'</td>'
                    

                    opening = """
                    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
                    "http://www.w3.org/TR/html4/strict.dtd">
                    <html>
                    <head>
                    <title>""" + row[0] + """</title>
                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css" />

                    <link rel="stylesheet" href="https://drvic10k.github.io/bootstrap-sortable/Contents/bootstrap-sortable.css" />
                  
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.js"></script>
                  
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
                  
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.19.1/moment.js"></script>
                  
                    <script src="https://drvic10k.github.io/bootstrap-sortable/Scripts/bootstrap-sortable.js"></script>
                  
                    <link href="//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css" rel="stylesheet">
                    </head>
                    <body>
                    <h1>""" + row[0] + """</h1>
                    </br>
                    <table>
                    <tr><td>S+ shots/20</td><td>S shots/20</td><td>A shots/20</td><td>B shots/20</td><td>C shots/20</td><td>D shots/20</td><td>E shots/20</td><td>F shots/20</td><td></tr>
                    <tr>""" + SS + S + A + B + C + D + E + F + """</tr>
                    </table>
                    </br>
                    """

                    closing = """
                    </body>
                    </html>
                    """

                    players = getplayers(row)

                    html = opening+players+closing

                    f.write(html)
                    f.close()
    
    csvFile.close()


def getplayers(teamdata):

    csv.register_dialect('myDialect',
    delimiter = ',',
    skipinitialspace=True)

    players = []
    with open('/Users/samee/Documents/Shot Danger Project/pure_shot_data/per20playerspureshotsteams.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, dialect='myDialect')
        for row in reader:
            if not row:
                e = 1
            else:
                for item in row:
                    if teamdata[0] in item:
                        players.append(row)

    tablestart = """<table class="table table-bordered sortable">
                        <thead>
                            <tr><th>Player Name</th><th>Position</th><th>S+ shots/20 REL</th><th>S shots/20 REL</th><th>A shots/20 REL</th><th>B shots/20 REL</th><th>C shots/20 REL</th><th>D shots/20 REL</th><th>E shots/20 REL</th><th>F shots/20 REL</th></tr>
                        </thead>
                        <tbody id="myTable">
    """
    tableforwards = ''
    tabledefense = ''
    tableend = """
                        </tbody></table>"""

    for row in players:
        name = getplayername(row[0])
        SSr = '<td>'+str(round((float(row[1]) - float(teamdata[1])), 3))+'</td>'
        Sr = '<td>'+str(round((float(row[2]) - float(teamdata[2])), 3))+'</td>'
        Ar = '<td>'+str(round((float(row[3]) - float(teamdata[3])), 3))+'</td>'
        Br = '<td>'+str(round((float(row[4]) - float(teamdata[4])), 3))+'</td>'
        Cr = '<td>'+str(round((float(row[5]) - float(teamdata[5])), 3))+'</td>'
        Dr = '<td>'+str(round((float(row[6]) - float(teamdata[6])), 3))+'</td>'
        Er = '<td>'+str(round((float(row[7]) - float(teamdata[7])), 3))+'</td>'
        Fr = '<td>'+str(round((float(row[8]) - float(teamdata[8])), 3))+'</td>'

        if name[2] == 'D':
            tabledefense += """ 
                                <tr>""" + ('<td>' + name[0] + ' ' + name[1] + '</td>') + '<td>' + name[2] + '</td>' + SSr +Sr + Ar + Br + Cr + Dr + Er + Fr + """</tr>"""
        else:
            tableforwards += """ 
                                <tr>""" + ('<td>' + name[0] + ' ' + name[1] + '</td>') + '<td>' + name[2] + '</td>' + SSr +Sr + Ar + Br + Cr + Dr + Er + Fr + """</tr>"""
        

    fulltable = """
    </br>
    <h2>Defensemen</h2>
    """ +tablestart+tabledefense+tableend + """
    </br>
    <h2>Forwards</h2>
    """+tablestart+tableforwards+tableend

    csvFile.close()

    return fulltable

   # print(players)

                        
def getplayername(id):
    playerinfo = requests.get(constants.API_URL + constants.PEOPLE_ENDPOINT + str(id)).json()
    #print(id)

    firstname = playerinfo["people"][0]["firstName"]
    lastname = playerinfo["people"][0]["lastName"]
    position = playerinfo["people"][0]["primaryPosition"]["code"]

    name = [firstname, lastname, position]

    return name

if __name__ == '__main__':
    main()
