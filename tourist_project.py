#lists
destinations = ["Paris, France", "Shanghi, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#var1

#functions
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

#var2
test_destination_index = get_traveler_location(test_traveler)

#print statements
print(test_destination_index)