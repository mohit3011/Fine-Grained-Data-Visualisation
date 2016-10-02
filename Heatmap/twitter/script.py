from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np
import os
import re
import pandas as pd
try:
    import json
except ImportError:
    import simplejson as json

h1 = raw_input("Enter hashtag 1 > ")
h2 = raw_input("Enter hashtag 2 > ")
h3 = raw_input("Enter hashtag 3 > ")

color = ['#2ecc71','#2980b9','#c0392b','#f1c40f','#2c3e50']

ckey = 'fibkxu7Ki2PjXQM13EOpqNoB8'
csecret = 'aLs6U02RHTl3Hx1XOyF20SuYAfUpAKGJvEWpca1s8JWqqEw7Wg'
atoken = '744960984230440960-va4hCQfFm43kPT3kbb7BVwX7Xtnj7Wa'
asecret = 'pCRHlvHBLsTgPymvtzVNiXX6sl44dBPTEmBHpfMFycd63'

oauth = OAuth(atoken , asecret, ckey, csecret)

twitter_stream = TwitterStream(auth=oauth)

filterString = h1+","+h2+","+h3
iterator = twitter_stream.statuses.filter(track=filterString)


total_tweets = 0
t=[]
cnt_of_h=[0,0,0]
width = 0.8

fig,ax = plt.subplots()
h = [h1,h2,h3]
x_pos = list(range(len(h)))

def word_in_text(word,text):
    word = word.lower()
    text = text.lower()
    match = re.search(word,text)
    if match:
        return True
    return False

def add_data():
    global total_tweets
    cnt = 0

    if total_tweets > 3000:
        os.system('sleep 1m')
        os.system('exit')

    for tweet in iterator:
        try:
            x = json.dumps(tweet)
            j = json.loads(x)
            tweet_text = j['text']
            if word_in_text(h1,tweet_text):
                cnt_of_h[0] += 1
            if word_in_text(h2,tweet_text):
                cnt_of_h[1] += 1
            if word_in_text(h3,tweet_text):
                cnt_of_h[2] += 1
        except:
            continue
        cnt += 1
        if cnt == 5:
            break;
       
    total_tweets += 5
    print total_tweets

def animate(i):
    global width
    add_data()
    width = 0.5
    ax.clear()
    ax.set_ylabel('Number of tweets')
    stitle = "Ranking : "+h1+" vs. " + h2 + " vs. " + h3
    ax.set_title(stitle)
    ax.set_xticks([p+ 0.2*width for p in x_pos])
    ax.set_xticklabels(h)
    plt.bar(x_pos, cnt_of_h, width, color='g')


ani = animation.FuncAnimation(fig,animate,interval=10)

plt.show()
