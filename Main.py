import pandas as pd
from functools import reduce
import requests
club_amount = int(input("how many clubs does your organization own?"))

club_list = []
def club_merge(club_amount,club_list):
    merged_club = reduce(lambda left, right: pd.merge(left,right, on = 'trophies', how = 'outer'), club_list)
    
    
        
        
    return merged_club



for i in range(club_amount):
    
    
    api_url = input("Enter your url. Find your club's url on the brawl stars developer website. ")
    api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjMzMWQwNWQzLTYxZTgtNDk2OS05MjI2LTc0ZmVjMWU0NTRiYiIsImlhdCI6MTcyMzQ5NzA5NCwic3ViIjoiZGV2ZWxvcGVyLzlmZGE4M2ZmLTVkNzQtN2NjYi0zYjg5LTRhZjMzN2ZiMzFmNCIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiOTkuMTcwLjMzLjYzIl0sInR5cGUiOiJjbGllbnQifV19.VJIdlCpBaliK2GLQfQvzdwkqiaB1dvJBdmY_Qsq75aPLqlPGC6gtPt55-TFrkncqgqnMRGY-7DX51_cfC3vHrg'    
    headers = { 
        'Authorization': f'Bearer {api_key}'
    }

    response = requests.get(api_url, headers=headers)
    data = response.json()
    club_members = data["members"]
    member_list = []
    trophy_list = []
    for member in club_members:
        member_list.append(member["name"])
        trophy_list.append(member["trophies"])
    Club = pd.DataFrame({"Players" : member_list,
        "trophies": trophy_list})
    club_list.append(Club)
    
organization = club_merge(club_amount, club_list)
print(organization.describe())

