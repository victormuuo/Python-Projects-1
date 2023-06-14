import matplotlib.pyplot as plt


left=[2,5,8,11,14]
height=[10,3,7,12,15]
tick_label=['one','two','three','four','five']
plt.bar(left,height,tick_label=tick_label, width=0.8,color=['green','orange'])



plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title('Demo Graph - Bar Chart')
  
plt.show()

