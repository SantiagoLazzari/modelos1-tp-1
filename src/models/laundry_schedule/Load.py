from models.laundry_schedule.Garmet import Garmet


class Load():
    
    def __init__(self):
        self.garmets = list[Garmet]()

    def add(self, garmet: Garmet):
        self.garmets.append(garmet)

    def totalTime(self):
        time = 0
        for garmet in self.garmets:
            if garmet.time >= time:
                time = garmet.time

        return time

    def isGarmetsCompatible(self, garmets: list[Garmet]) -> bool:
        loadGarmetIds = list(map(lambda x : x.id, garmets))
        loadGarmetIncompatibleIds = []

        for garmet in garmets:
            loadGarmetIncompatibleIds += garmet.restricitons

        for loadGarmetId in loadGarmetIds:
            if loadGarmetId in loadGarmetIncompatibleIds:
                return False

        return True

    def isLoadCompatible(self) -> bool:
        return self.isGarmetsCompatible(garmets=self.garmets)

    def canAdd(self, garmet: Garmet) -> bool:
        garmetsCandidate = self.garmets.copy()
        garmetsCandidate.append(garmet)
        return self.isGarmetsCompatible(garmets=garmetsCandidate)