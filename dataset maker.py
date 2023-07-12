import requests
handle = "RakibJoy"
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
    if con['newRating'] >= target :
        break
#gets the start and end time

url = 'https://codeforces.com/api/user.status?handle='+handle+'&from=1'
response = requests.get(url)
x = response.json()
cnt =0
for sub in x['result']:
    if start <= sub['creationTimeSeconds'] <= end and sub['verdict']=='OK':
        if 'rating' in sub['problem'] and sub['problem']['rating']>current:
            con_id = sub['contestId']
            index = sub['problem']['index']
            rating = sub['problem']['rating']
            tags = sub['problem']['tags']
            print('id',con_id)
            print('index',index)
            print('rating',rating)
            print('tags',tags)
            cnt += 1

print(cnt)
