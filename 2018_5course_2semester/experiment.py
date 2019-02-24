import matplotlib.pyplot as plt
left, bottom = 0.1, 0.1 # procentage from figure size
width, hight = 0.8,0.8 # procentage from figure size
rect = [left, bottom, width, hight]
plt.figure(1, figsize=(5,4))

axPlot = plt.axes(rect)
axPlot.plot()

plt.show()
