import plotly
import random
#plotly.tools.set_credentials_file(username='yashvermac',api_key='hgd48mxf12')

a=[]
b=[]
c=[]

NP = raw_input("Enter number of points > ")
N = raw_input("Enter the range of points > ")
div = raw_input("Enter number of div you want to create > ")

for i in xrange(0,int(NP)):
	a.append(random.uniform(1,int(N)))
	b.append(random.uniform(1,int(N)))
 
for i in xrange(int(div)):
    c.append([])
    for j in range(int(div)):
        c[i].append(0)


for i in xrange(0,int(NP)):
    x = int(a[i]/(int(N)/int(div)))
    y = int(b[i]/(int(N)/int(div)))
    c[int(x)][int(y)] += 1

data = [
        plotly.graph_objs.Heatmap(
            z=c
            )
        ]

plotly.offline.plot(data)
