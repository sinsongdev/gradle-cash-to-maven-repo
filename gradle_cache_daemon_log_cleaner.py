# File name: gradle_cache_daemon_log_cleaner.py
# Author by: ksh (sinsongdev@gmail.com)
# History: 
# [2022/08/31 11:27 AM] Created.
#
# Function: Delete all daemon log files from gradle cache. 
#           Gradle daemon log files are in /gradle_home/daemon/{version}/daemon-{***}.out.log
#

import os
from shutil import copyfile

logging = True
gradle_home_path = "E:/android/gradle_home"
deleted_log_file_count = 0

def processDaemonVersion(gradle_home_daemon_version_path):
    global deleted_log_file_count

    if (logging):
        print(gradle_home_daemon_version_path)

    files = os.listdir(gradle_home_daemon_version_path)
    for file in files:
        if (file.endswith('.out.log')):
            deleted_log_file_count = deleted_log_file_count + 1
            if (logging):
                print(gradle_home_daemon_version_path + file)
            os.remove(gradle_home_daemon_version_path + file)
    return

gradle_home_daemon_path = gradle_home_path + "/daemon/"
daemon_versions = os.listdir(gradle_home_daemon_path)
for daemon_version in daemon_versions:
    gradle_home_daemon_version_path = gradle_home_daemon_path + daemon_version + '/'
    processDaemonVersion(gradle_home_daemon_version_path)

print("Done!")
print("Total %d files are deleted!"%(deleted_log_file_count))