from matplotlib import pyplot as plt

x = [1,4,9,16,25,36,49,64]

y = [i for i in range(1,9)]

plt.plot(x,y,'<',color='g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('matplotlib sample')

plt.show()