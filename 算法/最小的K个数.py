class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput):
            return []
        return sorted(tinput)[:k]
        # write code here


if __name__ == '__main__':
    s = Solution()
    a = s.GetLeastNumbers_Solution(tinput=[4, 5, 1, 6, 2, 7, 3, 8], k=4)
    print(a)
