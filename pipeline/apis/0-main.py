#!/usr/bin/env python3

"""
By using the Swapi API, create a method that returns the list of ships that can hold a given number of passengers:

Prototype: def availableShips(passengerCount):
Don’t forget the pagination
If no ship available, return an empty list.
"""

"""
Test file
"""

availableShips = __import__('0-passengers').availableShips
ships = availableShips(4)
for ship in ships:
    print(ship)