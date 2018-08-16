import csv
import json
import sys
try:
    file_input= sys.argv[1]
    file_output = sys.argv[2]
    with open(file_input,"r") as fileinput_json :
        json_content=json.load(fileinput_json)
    with open(file_output,"w") as fileoutput_csv :
        csv_writer= csv.DictWriter(fileoutput_csv,fieldnames=json_content[0].keys())
        csv_writer.writeheader()
        #print(json_content[0].keys())
        for row in json_content:
            #print (row.values())
            csv_writer.writerow(row)
except IOError:
    print ("I/O error") 