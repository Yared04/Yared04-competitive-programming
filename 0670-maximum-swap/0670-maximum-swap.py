class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(map(int, list(str(num))))
        number_idx = defaultdict(list)
        to_swap = 0
        heap = []
        for idx, number in enumerate(num_list):
            heappush(heap, (-number, idx))
            number_idx[number].append(idx)
        while heap:
            num, idx = heappop(heap)
            if idx == to_swap:
                to_swap += 1
                continue
            idx = number_idx[-num][-1]
            num_list[idx], num_list[to_swap] = num_list[to_swap], num_list[idx]
            break
            
        num_list = list(map(str, num_list))
        return int("".join(num_list))