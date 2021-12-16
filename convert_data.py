#!/usr/bin/env python3
import csv
import json

with open('inflation.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')

    yearly_data = {}

    for row in reader:
        datetime = row['C-VPIZR-0']
        if len(datetime) == 10:
            yearly_data[datetime[6:]] = float(row['F-VPIMZBM'].replace(',', '.'))

    print(json.dumps(yearly_data))
