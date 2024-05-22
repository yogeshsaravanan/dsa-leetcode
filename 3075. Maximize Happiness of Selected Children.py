class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        sorted_happy= sorted(happiness)
        val=0
        count=0
        while k>0:
            t=sorted_happy.pop()
            if t >= count:
                val+=t-count
            else:
                val+=0
            count+=1
            k-=1
        return val
            
        
