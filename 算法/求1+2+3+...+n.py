class Solution:
    def __init__(self):
        self.sum = 0

    def Sum_Solution(self, n):
        while n > 0:
            self.sum += n
            n -= 1
        return self.sum


if __name__ == '__main__':
    s = Solution()
    a = s.Sum_Solution(10)
    print(a)
