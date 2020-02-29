#Each ornament is a square containing 9 squares with the middle one of a fixed colour
#The other squares can be either black or white
#below a string of an 8 digit binary number to represent the colours of the squares
#for example 10101010 represents a square with the corners coloured black and the rest white
#while 01010101 has all of the corners coloured white and the rest black

#Here every possible ornament can be represent in binary form with the digits 0-255

def gen_ornaments():
  ornament_dict = {}

  #Loop through possible ornaments
  for i in range(256):
    x = format(i, '08b')#string binary representation of the square


    new_ornament = True # assume new ornament

    #check if any rotation or reflection in already accounted for
    if rotate_pi(x) in ornament_dict:
      new_ornament = False

    if rotate_clock(x) in ornament_dict:
      new_ornament = False

    if rotate_anticlock(x) in ornament_dict:
      new_ornament = False

    if vertical_reflection(x) in ornament_dict:
      new_ornament = False

    if horizontal_reflection(x) in ornament_dict:
      new_ornament = False
    
    if top_right_diagonal_reflection(x) in ornament_dict:
      new_ornament = False

    if top_left_diagonal_reflection(x) in ornament_dict:
      new_ornament = False

    #If not add it to the dictionary
    if new_ornament:
      ornament_dict[x] = x

  #print result
  print(len(ornament_dict))



def rotate_pi(ornament):
  newOrnament = ornament[4:]+ornament[:4]
  return newOrnament

def rotate_clock(ornament):
  newOrnament = ornament[6:]+ornament[:6]
  return newOrnament

def rotate_anticlock(ornament):
  newOrnament = ornament[2:]+ornament[:2]
  return newOrnament

def vertical_reflection(orn):
  newOrnament = orn[2]+orn[1]+orn[0]+orn[7]+orn[6]+orn[5]+orn[4]+orn[3]
  return newOrnament

def horizontal_reflection(orn):
  newOrnament = orn[6]+orn[5]+orn[4]+orn[3]+orn[2]+orn[1]+orn[0]+orn[7]
  return newOrnament

def top_right_diagonal_reflection(orn):
  newOrnament = orn[4]+orn[3]+orn[2]+orn[1]+orn[0]+orn[7]+orn[6]+orn[5]
  return newOrnament

def top_left_diagonal_reflection(orn):
  newOrnament = orn[0]+orn[7]+orn[6]+orn[5]+orn[4]+orn[3]+orn[2]+orn[1]
  return newOrnament

gen_ornaments()

