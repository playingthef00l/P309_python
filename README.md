# P309 - Oil Drop Lab Python scripts
IDEA:
Find average rising/falling velocities for each drop using segmented linear regression
plug them into eqn 10 on labsheet
try to get a reasonable measure for q

1) Use clean_drops.py to clean and convert all .xls files to .csvs
2) Count the number of rising and falling segments for each drop w/ seg_count.py
3) Use the number of breaks to calculate  velocities with slr.py
4) plug the velocities for each drop into gnarly_eqn.py


Off by ~6 orders of magnitude, will recheck constants soon.
