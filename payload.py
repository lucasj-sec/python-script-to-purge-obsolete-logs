import os 
from os import path
import shutil
import time

limit_use = 75
path_logs = "/var/log"

def check_disk_usage ():
    total, used, free = shutil.disk_usage(path_logs)
    percent_used = (used / total) * 100
    if percent_used > limit_use:
        print("WARNING: Disk usage is above the limit of {}%".format(limit_use))
        action = input("Do you want to delete old logs? (y/n): ")
        if action.lower() == 'y':
            erase = time.time() - 7776000 # 3 months in seconds, Junior! 
            for archive in os.listdir(path_logs):
                complet_path = os.path.join(path_logs, archive)
                if os.path.getmtime(complet_path) < erase:
                    os.remove(complet_path)
                    print("Deleted: {}".format(complet_path))
        else:
            print("Do it yourself, analyst!")
    else:
        print("You're not coocked else, analyst")

if __name__ == "__main__":
    check_disk_usage()