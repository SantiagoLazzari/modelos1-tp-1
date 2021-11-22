from math import perm
from models.rules.AbstractRule import AbstractRule
from models.laundry_schedule.Garmet import Garmet
from models.laundry_schedule.LoadCollection import LoadCollection
from models.laundry_schedule.Load import Load
import random


class MaxToMinGeneticClosePremutation(AbstractRule):

	def process(self, garmets:list[Garmet]) -> LoadCollection:
		garmets.sort(key=lambda x: x.time, reverse=True)
		bestLoadCollectionSpecies = list[LoadCollection]()
		# hyperparameters
		speciesCount = 5
		generationsCount = 100
		childsPerSpecies = 2
		pivotMaxSize = 6

		# Initial Species
		for species in range(speciesCount):
			loadCollection = LoadCollection(loads=[])
			for garmet in garmets:
				loadCollection.addGarmetToCollectionOrAddNewLoad(garmet=garmet)
			bestLoadCollectionSpecies.append(loadCollection)

		# Create Generations
		for generation in range(generationsCount):
			generationLoadCollections = bestLoadCollectionSpecies.copy()
			for species in bestLoadCollectionSpecies:
				for child in range(childsPerSpecies):
					childGarmets = species.garmets.copy()
					x = random.randrange(len(garmets))
					y = None 
					pivotSize = random.randrange(pivotMaxSize)
					if x >= pivotMaxSize:
						y = x - pivotSize
					else:
						y = x + pivotSize
					y = random.randrange(len(garmets))
					oldX = childGarmets[x]
					oldY = childGarmets[y]
					childGarmets[x] = oldY
					childGarmets[y] = oldX 
					childLoadCollection = LoadCollection(loads=[])
				
					for garmet in childGarmets:
						childLoadCollection.addGarmetToCollectionOrAddNewLoad(garmet=garmet)
					generationLoadCollections.append(childLoadCollection)

			random.shuffle(generationLoadCollections)
			generationLoadCollections.sort(key=lambda x: x.loadTime())
			print(f"generation: {generation}, {list(map(lambda x: x.loadTime(),generationLoadCollections))}")
			bestLoadCollectionSpecies = generationLoadCollections[:speciesCount]

		return bestLoadCollectionSpecies[0]