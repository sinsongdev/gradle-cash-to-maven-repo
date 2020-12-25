# File name: gradle_cache_to_repo.py
# Author by: ksh (sinsongdev@gmail.com)
# History: 
# [2019/05/31 11:27 AM] Created.
# [2020/12/25 10:22 AM] "Cannot create a file when that file already exists" error fix.
#
# Function: Convert android gradle cache into local maven repository.
#           This local maven repository can be used in gradle offline build directly instead of gradle cache.

import os
from shutil import copyfile

logging = False
src = "E:/android/gradle_home/caches/modules-2/files-2.1/"
dst = "E:/android/gradle_local_repo/"

group_count = 0
artifect_count = 0

def makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return

def processGroup(group):
    global group_count
    group_count = group_count + 1
    group_dir = group.replace(".", "/")
    if (logging):
        print(group_dir)
    makedirs(dst + group_dir)

    artifects = os.listdir(src + group)
    for artifect in artifects:
        processArtifect(group, group_dir, artifect)
    return

def processArtifect(group, group_dir, artifect):
    global artifect_count
    artifect_count = artifect_count + 1
    artifect_dir = dst + group_dir + "/" + artifect
    makedirs(artifect_dir)
    if (logging):
        print(artifect)

    src_artifect_dir = src + group + "/" + artifect
    versions = os.listdir(src_artifect_dir)
    for version in versions:
        processVersion(group, artifect, artifect_dir, version)
    return

def processVersion(group, artifect, artifect_dir, version):
    version_dir = artifect_dir + "/" + version
    makedirs(version_dir)
    if (logging):
        print(version)

    src_version_dir = src + group + "/" + artifect + "/" + version
    hashs = os.listdir(src_version_dir)
    for hash in hashs:
        hash_dir = src_version_dir + "/" + hash
        files = os.listdir(hash_dir)
        
        for file in files:
            src_file_path = hash_dir + "/" + file
            dst_file_path = version_dir + "/" + file
            copyfile(src_file_path, dst_file_path)
    return

groups = os.listdir(src)
for group in groups:
    processGroup(group)

print("Done!")
print('Total {group_count} groups')
print('Total {artifect_count} artifects')