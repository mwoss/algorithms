from typing import List


class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        nums_size = len(nums)
        res = [0] * nums_size
        for i, num in enumerate(nums):
            pos = (i + k) % nums_size
            res[pos] = num

        for i, res_num in enumerate(res):
            nums[i] = res_num


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums) == 0 or k <= 0:
            return

        nums_size = len(nums)

        rotated, start, curr_idx = 0, 0, k % nums_size
        temp, num_to_rotate = nums[0], nums[0]

        while rotated < nums_size - 1:
            while start != curr_idx:
                k_idx = (curr_idx + k) % nums_size
                temp = nums[k_idx]
                nums[k_idx] = num_to_rotate
                num_to_rotate = temp
                curr_idx = (curr_idx + k) % nums_size
                rotated += 1

            start += 1
            curr_idx = start
            num_to_rotate = nums[curr_idx]


class Solution3:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums) == 0 or k <= 0:
            return

        k_idx, nums_len = k % len(nums), len(nums) - 1
        self.reverse(nums, 0, nums_len - k_idx)
        self.reverse(nums, nums_len - k_idx + 1, nums_len)
        self.reverse(nums, 0, nums_len)

    def reverse(self, nums: List[int], lower: int, upper: int):
        # built-in reversed create a new iterable, thus we have to reverse arr manually
        while lower < upper:
            nums[lower], nums[upper] = nums[upper], nums[lower]
            lower += 1
            upper -= 1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    s = Solution3()
    s.rotate(nums, 2)
    print(nums)
