import csv
from operator import itemgetter
# from timer import get_mark_index

f_results = open("Results.csv","a")

with open("RACE 1.csv","r") as input:
    reader = csv.reader(input)
    rating = next(reader)
    marks = next(reader)
    marks.remove("Marks: ")
    headers = next(reader)
    race_data = [row for row in reader]


#sort by et per marks
et_sort = sorted(race_data, key=itemgetter(5))
et = sorted(et_sort, key=itemgetter(0))
print(et,"\n\n")

#sort by ct per marks
ct_sort = sorted(race_data, key=itemgetter(-1))
ct = sorted(ct_sort, key=itemgetter(0))
print(ct)

# mark_ind = get_mark_index()
mark_ind = []                     #creates mark index - would normally call/pass from timer.py
for i in range(len(marks)):
    mark_ind.append(i+1)



f_results.write("Race results\nMk num,Mk name")
for i in range(len(marks)):
    f_results.write("\n"+str(mark_ind[i])+","+str(marks[i]))

f_results.write("\n\nElapsed time rank:\n")
for i in et:
    for j in i:
        f_results.write(str(j)+",")
    f_results.write("\n")

f_results.write("\n\nCorrected time rank:\n")
for i in ct:
    for j in i:
        f_results.write(str(j)+",")
    f_results.write("\n")