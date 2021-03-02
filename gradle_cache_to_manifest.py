# File name: gradle_cache_to_manifest.py
# Author by: ksh (sinsongdev@gmail.com)
# History: 
# [2021/03/02 08:27 PM] Created.
#
# Function: Create a manifest file that contains a list of the latest versions of android gradle cache libraries.
#           This manifest can be used in gradle offline synchronize.

import os
from shutil import copyfile

src = "E:/android/gradle_home/caches/modules-2/files-2.1/"
manifest_file_path = "E:/android/gradle_cache_manifest.txt"

def processGroup(group):
    artifects = os.listdir(src + group)
    for artifect in artifects:
        processArtifect(group, artifect)
    return

def processArtifect(group, artifect):
    src_artifect_dir = src + group + "/" + artifect
    versions = os.listdir(src_artifect_dir)
    last_version = versions[-1]
    processVersion(group, artifect, last_version)
    return

def processVersion(group, artifect, version):
    manifest_file.write(group + ':' + artifect + ':' + version + '\n')
    return

manifest_file = open(manifest_file_path, 'w')

groups = os.listdir(src)
for group in groups:
    processGroup(group)

manifest_file.close()

print("Done!")