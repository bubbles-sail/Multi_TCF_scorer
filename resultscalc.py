import csv
from operator import itemgetter

def get_race_data():
    with open("RACE 1.csv","r") as input:
        reader = csv.reader(input)
        rating = next(reader)
        rating = str(rating[1])
        ref_boat = next(reader)
        ref_boat = str(ref_boat[1])
        mark_list = next(reader)
        mark_list.remove("Marks: ")
        headers = next(reader)
        race_data = [row for row in reader]
    mark_ind = []                     #creates mark index - would normally call/pass from timer.py?
    for i in range(len(mark_list)):
        mark_ind.append(i+1)
    return rating, ref_boat, mark_list, mark_ind, headers, race_data

def get_sorted_results(race_d):
    et_sort = sorted(race_d, key=itemgetter(5))
    et = sorted(et_sort, key=itemgetter(0))
    ct_sort = sorted(race_data, key=itemgetter(6))
    ct = sorted(ct_sort, key=itemgetter(0))
    return et, ct

#####################################################################################
#Write results to file

rating_band, ref_boat, marks, mark_id, file_headers, race_data = get_race_data()    #reference_boat
et_rank, ct_rank = get_sorted_results(race_data)

f_results = open("Results.csv","a")
f_results.write("Race results\nRating,"+rating_band+"\nMk num,Mk name")
for i in range(len(marks)):
    f_results.write("\n"+str(mark_id[i])+","+str(marks[i]))
f_results.write("\nReference boat:,"+ref_boat)
f_results.write("\n\nElapsed time rank:\n")
for i in range(len(file_headers)):
    f_results.write(file_headers[i]+",")
f_results.write("\n")

for i in et_rank:
    for j in i:
        f_results.write(str(j)+",")
    f_results.write("\n")

f_results.write("\n\nCorrected time rank:\n")
for i in range(len(file_headers)):
    f_results.write(file_headers[i]+",")
f_results.write("\n")

for i in ct_rank:
    for j in i:
        f_results.write(str(j)+",")
    f_results.write("\n")