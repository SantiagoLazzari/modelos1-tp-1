from models.rules.AbstractRule import AbstractRule
from models.laundry_schedule.Garmet import Garmet
from models.laundry_schedule.Load import Load
from models.laundry_schedule.LoadCollection import LoadCollection
import random

class RandomSearchRule(AbstractRule):
	def process(self, garmets:list[Garmet]) -> LoadCollection:
		
		bestLoadCollection = LoadCollection(loads=[])

		for x in range(1000):
			randomShuffle = random.shuffle(garmets)

			loadCollection = LoadCollection(loads=[])
			
			for garmet in garmets:
				loadCollection.addGarmetToCollectionOrAddNewLoad(garmet=garmet)
			
			totalTime = loadCollection.loadTime()
			bestLoadCollectionTime = bestLoadCollection.loadTime()
			print(totalTime)
			
			if totalTime < bestLoadCollectionTime:
				bestLoadsCollection = loadCollection
				
		return bestLoadCollection
