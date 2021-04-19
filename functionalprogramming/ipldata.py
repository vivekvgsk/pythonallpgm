ipldata=[
    {"team":"mumbai","mp":20,"won":12,"draw":4,"los":4,"pts":40},
    {"team":"punjab","mp":20,"won":12,"draw":4,"los":4,"pts":65},
    {"team":"kkr","mp":20,"won":8,"draw":9,"los":3,"pts":33},
    {"team":"dd","mp":20,"won":6,"draw":11,"los":3,"pts":31},
    {"team":"csk","mp":20,"won":6,"draw":11,"los":3,"pts":29},
    ]
#highest point
hp=list(map(lambda points:points["pts"],ipldata))
print(hp)
print(max(hp))
team=list(filter(lambda team:team["pts"]==max(hp),ipldata))
print(team)
range_team=list(filter(lambda team:(team["pts"]<=70) & (team["pts"]>30),ipldata))
print(range_team)
print(len(range_team))
teams=list(map(lambda team:team["team"],range_team))
print(teams)
