from models.rules.AbstractRule import AbstractRule
from models.laundry_schedule.Garmet import Garmet
from models.laundry_schedule.LoadCollection import LoadCollection
from models.laundry_schedule.Load import Load

class MaxToMinRule(AbstractRule):
	def process(self, garmets:list[Garmet]) -> LoadCollection:
		loadCollection = LoadCollection(loads=[])
		garmets.sort(key=lambda x: x.time, reverse=True)
		for garmet in garmets:
			loadCollection.addGarmetToCollectionOrAddNewLoad(garmet=garmet)

		return loadCollection
