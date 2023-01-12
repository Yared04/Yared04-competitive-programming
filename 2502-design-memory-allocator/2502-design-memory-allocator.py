class Allocator:

    def __init__(self, n: int):
        self.memory = [0] * n


    def allocate(self, size: int, mID: int) -> int:
        left, right = 0, size-1
        total = sum(self.memory[left: right + 1])
        flag = False
        while not flag and right < len(self.memory):
            if total == 0:
                flag = True
                break
            if right == len(self.memory) - 1:
                break
            total -= self.memory[left]
            left += 1
            right += 1
            total += self.memory[right]
        if flag:
            for i in range(left, right+1):
                self.memory[i] = mID
            return left
        return -1

    def free(self, mID: int) -> int:
        print(self.memory)
        count = 0
        for idx, _id in enumerate(self.memory):
            if _id == mID:
                count += 1
                self.memory[idx] = 0
        return count


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)