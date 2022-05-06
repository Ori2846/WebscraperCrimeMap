import matplotlib.pyplot as plt
import json

dictionary = json.load(open('history.json', 'r'))
xAxis = [key for key, value in dictionary.items()]
yAxis = [value for key, value in dictionary.items()]
plt.grid(True)

## BAR GRAPH ##
fig = plt.figure()
plt.bar(xAxis,yAxis, color='maroon')
plt.xlabel('variable')
plt.xticks(rotation = 90)
plt.ylabel('value')


plt.show()