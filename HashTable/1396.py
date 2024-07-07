class UndergroundSystem(object):

    def __init__(self):
        self.id_entry_time = {}
        self.time_trip = {}

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        if (id in self.id_entry_time.keys()):
            return None
        self.id_entry_time[id] = [stationName, t]

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        journey = (self.id_entry_time[id][0], stationName)
        time =  (t - self.id_entry_time[id][1] )

        if(journey in self.time_trip.keys()):
            self.time_trip[journey].append(time)
        else:
            self.time_trip[journey] = [time]


    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        trip_times = self.time_trip[(startStation, endStation)]
        return sum(trip_times)/len(trip_times)

undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(10, "Leyton", 3)
undergroundSystem.checkOut(10, "Paradise", 8)
undergroundSystem.getAverageTime("Leyton", "Paradise")
undergroundSystem.checkIn(5, "Leyton", 10)
undergroundSystem.checkOut(5, "Paradise", 16)
undergroundSystem.getAverageTime("Leyton", "Paradise")
undergroundSystem.checkIn(2, "Leyton", 21)
undergroundSystem.checkOut(2, "Paradise", 30)
undergroundSystem.getAverageTime("Leyton", "Paradise")