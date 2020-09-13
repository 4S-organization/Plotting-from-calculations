import matplotlib.pyplot as pyplot
import csv

speed = []
temperature = []
pressure = []
height = []
second = []



def startRendering():	# Start programm
	readCSVFile("tests/test1.csv","speed", speed)
	readCSVFile("tests/test1.csv","temperature", temperature)
	readCSVFile("tests/test1.csv","pressure", pressure)
	readCSVFile("tests/test1.csv","height", height)
	readCSVFile('tests/test1.csv', "second" , second)
	createShedule(speed,temperature,pressure,height,second)


def readCSVFile(filename,row1,lst):
	with open(filename,newline='') as csvfile:
		reader = csv.DictReader(csvfile,delimiter=";")
		for row in reader:
			lst.append(row[row1])
		


def createShedule(sp,tp,dv,hg,scd):

	print(second)

	pyplot.figure(figsize=(14, 14))

	pyplot.subplot(2, 2, 1)
	pyplot.plot(scd,sp)
	pyplot.title('Скорость', fontsize = 20)
	pyplot.xlabel('секунды', fontsize=12)
	pyplot.ylabel('скорость м/с', fontsize=12)

	pyplot.subplot(2, 2, 2)
	pyplot.plot(scd, tp, 'r')
	pyplot.title('Температура', fontsize=20)
	pyplot.xlabel('секунды', fontsize=12)
	pyplot.ylabel('температура', fontsize=12)


	pyplot.subplot(2, 2, 3)
	pyplot.plot(scd, dv, 'purple')
	pyplot.title('Давление', fontsize = 20)
	pyplot.xlabel('секунды', fontsize=12)
	pyplot.ylabel('давление', fontsize=12)

	pyplot.subplot(2, 2, 4)
	pyplot.plot(scd, hg, 'g')
	pyplot.title('Высота', fontsize=20)
	pyplot.xlabel('секунды', fontsize=12)
	pyplot.ylabel('высота', fontsize=12)


	pyplot.show()



if __name__ == '__main__':
	startRendering()