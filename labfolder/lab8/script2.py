#!/bin/python3

import json
import csv

with open('../../data/schacon.repos.json', 'r') as file:
    data = json.load(file)

with open("chacon.csv", "w", newline="") as output:
    csv_writer = csv.writer(output)

    for i, repo in enumerate(data[:5]):
       csv_writer.writerow([
          repo.get("name", ""),
          repo.get("html_url", ""),
          repo.get("updated_at",""),
          repo.get("visibility","")
    ])
