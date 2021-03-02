# File name: gradle_cache_synchronizer.py
# Author by: ksh (sinsongdev@gmail.com)
# History: 
# [2021/03/02 08:27 PM] Created.
#
# Function: Extract latest versions of android gradle cache libraries with a manifest file.

import os
from shutil import copyfile
from distutils.dir_util import copy_tree

src = "E:/android/gradle_home/caches/modules-2/files-2.1/"
dst = "E:/android/gradle_cache_latest/"
manifest_file_path = "E:/android/gradle_cache_manifest.txt"


def checkExistance(group, artifect):
    src_version_dir = src + group + "/" + artifect
    exist = os.path.exists(src_version_dir)
    return exist

def getLastVersion(group, artifect):
    src_version_dir = src + group + "/" + artifect
    versions = os.listdir(src_version_dir)
    last_version = versions[-1]
    return last_version

def exportVersion(group, artifect, version):
    src_version_dir = src + group + "/" + artifect + "/" + version
    dst_version_dir = dst + group + "/" + artifect + "/" + version
    copy_tree(src_version_dir, dst_version_dir)
    return


manifest_file = open(manifest_file_path, 'r')
manifest_file_lines = manifest_file.readlines()
for manifest_file_line in manifest_file_lines:
    manifest_file_line_tokens = manifest_file_line.split(':')
    group = manifest_file_line_tokens[0]
    artifect = manifest_file_line_tokens[1]
    manifest_version = manifest_file_line_tokens[2]

    if checkExistance(group, artifect) == True:
        last_version = getLastVersion(group, artifect)
        if last_version > manifest_version:
            exportVersion(group, artifect, last_version)
            print(manifest_file_line)

manifest_file.close()

print("Done!")