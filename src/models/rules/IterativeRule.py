from models.rules.AbstractRule import AbstractRule
from models.laundry_schedule.Garmet import Garmet
from models.laundry_schedule.LoadCollection import LoadCollection
from models.laundry_schedule.Load import Load

class IterativeRule(AbstractRule):
	def process(self, garmets:list[Garmet]) -> LoadCollection:
		
		loads = []

		for garmet in garmets:
			load = Load()
			load.add(garmet=garmet)
			loads.append(load)


		return LoadCollection(loads=loads)