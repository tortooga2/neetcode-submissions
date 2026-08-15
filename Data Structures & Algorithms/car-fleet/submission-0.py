class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Sort cars by position descending (closest to target first)
        cars = sorted(list(zip(position, speed)), reverse=True)

        output = 0
        curr_max_time = 0.0

        # Instead of simulating second-by-second, compare arrival times
        for p, s in cars:
            arrival_time = (target - p) / s
            
            # If this car takes longer than the fleet ahead, it starts a new fleet
            if arrival_time > curr_max_time:
                output += 1
                curr_max_time = arrival_time
                
        return output