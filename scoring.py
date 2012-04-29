#
# Scoring function for asteroid objects
#
from bigfloat import *   # TODO use this
import math

def closeness_weight(obj):
  emoid = 1 if isinstance(obj['GM'], basestring) else obj['moid']
  s = (10-emoid) * 3
  """
  if obj['neo'] != 'N':
    s = s * 1.4
  if obj['pha'] != 'N':
    s = s * 1.2
    """
  s = s * ((1/obj['ad']) * 100)    # penalize aphelion distance
  return s

def price(obj):
  G = 6.67300e-20   # km^3 / kgs^2

  # mass in kg
  exactmass = False
  if isinstance(obj['GM'], basestring):
    mass = 1.47e15
  else:
    exactmass = True
    mass = obj['GM'] / G


  # radius in m
  if obj['diameter'] == '':
    if exactmass:
      # If we know the mass, don't make assumptions about radius
      print 'Disqualified', obj['full_name']
      return -1

    # 5km radius by default
    radius = 5
  else:
    if not exactmass:
      # If we know the radius, don't make assumptions about mass
      print 'Disqualified', obj['full_name']
      return -1

    radius = obj['diameter'] / 2

  # vol in km^3
  vol = 4/3 * math.pi * math.pow(radius, 3) # model as sphere

  # density in kg/km^3
  density = mass / vol

  return density

def score(obj):
  #return price(obj) + closeness_weight(obj)
  return price(obj)