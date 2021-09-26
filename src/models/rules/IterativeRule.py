from typing import AbstractSet


from models.rules.AbstractRule import AbstractRule
from models.laundry_schedule.Garmet import Garmet
from models.laundry_schedule.Load import Load

class IterativeRule(AbstractRule):
    def process(self, garmets:list[Garmet]) -> list[Load]:
        
        load = Load()

        for garmet in garmets: 
            load.add(garmet=garmet)


        return [load]