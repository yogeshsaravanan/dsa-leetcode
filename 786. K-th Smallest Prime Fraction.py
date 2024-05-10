class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        a=[]
        numerator=[]
        denominator=[]
        fra=[]
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if arr[i]==arr[j]:
                    pass
                else:
                    t=arr[i]/arr[j]
                    numerator.append(arr[i])
                    denominator.append(arr[j])
                    fra.append(t)
        sorted_fra=sorted(fra)
        kth_fra=sorted_fra[k-1]
        index_of_k =fra.index(kth_fra)
        return [numerator[index_of_k],denominator[index_of_k]]
                
