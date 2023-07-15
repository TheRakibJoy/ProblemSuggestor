import json
import csv
import requests
# Define the column names
columns = ['ID', 'Index', 'Rating','Tags']

# Specify the output CSV file path
output_csv = 'CMtoMaster.csv'

# Write data to the CSV file
with open(output_csv, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(columns)
    handle = "adnan_toky"
    url = 'https://codeforces.com/api/user.rating?handle=' + handle
    current = 1900
    target = 2100
    response = requests.get(url)
    x = response.json()
    start = 0
    end = 0
    for con in x['result']:
        if start == 0 and con['newRating'] >= current and con['oldRating'] != 0:
            start = con['ratingUpdateTimeSeconds']
        if start > 0:
            end = con['ratingUpdateTimeSeconds']
        if con['newRating'] >= target:
            break
    # gets the start and end time

    url = 'https://codeforces.com/api/user.status?handle=' + handle + '&from=1'
    response = requests.get(url)
    x = response.json()
    cnt = 0
    for sub in x['result']:
        if start <= sub['creationTimeSeconds'] <= end and sub['verdict'] == 'OK':
            if 'rating' in sub['problem'] and sub['problem']['rating'] > current:
                con_id = sub['contestId']
                index = sub['problem']['index']
                rating = sub['problem']['rating']
                tags = sub['problem']['tags']
                for i in range(len(tags)):
                    tags[i] = tags[i].replace(" ","");
                    tags[i] = tags[i].replace("-", "");
                tags=', '.join(tags)
                print(tags)
                row =[con_id, index, rating, tags]
                writer.writerow(row)


print("CSV file created successfully.")
