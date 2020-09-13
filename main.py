import matplotlib.pyplot as pyplot
import csv

sp = []
tp = []
dv = []
hg = []
sec = []

def rdr(filename,row1,lst):
	with open(filename,newline='') as csvfile:
		reader = csv.DictReader(csvfile,delimiter=";")
		for row in reader:
			lst.append(row[row1])
		


def createShedule(sp,tp,dv,hg,scd):

	pyplot.figure(figsize=(14, 14))

	pyplot.subplot(2, 2, 1)
	pyplot.plot(sp,scd)
	pyplot.title('Скорость', fontsize = 20)
	pyplot.xlabel('секунды', fontsize=12)
	pyplot.ylabel('скорость м/с', fontsize=12)

	pyplot.subplot(2, 2, 2)
	pyplot.plot(tp, scd, 'r')
	pyplot.title('Температура', fontsize=20)
	pyplot.xlabel('секунды', fontsize=12)
	pyplot.ylabel('температура', fontsize=12)


	pyplot.subplot(2, 2, 3)
	pyplot.plot(dv, scd, 'purple')
	pyplot.title('Давление', fontsize = 20)
	pyplot.xlabel('секунды', fontsize=12)
	pyplot.ylabel('давление', fontsize=12)

	pyplot.subplot(2, 2, 4)
	pyplot.plot(hg,scd , 'g')
	pyplot.title('Высота', fontsize=20)
	pyplot.xlabel('секунды', fontsize=12)
	pyplot.ylabel('высота', fontsize=12)


	pyplot.show()

rdr("test.csv","sp",sp)
rdr("test.csv","tp",tp)
rdr("test.csv","dv",dv)
rdr("test.csv","hg",hg)
for i in range(len(sp)):
	sec.append(i+1)
createShedule(sp,tp,dv,hg,sec)






