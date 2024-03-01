import datetime as dt
import os
import pytz    
output_path=r"D:\Notebooks\logs"

log_file="01_test_run_log.txt"
os.chdir(output_path)
log_file_path = os.path.join(os.getcwd(),log_file)

tz_IST = pytz.timezone('Asia/Kolkata')
run_date=dt.datetime.today().strftime("%d-%m-%y")
run_time= "Run  at "+dt.datetime.today().strftime("%H:%M:%S")+" IST"

sep="---------"
now1 =dt.datetime.now()
 
lines = ["\n",run_date, sep,run_time]
with open(log_file_path, 'a') as f:
    #f.writelines(lines)
    f.write('\n'.join(lines))
