"""
Our football team has finished the championship.

Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", 
where x is our team's score and y is our opponents score.

For example: ["3:1", "2:2", "0:1", ...]

Points are awarded for each match as follows:

if x > y: 3 points (win)
if x < y: 0 points (loss)
if x = y: 1 point (tie)
We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

Notes:

our team always plays 10 matches in the championship
0 <= x <= 4
0 <= y <= 4
"""

def points(games):
    result = 0
        
    for i in games:        
        if i[0] > i[2]:
            result += 3
        elif i[0] == i[2]:
            result += 1
    
    return result


"""
def points(games):
    count = 0
        
    for i in games:
        result = i.split(':')
        if result[0] > result[1]:
            count += 3
        elif result[0] == result[1]:
            count += 1
    
    return count
"""     

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))
