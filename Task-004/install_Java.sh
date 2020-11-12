#!/bin/bash

cd 
sudo apt update

mkdir -p opt
cd opt


wget -O jdk-8u221-linux-x64.tar.gz -c --content-disposition  "https://javadl.oracle.com/webapps/download/AutoDL?BundleId=239835_230deb18db3e4014bb8e3e8324f81b43"


tar -zxvf jdk-8u221-linux-x64.tar.gz


rm jdk-8u221-linux-x64.tar.gz
gedit 
cd 

touch bash_profile
echo "JAVA_HOME=~/opt/jdk1.8.0_221" >> .bash_profile
echo "export PATH=$PATH:$JAVA_HOME/bin" >> .bash_profile
