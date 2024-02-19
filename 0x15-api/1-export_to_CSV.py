#!/usr/bin/python3
'''A script that extend python script to export data in the CSV format.'''
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    usr_id = sys.argv[1]
    usr = requests.get(url + "users/{}".format(usr_id)).json()
    username = usr.get("username")
    todos = requests.get(url + "todos", params={"userId": usr_id}).json()

    with open("{}.csv".format(usr_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [usr_id, username, t.get("completed"), t.get("title")]
        ) for t in todos]
