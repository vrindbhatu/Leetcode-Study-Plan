class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        hour = (hour % 12 + minutes/60) * 30
        minute = minutes * 6
        
        angle = abs(hour-minute)
        
        if angle > 180:
            return 360 -  angle
        else:
            return angle
        