class Solution:
    # def findRelativeRanks(self, score: List[int]) -> List[str]:
    #     a=[]
    #     l=len(score)
    #     sorted_score=sorted(score)
    #     for i in range(l):
    #         s=score[i]
    #         place=l-sorted_score.index(s)
    #         if place == 1:
    #             place='Gold Medal'
    #         elif place ==2:
    #             place='Silver Medal'
    #         elif place ==3:
    #             place='Bronze Medal'
    #         else:
    #             place=str(place)
    #         a.append(place)    
    #     return a
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rank_mapping = {score: medals[i] if i < 3 else str(i + 1) for i, score in enumerate(sorted_score)}
        return [rank_mapping[score] for score in score]
            
            
        
        
