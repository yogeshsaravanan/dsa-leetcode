class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait_time=0
        total_wait=0
        for i in customers:
            if i[0]>wait_time:
                wait_time=i[0]+i[1]
            else:
                wait_time+=i[1]
            total_wait+=(wait_time-i[0])
        return total_wait/len(customers)
