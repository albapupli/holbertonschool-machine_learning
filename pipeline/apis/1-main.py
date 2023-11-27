#!/usr/bin/env python3

"""
By using the Swapi API, create a method that returns the list of names of the home planets of all sentient species.

Prototype: def sentientPlanets():
Don’t forget the pagination
sentient type is either in the classification or designation attributes.
"""

"""
Test file
"""
sentientPlanets = __import__('1-sentience').sentientPlanets
planets = sentientPlanets()
for planet in planets:
    print(planet)