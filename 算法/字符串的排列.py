import itertools
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        return sorted(list(set(map(''.join, itertools.permutations(ss)))))


if __name__ == '__main__':
    s = Solution()
    print(list(s.Permutation('ab')))
