#coding:utf-8

import os, subprocess

dir_here = os.getcwd()
print(dir_here)

dir_save_log = os.path.join(dir_here, "device_raw.txt")
dir_save_sort = os.path.join(dir_here, "device_sorted.txt")

cmd = "ffmpeg -list_devices true -f dshow -i dummy 2> \"{}\"".format(dir_save_log)
subprocess.Popen(cmd, shell=True)
print(cmd)


with open(dir_save_log, "r", encoding="utf-8") as reader:
    data_log = reader.read()
    
data_device_raw = data_log.split("DirectShow video devices (some may be both video and audio devices)")[1].split("DirectShow audio devices")[0]


data_device = [i.split("]")[1].replace("\n", "") for i in data_device_raw.split("[")[1:-1]]

print(len(data_device))
for i in range(len(data_device)//2):
    print("{},{}".format(data_device[i*2].replace("  \"", "").replace("\"", ""), data_device[i*2+1].replace("     Alternative name \"", "").replace("\"", "")))
    

data_device_s = "\n".join(["{},{}".format(data_device[i*2].replace("  \"", "").replace("\"", ""), data_device[i*2+1].replace("     Alternative name \"", "").replace("\"", "")) for i in range(len(data_device)//2)])

print(type(data_device_s))


with open(dir_save_sort, "w", encoding="utf-8") as writer:
    writer.write(data_device_s)
