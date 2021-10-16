class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots = slots1 + slots2
        if len(slots) == 0:
            return []
        slots.sort()
        
        latest_end = 0
        
        for slot in slots:
            if (latest_end-slot[0])>=duration and (slot[1]-slot[0])>=duration:
                return [slot[0], slot[0]+duration]
            
            latest_end = max(latest_end, slot[1])
            
        return []
