# LIVE Sentiment Data Plotting Module

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(object):
    tweetData = open('Tweet_Sentiments.txt','r').read()
    lines = tweetData.split('\n')
    xarr = []
    yarr = []
    x = 0
    y = 0
    for l in lines:
        x += 1
        if 'pos' in l:
            y += 1
        elif 'neg' in l:
            y -= 0.4
        xarr.append(x)
        yarr.append(y)
    ax1.clear()
    ax1.plot(xarr, yarr)
    plt.xlabel('Time')
    plt.ylabel('Sentiment')
    plt.title('Loc: San Francisco')
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.xlabel('Time')
plt.ylabel('Sentiment')
plt.show()