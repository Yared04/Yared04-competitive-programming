       
class Solution:
    def count_to_k(self,k,start):
        if start == k:
            return self.count
        if start < k:
            start += 4
            self.count += 1
            self.count_to_k(k,start)
        elif start > k:
            start -= 1
            self.count += 1
            self.count_to_k(k, start)
        # print(count)
    def run(self,k):
        self.count = 0
        from31 = self.count_to_k(k,31)
        from32 = self.count_to_k(k,32)
        print(from31,from32)

t = int(input())
for i in range(t):
        k = int(input())
        one = Solution()
        one.run(k)