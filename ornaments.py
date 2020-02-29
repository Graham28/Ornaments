import copy

def gen_ornaments():
  ornament_dict = {}
  for i in range(256):
    x = format(i, '08b')
    new_ornament = True

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

    if new_ornament:
      ornament_dict[x] = x

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

