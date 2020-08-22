#K-th Symbol in Grammar

class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if K == 1:
            return 0
        if K <= (1 << (N - 2)):
            return self.kthGrammar(N - 1, K)
        else:
            return 1 - self.kthGrammar(N - 1, K - (1 << (N - 2)))