import matplotlib.pyplot as plt


x1=[2,5,8,11,14]
y1=[1,3,5,7,9]

plt.plot(x1,y1,label="Line 1")

x2=[1,5,7,8,11,15]
y2=[15,12,10,6,5,3]

plt.plot(x2,y2,label= 'Line 2')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title('Demo Graph - Two Lines')

plt.legend()  
plt.show()

