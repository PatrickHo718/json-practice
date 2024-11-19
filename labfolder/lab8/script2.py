#!/bin/python3

import json
import csv

with open('../../data/schacon.repos.json', 'r') as file:
    data = json.load(file)

with open("chacon.csv", "w", newline="") as output:
    csv_writer = csv.writer(output)

    csv_writer.writerow(["name","html_url","updated_at","visibility"])

    for i, repo in enumerate(data[:5]):
       csv_writer.writerow([
          repo.get("name", ""),
          repo.get("html_url", ""),
          repo.get("updated_url",""),
          repo.get("visibilty_url","")
    ])
