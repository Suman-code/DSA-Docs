activities = [ ['A1' , 0 , 6],
            ['B1' , 3, 4],
            ['C1' , 1, 2],
            ['D1' , 5, 8],
            ['E1' , 8 , 9]]



def activity(activity):
    activity.sort(key=lambda x: x[2])
    i = 0
    firstA = activity[i][0]
    for j in range(len(activity)):
        if activity[j][1] > activity[i][2]:
            print(activity[j][0])
            i = j

activity(activities)

 