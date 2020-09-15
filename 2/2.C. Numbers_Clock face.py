"""The hour hand of an analog clock turned α degrees since the midnight. Determine the angle
by which the minute hand turned since the start of the current hour. Input and output in this problems are integers.

Example input
190
(6:20)
Example output
120
(20 min)
"""
#30 degree for per hour
#6 degree for per minute
mins = int(input())

hour = int(mins/30)
minutes_passed  = (mins - hour*30)
print(hour)
print(minutes_passed*6*2)