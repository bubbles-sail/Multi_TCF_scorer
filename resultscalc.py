import csv
from operator import itemgetter

f_results = open("test.csv","a")

with open("test.csv","r") as input:
    reader = csv.reader(input)
    rating = next(reader)
    marks = next(reader)
    marks.remove("Marks: ")
    headers = next(reader)
    all_race_data = [row for row in reader]

#reduce data into mark, boat, el and cor times
race_data = all_race_data
for i in range(len(race_data)):
    del race_data[i][3:5]

#sort by et per mark
et_sort = sorted(race_data, key=itemgetter(3))
et = sorted(et_sort, key=itemgetter(0))
print(et,"\n\n")

#sort by ct per marks
ct_sort = sorted(race_data, key=itemgetter(-1))
ct = sorted(ct_sort, key=itemgetter(0))
print(ct)

f_results.write("\n\nElapsed time rank:\n")
for i in et:
    f_results.write(str(i)+"\n")

f_results.write("\n\nCorrected time rank:\n")
for i in ct:
    f_results.write(str(i)+"\n")