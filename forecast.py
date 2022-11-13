# 5 DAY FORECAST


import pandas as pd
from itertools import islice


def future(data):

	Min_temp = []
	Max_temp = []
	Description = []
	Icon = []
	Date = []
	for i in range(0, 40, 8):
		Description.append(data['list'][i]['weather'][0]['description'])
		Icon.append(data['list'][i]['weather'][0]['icon'])
		Date.append(data['list'][i]['dt_txt'])

	for i in range(40):
		Min_temp.append(data['list'][i]['main']['temp_min'] - 273.15)
		Max_temp.append(data['list'][i]['main']['temp_max'] - 273.15)

	length_to_split = [5, 5, 5, 5, 5]
	Inputt = iter(Max_temp)
	Output = [list(islice(Inputt, elem)) for elem in length_to_split]

	Maxi = []
	for i in Output:
		Maxi.append(max(i))

	Inputt = iter(Min_temp)
	Output = [list(islice(Inputt, elem)) for elem in length_to_split]
	Mini = []
	for i in Output:
		Mini.append(min(i))

	j=0
	for i in Date:
		Date[j] = i[0:10]
		j += 1

	j = 0
	for i in Icon:
		Icon[j] = 'http://openweathermap.org/img/w/{}.png'.format(i)
		j += 1

	d = {'Date': Date, 'Min_temp': Mini, 'Max_temp': Maxi, 'Description': Description, 'Icon': Icon}
	df = pd.DataFrame(d)

	return df