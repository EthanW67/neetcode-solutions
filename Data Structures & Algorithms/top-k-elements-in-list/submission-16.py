class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frequency sort the list
        freqdict = {}

        for i in range(len(nums)):
            freqdict[nums[i]] = 1 + freqdict.get(nums[i], 0)
        # print(freqdict)
        reverseList = []

        for value, count in freqdict.items():
            reverseList.append([count, value])
            reverseList.sort()
        # print(reverseList)
        results = []
        while k > 0:
            results.append(reverseList.pop()[1])
            k -= 1
        # print(results)
        return results




        # change and sort the freq

        # get results
