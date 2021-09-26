
class Garmet():
    def __init__(self, id, restrictions, time):
        '''
        @params
            id: number representing a garmet
            restrictions: List of other Garmet ids that this garmet has restrictions to share loudry
            time: time it takes to this garmet to clean
        '''        
        self.id = id
        self.restricitons = restrictions
        self.time = time

    def __str__(self):
        return f"id: {self.id}, restrictions: {self.restricitons}, time: {self.time}"
