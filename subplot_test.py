import pylab

def init():
	global times, prices
	times = []
	prices = []
	init = 1
	with open("BHP.csv", "r") as file:
		for line in file:
			if(init == 1):
				init = 0
				continue
			c = line.split(",")
			time = c[0]
			price = float(c[4])
			times.append(time)
			prices.append(price)


			

def observe():
	global times, prices
	pylab.subplot(2,1,1)
	pylab.plot(prices)
	min_price = min(prices)
	max_price = max(prices)
	pylab.ylim(min_price-10, max_price+10)
	pylab.xticks([])
	pylab.subplot(2,2,3)	
	pylab.plot([1,2,3,4], [1,2,3,4])
	pylab.subplot(2,2,4)
	pylab.plot([1,2,3,4], [2,3,4,5])
	pylab.show()

init()
observe()
