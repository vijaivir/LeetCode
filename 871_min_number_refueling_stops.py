#Credit: lomanhei
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        count = 0
		# Sort the `stations` by the amount of fuel descendingly.
        stations.sort(key = lambda x : x[1], reverse = True)
		# Loop if carrying fuel is enough to finish the course
        while startFuel < target:
            for i in range(len(stations)):
				# Check if next station is within range.
                if stations[i][0] <= startFuel:
                    startFuel += stations[i][1]
                    count += 1
                    stations.pop(i)
                    break
			# No available stations within range OR no more stations left.
            else:
                return -1
        return count
