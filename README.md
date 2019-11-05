# gradle-cash-to-maven-repo
Simple python script to convert gradle cache into local maven repository.

## Introduction
Android Studio is an excellent IDE for android app development and this is heavily dependent on the gradle build system and the maven repository.
The gradle downloads all dependency libraries from the maven repository into the local cache folder.
But this cache folder is not portable. If we  transfer this cache folder from our PC to another, the gradle doesn't recognize copied version of gradle cache.

To resolve this issue, I have developed small python script that converts the gradle cache folder into local maven repository.

## Converting
In fact, gradle cache folder structure is almost the same as local maven repository and my script will convert the local gradle cache folder into local maven equivalent.

## Usage
Android Studio configuration.