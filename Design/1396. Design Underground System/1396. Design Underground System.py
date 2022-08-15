class UndergroundSystem:

    def __init__(self):
        self.journey_dict = {}
        self.metric_dict = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.journey_dict[id] = (stationName, t)
        
        return
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.journey_dict[id]
        
        
        if(start_station, stationName) in self.metric_dict:
            self.metric_dict[(start_station, stationName)][0] += 1
            self.metric_dict[(start_station, stationName)][1] += (t - start_time)
        else:
            self.metric_dict[(start_station, stationName)] = [1, t - start_time]
        
        return

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_journey_count, total_journey_time = self.metric_dict[(startStation, endStation)]
        averageTime = total_journey_time / total_journey_count
        
        return averageTime
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

class UndergroundSystem: 

    def __init__(self):
        self.checkInData = {}
        self.journeyData = {}
         
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInData[id] = (stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkInData[id]
        del self.checkInData[id]
        
        timeTaken = t - startTime
        journey = (startStation, stationName)
        
        if journey in self.journeyData:
            self.journeyData[journey][0] += 1
            self.journeyData[journey][1] += timeTaken
        else:
            self.journeyData[journey] = [1, timeTaken]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        journey = (startStation, endStation)
        
        count, time = self.journeyData[journey]
        average = time / count
        return average
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)