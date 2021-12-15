import csv
from operator import itemgetter
from datetime import datetime

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

def get_sorted_results(race_d, mark_ids):
    et_sort = sorted(race_d, key=itemgetter(5))
    et = sorted(et_sort, key=itemgetter(0))
    ct_sort = sorted(race_data, key=itemgetter(6))
    ct = sorted(ct_sort, key=itemgetter(0))
    return et, ct

def convert_data_from_string(input):
    for j in range(len(input)):
        #times str to datetime
        time_string = input[j][3]
        input[j][3] = datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')
        time_string = input[j][4]
        input[j][4] = datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S.%f')
        time_string = input[j][5]
        input[j][5] = datetime.strptime(time_string, '%H:%M:%S.%f')
        time_string = input[j][6]
        input[j][6] = datetime.strptime(time_string, '%H:%M:%S.%f')
        #marks str to int
        mark_string = input[j][0]
        input[j][0] = int(mark_string)
        #rating str to float
        rating_string = input[j][2]
        input[j][2] = float(rating_string)
    output = input
    return output

def get_ct_deltas_dict(input,marks):
    temp_list = []
    d_ct_rank = []
    for i in marks:
        for j in range(len(input)):
            if i == int(input[j][0]):
                temp_list.append(input[j])
        for k in range(1,len(temp_list)):
            temp_list[k].append(temp_list[k][6] - temp_list[k-1][6])
        temp_list[0].append(datetime.now() - datetime.now())
        d_ct_rank.append(temp_list)
        temp_list=[]       
    return d_ct_rank

#####################################################################################
#Write results to file

rating_band, ref_boat, marks, mark_id, file_headers, race_data = get_race_data()    #reference_boat
str_et_rank, str_ct_rank = get_sorted_results(race_data, mark_id)
elapsed_rank = str_et_rank

ct_rank = convert_data_from_string(str_ct_rank)      #converts file data strings to int/float/datetime
d_ct_rank = get_ct_deltas_dict(ct_rank,mark_id)      #adds ct delta to first boat in ct at each mark

#write race info to file
f_results = open("Results.csv","a")
f_results.write("Race results\nRating,"+rating_band+"\nMk num,Mk name")
for i in range(len(marks)):
    f_results.write("\n"+str(mark_id[i])+","+str(marks[i]))
f_results.write("\nReference boat:,"+ref_boat)
f_results.write("\n\nElapsed time rank:\n")
for i in range(len(file_headers)):
    f_results.write(file_headers[i]+",")
f_results.write("\n")

#write et info to file
for i in elapsed_rank:
    for j in i:
        f_results.write(str(j)+",")
    f_results.write("\n")

f_results.write("\n\nCorrected time rank:\nBoat,Elapsed,Corrected,dCorrected")

f_results.write("\n")
#write ct info to file
for i in mark_id:
    f_results.write("Mark "+str(i)+"\n")
    for j in d_ct_rank:
        for k in j:
            if k[0] == i:
                f_results.write(k[1]+","+k[5].strftime("%H:%M:%S.%f")+","+k[6].strftime("%H:%M:%S.%f")+","+str(k[7])+"\n")
        
    f_results.write("\n")