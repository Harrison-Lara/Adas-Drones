# Adas-Drones

PROBLEM : We need to figure out how many drones are requested by the user,
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
