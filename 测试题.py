#如果a+b+c=1000，且a^2+b^2=c^2(a,b,c自然数)所有a,b,c组合
#1:枚举
# for a in range(0,1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a+b+c == 1000 and a**2+b**2==c**2:
#                 print("a, b, c:%d, %d, %d" % (a, b, c))
# for a in range(0,1001):
#     for b in range(0, 1001):
#         c = 1000-a-b
#         if a**2+b**2==c**2:
#             print("a, b, c:%d, %d, %d" % (a, b, c))
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num],index]
            hashmap[num] = index
        return None
nums = [1,2,3,6]
targets = 7
int = Solution()
print(int)
