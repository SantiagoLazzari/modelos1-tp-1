from models.rules.AbstractRule import AbstractRule
from models.laundry_schedule.Garmet import Garmet
from models.laundry_schedule.Load import Load
from models.laundry_schedule.LoadCollection import LoadCollection
import random

class RandomSearchRule(AbstractRule):
	def process(self, garmets:list[Garmet]) -> LoadCollection:
		
		bestLoadCollection = None

		for x in range(10):
			randomShuffle = random.shuffle(garmets)
			loadCollection = LoadCollection(loads=[])
			
			for garmet in garmets:
				loadCollection.addGarmetToCollectionOrAddNewLoad(garmet=garmet)

			if bestLoadCollection == None:
				bestLoadCollection = loadCollection
				continue
			
			totalTime = loadCollection.loadTime()
			bestLoadCollectionTime = bestLoadCollection.loadTime()
			print(totalTime)
			if totalTime < bestLoadCollectionTime:
				bestLoadCollection = loadCollection

		return bestLoadCollection
