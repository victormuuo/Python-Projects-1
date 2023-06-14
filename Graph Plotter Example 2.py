import matplotlib.pyplot as plt


x=[2,5,8,11,14]
y=[2,3,5,7,9]

plt.plot(x,y,color='blue',linestyle='dashed',linewidth=4,marker='o',markerfacecolor='green',markersize=12)

plt.ylim=(1,12)
plt.xlim=(1,15)

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title('Demo Graph - Customization')
  
plt.show()

