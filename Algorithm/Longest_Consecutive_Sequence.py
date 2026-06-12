class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        answer=0
        for i in seen:
            current=i
            streak = 1 
            if current -1 not in seen:
                while current+1 in seen:
                    current+=1
                    streak+=1
            answer=max(answer,streak)
        return answer