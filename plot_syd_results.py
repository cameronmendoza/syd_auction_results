import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


def graph():
	date, cr, total_sched_auct, sold_prior, passed, sold_at, withdrawn, sold_after = np.loadtxt(
		'syd_results.csv', delimiter=',', unpack=True, skiprows=1,
		converters={0: mdates.strpdate2num('%Y-%m-%d')})
	fig = plt.figure()

	ax1 = fig.add_subplot(1, 1, 1, axisbg='white')

	# General scatter plot
        plt.plot_date(x=date, y=cr, marker='x', color='b')

        # Linear interpolation
	# plt.plot_date(x=date, y=cr, marker='', linestyle='-', color='g')

        # Line of best fit 
        # plt.plot(np.unique(date), np.poly1d(np.polyfit(date, cr, 1))(np.unique(date)))

	plt.title('Sydney\'s Clearance rate')
	plt.ylabel('Clearance rate (%)')
	plt.xlabel('Date')
	plt.show()

graph()

