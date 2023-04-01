import csv
import matplotlib.pyplot as pl

def read_dat(path):
	with open(path,"r") as file:
		reader = csv.reader(file, delimiter=',')
		header = next(reader)
		data = []
		for i in reader:
			it=zip(header,i)
			count_d={k:v for k,v in it}
			data.append(count_d)
		return data

def bar_graf(x,y):
	f,a=pl.subplots()
	a.bar(x,y)
	pl.show()
def pie_graf(labels,y):
	f,a=pl.subplots()
	a.pie(y,labels=labels)
	a.axis("equal")
	pl.show()


if __name__ == '__main__':
	data = read_dat('world_population.csv')
	A=True
	while A:
		a=int(input("Posicion [0,234] => "))#227 [0-234]
		if a>234 or a<0:
			print("Posicion invalida")
			continue
		graf_y=[]
		graf_x=["2022 Population","2020 Population","2015 Population","2010 Population"
		,"2000 Population","1990 Population","1980 Population","1970 Population"]
		graf_x.reverse()
		for i in graf_x:
			s=int(data[a][i])
			graf_y.append(s)
		bar_graf(graf_x,graf_y)

		#World Graf pop
		graf_y=[]
		u="World Population Percentage"
		graf_x=[]

		for i in data:
			graf_x.append(i["World Population Percentage"])
			graf_y.append(i["Country/Territory"])
		pie_graf(graf_y,graf_x)




	