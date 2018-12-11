class Solution:
    def __init__(self):
        self.L_A = []
        self.L_B = []

    def push(self, node):
        self.L_A.append(node)
        # write code here

    def pop(self):
        if self.L_B:
            return self.L_B.pop()
        elif not self.L_A:
            return None
        else:
            while self.L_A:
                self.L_B.append(self.L_A.pop())
            return self.L_B.pop()


if __name__ == '__main__':
    s = Solution()
    for i in range(1, 6):
        s.push(i)
    print(s.pop())
    print(s.pop())
    print(s.pop())
