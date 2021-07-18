import requests
import json
import csv


""" URL to Hasura endpoint to get mail message of account invoice
with a fixed date range (Q1)
with Limit of 5 and offset of 5
 """
path = "getAccountInvoiceQ1Distinct"
url = "http://localhost:8080/api/rest/{}".format(path)

""" get the response from Hasura in JSON (Python Dict) """
resp = requests.get(url)
data = resp.json()



""" write the Dict Object to a JSON file """
""" to easily visualize the data """
filename = "{}.json".format(path) # set the file name the same as the Hasura path to easily remember
filepath = "./data/{}".format(filename)
with open(filepath, "w") as json_file:
    # writer = csv.writer(json_file, delimiter=",")
    # writer.writerow([data])
    json.dump(data, json_file)

first_record = data["mail_message"][0]
print(first_record)


""" ## this is to test a theory 
# print(resp.content)
# parsed = json.loads(resp.content)

# r = resp.content.decode()
with open('./data/test2.json', "w") as json_file:
    writer = csv.writer(json_file, delimiter=",")
    writer.writerow([data])
    json.dump(parsed, json_file) """

""" write the distinct body in a csv """
filename = "{}.csv".format(path)
filepath = "./csv/{}"
with open('path/to/csv_file', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(row)






""" Scrap Code """
""" ---------- """
""" url = "http://localhost:8080/api/rest/getAccountInvoice"
payload = {
	"dates": "2021-01-01",
	"datee": "2021-04-01",
}


resp = requests.get(url, params=payload)
# excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
# headers = [(name, value) for (name, value) in 
# resp.raw.headers.items() if name.lower() not in excluded_headers]
# response = Response(resp.content, resp.status_code, headers)

contents = resp.content
print(contents) """


""" access the REST with a fixed date """
""" url = "http://localhost:8080/api/rest/getAccountInvoiceQ1"
headers = {'accept': "application/json", 'accept': "text/csv"}

resp = requests.get(url, headers=headers)
# print(resp.content)
data = resp.text
# print(data)

with open('./data/test1.csv', "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow([data])
    # for line in data:
    #     writer.writerow(line)
 """

# url = "http://localhost:8080/api/rest/getAccountInvoiceQ1"

""" End | Scrap Code """
