# -*- coding:utf-8 -*-
class Solution(object):
    def Permutation(self, ss):
        # write code here
        item = ss[0]
        if len(ss) > 1:
            for item in ss:
                item += self.Permutation(ss[1:])
                print(item)
        else:
            return item


if __name__ == '__main__':
    s = Solution()
    print(list(s.Permutation('ab')))
