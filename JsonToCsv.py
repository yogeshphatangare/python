import csv
import json
try:
    with open("myplaylist.json","r") as fileinput_json :
        json_content=json.load(fileinput_json)
    with open("myplaylist.csv","w") as outputfile_csv :
        csv_writer= csv.DictWriter(outputfile_csv,fieldnames=json_content[0].keys())
        csv_writer.writeheader()
        for row in json_content:
            csv_writer.writerow(row)
except IOError:
    print ("I/O error") 
