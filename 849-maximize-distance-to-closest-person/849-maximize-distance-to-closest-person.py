class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left_closest_seat = [float('inf') for i in range(len(seats))]
        right_closest_seat = [float('inf') for i in range(len(seats))]
        
        closest_index = float('inf')
        for i in range(len(seats)):
            if seats[i] == 1:
                closest_index = i
            left_closest_seat[i] = closest_index
            
        closest_index = float('inf')
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 1:
                closest_index = i
                
            right_closest_seat[i] = closest_index
            
            
        max_distance = -1
        for i in range(len(seats)):
            dist = min(abs(i - left_closest_seat[i]),abs(right_closest_seat[i] - i))
            if dist > max_distance:
                max_distance = dist
                
        return max_distance
        