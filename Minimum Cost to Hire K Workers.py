import heapq

def mincostToHireWorkers(quality, wage, k):
    nQuality = len(quality)
    minCost = float("inf")
    qualityTillNow = 0
    wageQualityRatio = []

    for i in range(nQuality):
        heapq.heappush(wageQualityRatio, (wage[i] / quality[i], quality[i]))

    highQualityWorkers = []

    for i in range(nQuality):
        ratio, qua = heapq.heappop(wageQualityRatio)
        qualityTillNow += qua
        heapq.heappush(highQualityWorkers, -qua)

        if len(highQualityWorkers) > k:
            qualityTillNow += heapq.heappop(highQualityWorkers)

        if len(highQualityWorkers) == k:
            minCost = min(minCost, qualityTillNow * ratio)

    return minCost

print(mincostToHireWorkers([10,20,5],[70,50,30],2))
