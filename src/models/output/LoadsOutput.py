from models.laundry_schedule.Load import Load

class LoadsOutput():
    def showOutput(self, loads: list[Load]):
        loadCount = 1
        totalTime = 0
        for load in loads:
            print(f"Load {loadCount} has garmets {list(map(lambda x : x.id, load.garmets))} and its total time is {load.totalTime()}")
            loadCount += 1
            totalTime += load.totalTime()

        print(f"total time is {totalTime}")