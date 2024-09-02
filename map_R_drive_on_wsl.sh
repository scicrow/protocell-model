# Bash Script to map R Drive on your ubuntu WSL
#
#
#  Authour: ANJI BABU KAPAKYALA
#	    CURTIN UNIVERSITY
#
#  USAGE : sudo bash map_R_drive_on_wsl.sh
#       
#
#  You have to run the script as super user.
# 

#!/bin/bash

#----------------------------------#
#  Function to mount R_Drive
function mount_R_drive() 
{
    mkdir -p R_Drive
    mount -t drvfs //staff.ad.curtin.edu.au/dmp/A-J/Biomolecular_Model-MANCER-HS00092 -o uid=$SUDO_USER,gid=$SUDO_USER,rw,users R_Drive/
    if [ $? -eq 0 ]
    then
        echo "Congrats !! R_drive Mounted !!"
        Print_Further_Instructions_On_screen
    else
        echo "Mounting FAILED !!"
    fi
}

#----------------------------------#
# Function to print instructions; called by mount_R_Drive if successful mount
function Print_Further_Instructions_On_screen() 
{
echo ""
echo " You will have to get access to see the files from R_drive"
echo " Follow below Instructions to fill Access form on opened Curtin IT webportal"
echo " Details are as follows:"
echo "!------------------------------------------------------------------!"
echo "!									 !"
echo "! Website: https://selfservice.curtin.edu.au/CherwellPortal/SSP#0  !"
echo "! Click On: IT Services						 !"
echo "! Enter USERNAME: STUDENT/CURTIN_ID                                !"
echo "! Enter CURTIN PAssword: ********** 				 !"
echo "! Click on 'Shared drive access' 					 !"
echo "! Fill details as below:						 !"
echo "! Shared drive Name: R:\Biomolecular_Model-MANCER-HS00092      	 !"
echo "! check match another users access 				 !"
echo "! matched user name: Ricardo Mancera  				 !"
echo "! Authoriser's user name: Ricardo Mancera  			 !"
echo "! SUBMIT "
echo "!									 !"
echo "!------------------------------------------------------------------!"
echo "!          Thanks by Anji Babu					 !"
echo "!------------------------------------------------------------------!"
echo ""
# xdg-open https://selfservice.curtin.edu.au/CherwellPortal/SSP#0
# register for access rights at cits.curtin.edu.in
# Details: R:\Biomolecular_Model-MANCER-HS00092
}

#----------------------------------#
# Function that checks for root, otherwise cancels program
function Check_for_root() 
{
    root=`id -u`
    if [ $root -eq 0 ]
    then  
        echo " This script is running as Root"
    else
        echo " "
        echo " Root previleges are required to run this script"
        echo " Run as Super User"
        exit
    fi
}

#----------------------------------#
Check_for_root
mount_R_drive
