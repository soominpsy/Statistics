from matplotlib import pyplot as plt

mentions = [500, 505]
years = [2013, 2014]
plt.bar([2012.6, 2013.6], mentions, 0.8)
plt.xticks(years)
plt.ylabel("number of I heard someone say 'data science'")
plt.ticklabel_format(useOffset=False)   # you can try comment this line, the result would be bad

plt.axis([2012.5, 2014.5,499, 506])
#plt.axis([2012.5, 2014.5, 0, 550])
plt.show()



