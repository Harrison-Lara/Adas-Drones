################################################################################
##
## CS 101
## Program: 1
## Name: Harrison Lara
## Email: hrlwwd@mail.umkc.edu
##
## PROBLEM : We need to figure out how many drones are requested by the user,
##           then we need to calculate how many parts are needed to make each
##           of the three drone types. 
##
## ALGORITHM : 
## 1. (basic drones * 4 rotors) + (good drones * 4 rotors) + (ridiculous drones * 8 rotors) = total rotors 
## 2. (basic drones * 2 motors) + (good drones * 4 motors) + (ridiculous drones *12 motors) = total motors     
## 3. (good drones * 1 camera) + (ridiculous * 5 cameras) = total cameras
## 4. (basic drones * 4.2ft wire) + (good drones * 9ft wire) + (ridiculous drones * 22.4ft wire) = total wire
##
## ERROR HANDLING:
##      - You can only type in an integer/float, no letter or special characters.
##
## OTHER COMMENTS:
##      -Basic Drone- 4 Rotors, 2 Motors, 0 Cameras, 4.2 feet of wire
##      -Good Drone- 4 Rotors, 4 Motors, 1 Camera, 9 feet of wire
##      -Ridiculous Drone- 8 Rotors, 12 Motors, 5 Cameras, 22.4 feet of wire
##
################################################################################

#welcome
print ('Welcome to Adas Drones')

#get input from user
basic_int = int(input('How many Basic Drones do you want?==>'))
good_int = int(input('How many Good Drones do you want?==>'))
rid_int = int(input('How many Ridiculous Drones do you want?==>'))

#calculate amount of Rotors, Motors, Cameras and Wire needed
#basic drones parts
num_basic = basic_int #amount of basic drones from input
basic_rt = 4
total_basic_rt = num_basic * basic_rt #amount of rotors
basic_mt = 2
total_basic_mt = num_basic * basic_mt #amount of motors
basic_ftw = 4.2 
total_basic_ftw = num_basic * basic_ftw #amount of wire

#good drones parts
num_good = good_int #amount of good drones from input
good_rt = 4
total_good_rt = num_good * good_rt #amount of rotors
good_mt = 4
total_good_mt = num_good * good_mt #amount of motors
good_cam = 1
total_good_cam = num_good * good_cam #amount of cameras
good_ftw = 9
total_good_ftw = num_good * good_ftw #amount of wire

#ridiculous drones parts
num_rid = rid_int #amount of ridiculous drones from input
rid_rt = 8
total_rid_rt = num_rid * rid_rt #amount of rotors
rid_mt = 12
total_rid_mt = num_rid * rid_mt #amount of motors
rid_cam = 5
total_rid_cam = num_rid * rid_cam #amount of cameras
rid_ftw = 22.4
total_rid_ftw = num_rid * rid_ftw #amount of wire

#combing all three drone parts into total part count
total_rt = total_basic_rt + total_good_rt + total_rid_rt #total rotors
total_mt = total_basic_mt + total_good_mt + total_rid_mt #total motors
total_cam = total_good_cam + total_rid_cam #total cameras
total_ftw = total_basic_ftw + total_good_ftw + total_rid_ftw #total wire

#Output to user
print('Total rotors needed ==> ' + str(total_rt))
print('Total motors needed ==> ' + str(total_mt))
print('Total cameras needed ==> ' + str(total_cam))
print('Total wire needed ==> ' + str (total_ftw) +'ft')








                      
                
                      
                      
                      

