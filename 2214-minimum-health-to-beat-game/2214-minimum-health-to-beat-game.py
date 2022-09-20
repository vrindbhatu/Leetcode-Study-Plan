class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        
        max_damage = max(damage)
        sum_total_damage = sum(damage)
        
        if armor >= max_damage:
            return sum_total_damage - max_damage + 1
        
        else:
            return sum_total_damage - armor + 1
        