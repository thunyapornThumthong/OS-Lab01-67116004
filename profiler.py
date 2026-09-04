# ==========================================
# OS-Lab 01: System Profiler
# Student ID: [67116004]
# ==========================================
import os
import psutil
import platform

print(f"OS Name: {platform.system()} {platform.release()}")
print(f"Number of CPU Cores: {psutil.cpu_count(logical=True)}")
print(f"Total RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB")





# TODO: Write your system profiler code here 
# Follow the instructions in the Lab manual.
