class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for number in seen:

            # Only start counting if this is the beginning of a sequence
            if number - 1 not in seen:

                sequenceLength = 1
                currentNumber = number

                while currentNumber + 1 in seen:
                    currentNumber += 1
                    sequenceLength += 1

                longest = max(longest, sequenceLength)

        return longest
            
