import re

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        self.jewels = jewels
        self.stones = stones
        count_jewels = re.findall(rf'[{jewels}]', stones)
        return len(count_jewels)


if __name__ == '__main__':
    jewels = Solution()
    assert jewels.numJewelsInStones("aA", "aAAbbbb") == 3
    assert jewels.numJewelsInStones("z", "ZZ") == 0