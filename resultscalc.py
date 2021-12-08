import csv
from operator import itemgetter

f_results = open("test.csv","a")

with open("test.csv","r") as input:
    reader = csv.reader(input)
    rating = next(reader)
    marks = next(reader)
    marks.remove("Marks: ")
    headers = next(reader)
    race_data = [row for row in reader]

#remove st, 
# for i in race_data:
#     del race_data[i][3:5]

#sort by et per mark
et_sort = sorted(race_data, key=itemgetter(-2))
et = sorted(et_sort, key=itemgetter(0))
print(et,"\n\n")

#sort by ct per marks
ct_sort = sorted(race_data, key=itemgetter(-1))
ct = sorted(ct_sort, key=itemgetter(0))
print(ct)



# f_results.write("\n\nElapsed time rank:\n")
# for i in et:
#     f_results.write(str(i)+"\n")

# f_results.write("\n\nCorrected time rank:\n")
# for i in ct:
#     f_results.write(str(i)+"\n")

