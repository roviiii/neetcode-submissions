class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}

        for word in strs:
            alphabetFrequencyList = [0] * 26

            for letter in word:
                alphabetFrequencyList[ord(letter) - ord("a")] += 1

            frequencyListTuple = tuple(alphabetFrequencyList)

            if frequencyListTuple not in results:
                results[frequencyListTuple] = []

            results[frequencyListTuple].append(word)

        endList = []

        for key in results:
            endList.append(results[key])

        return endList