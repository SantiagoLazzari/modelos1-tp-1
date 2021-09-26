from models.laundry_schedule.Garmet import Garmet
from models.rules.AbstractRule import AbstractRule
from models.laundry_schedule.Load import Load

class LaundrySchedule():
    
    def __init__(self, garmets: list[Garmet]):
        self.garmets = garmets
         
    def loadsWithRule(self, rule: AbstractRule) -> list[Load]:
        return rule.process(garmets=self.garmets)