from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np
try:
    import json
except ImportError:
    import simplejson as json

ckey = 'fibkxu7Ki2PjXQM13EOpqNoB8'
csecret = 'aLs6U02RHTl3Hx1XOyF20SuYAfUpAKGJvEWpca1s8JWqqEw7Wg'
atoken = '744960984230440960-va4hCQfFm43kPT3kbb7BVwX7Xtnj7Wa'
asecret = 'pCRHlvHBLsTgPymvtzVNiXX6sl44dBPTEmBHpfMFycd63'

oauth = OAuth(atoken , asecret, ckey, csecret)

twitter_stream = TwitterStream(auth=oauth)

iterator = twitter_stream.statuses.sample()


#x # followers_count (number of followers of user)
#y # friends_count (number of following of user)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

xd=[]
yd=[]
#hm = heatmap.Heatmap()
#heatmap, xedges, yedges = np.histogram2d(xd,yd,bins=500)
#extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

def add_data():
    cnt = 0
    xs=[]
    ys=[]
    lst = []
    for tweet in iterator:
        try:
            x = json.dumps(tweet)
            j = json.loads(x)
            foll_count = j['user']['followers_count']
            frie_count = j['user']['friends_count']
            if foll_count <= 1000 and frie_count <= 1000 and foll_count >= 100 and frie_count >= 100:
                xs.append(foll_count)
                ys.append(frie_count)
            print foll_count,frie_count
        except:
            continue
        if cnt > 5:
            break;
        cnt += 1
    lst.append(xs)
    lst.append(ys)
    return lst

def animate(i):
    xs,ys = add_data()
    xd.extend(xs)
    yd.extend(ys)
    ax1.clear()
    ax1.scatter(xd,yd)
    #plt.hist2d(xd,yd,bins=40)


ani = animation.FuncAnimation(fig,animate,interval=10)
plt.show()

'''
try:
    thread.start_new_thread(add_data,(2,))
    thread.start_new_thread(plot_data,(2,))
except:
    print "Error creating thread"


while 1:
    pass
'''


'''
for tweet in iterator:
    try:
        x = json.dumps(tweet)
        j = json.loads(x)
        foll_count = j['user']['followers_count']
        frie_count = j['user']['friends_count']
        #print j
        #print foll_count,frie_count
        if foll_count <= 1000000 and frie_count <= 1000000:
            x.append(foll_count)
            y.append(frie_count)
        #plt.plot(x,y)
        #plt.pause(0.1)
        #plt.show()
    except:
        continue
'''
