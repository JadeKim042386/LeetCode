from typing import List
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        for i in range(len(boxes)):
            cnt = 0
            for j in range(len(boxes)):
                if i != j and boxes[j] == '1':
                    cnt += abs(j - i)
            answer.append(cnt)
        return answer
'''
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0]*len(boxes)
        leftCount, leftCost, rightCount, rightCost, n = 0, 0, 0, 0, len(boxes)
        for i in range(1, n):
            if boxes[i-1] == '1':
                leftCount += 1
            leftCost += leftCount # each step move to right, the cost increases by # of 1s on the left
            ans[i] = leftCost
        for i in range(n-2, -1, -1):
            if boxes[i+1] == '1':
                rightCount += 1
            rightCost += rightCount
            ans[i] += rightCost
        return ans
'''