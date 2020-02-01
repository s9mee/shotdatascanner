import json
import requests
import constants
import csv

def main():

    compiled_info = []

    for x in range(0, 101):
        for y in range (-42, 43):
            compiled_info.append([(str(x)+".0"), (str(y)+".0")])

    #print(compiled_info)

    #for item in compiled_info:
     #   if item[0] == "0.0":
      #      print(item)

    csv.register_dialect('myDialect',
    delimiter = ',',
    skipinitialspace=True)

    #e = ["72.0", "-1.0", "shot"]
    
    #for item in compiled_info:
       # if item[0] == e[0]:
        #    if item[1] == e[1]:
         #       item.append(e[2])
                            
   # print (compiled_info[5871])

    with open('/Users/samee/Documents/Shot Danger Project/shots_data_no_tip.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, dialect='myDialect')
        for row in reader:
            #print (compiled_info)
            print("scanning")
            if not row:
                ee = 1
            else:
                #print(row)    
                for item in compiled_info:
                    if item[0] == row[0]:
                        if item[1] == row[1]:
                            if row[3] == "even" or row[3] == "Even":
                                if row[2] == "shot":
                                    item.append("shot")
                                    print(item)
                                else:
                                    if row[2] == "goal":
                                        item.append("goal")
                                        print(item)
    
    csvFile.close()


    createcsv(compiled_info)
    print("fin")

def createcsv(info):

    with open('/Users/samee/Documents/Shot Danger Project/no_tip_compiled.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(info)
    
    csvFile.close()

if __name__ == '__main__':
    main()