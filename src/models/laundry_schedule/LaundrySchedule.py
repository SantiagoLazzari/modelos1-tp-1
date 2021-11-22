from models.laundry_schedule.Garmet import Garmet
from models.rules.AbstractRule import AbstractRule
from models.laundry_schedule.Load import Load
from models.laundry_schedule.LoadCollection import LoadCollection


class LaundrySchedule():
	def __init__(self, garmets: list[Garmet], rule: AbstractRule):
		self.garmets = garmets
		self.loadCollection = self.loadsWithRule(rule)
			
	def loadsWithRule(self, rule: AbstractRule) -> LoadCollection:
		return rule.process(garmets=self.garmets)