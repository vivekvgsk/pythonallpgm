isldata=[
    {"team":"mumbai","mp":20,"won":12,"draw":4,"los":4,"pts":40},
    {"team":"atk","mp":20,"won":12,"draw":4,"los":4,"pts":40},
    {"team":"ne","mp":20,"won":8,"draw":9,"los":3,"pts":33},
    {"team":"fcg","mp":20,"won":6,"draw":11,"los":3,"pts":31},
    {"team":"hybd","mp":20,"won":6,"draw":11,"los":3,"pts":29},

]
#to find the team with points in range of 30-40
rangeteam=list(filter(lambda data:(data["pts"]<=40) & (data["pts"]>30),isldata))
print(rangeteam)
team_name=list(map(lambda team:team["team"],rangeteam))
print(team_name)
#number of total teams
teamno=len(isldata)
print(teamno)
#to print team names
team_name=list(map(lambda data:data["team"],isldata))
print(team_name)
#to find highest point
hp=max(list(map(lambda data:data["pts"],isldata)))
print(hp)
#to find team detaiils with highest point
ht=list(filter(lambda team:team["pts"]==hp,isldata))
print(ht)
#to find the team name with highest point
highestpt_team=list(map(lambda team:team["team"],ht))
print(highestpt_team)