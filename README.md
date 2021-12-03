# Multi_TCF_scorer
Yacht racing calculator for use with multiple TCF's as used by ORC and JCA rating systems.

Utilises TCF ratings only (Time on Time)

Pulls the boats and ratings from the fleet.csv file. Figured not worth an input function to do this as can be created in excel and saved as csv file
fleet.csv format

EVENT_NAME,TCF1,TCF2,TCF3,TCF4,...,...
BOAT1_NAME,BOAT1_TCF1,BOAT1_TCF2,...,...
BOAT2_NAME,BOAT2_TCF1,BOAT2_TCF2,...,...

No practical limit to number of boats and number of TCF's per boat

Program will save results to *.csv file with user specified name (race no etc)
Records:
[Rating band used]
[Mark name],[Boat name],[Start time],[mark time],[elapsed time],[corrected time]


Future work is to use results file to score boats leg by leg and analyse leg gains/losses.


Then create a GUI and package as either:
1, webapp with the likes of flask or
2, windows and android app with Beeware
