class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Counters: dict[dict, List[str]] = {}

        for s in strs:
            counter = [0] * 26
            
            for c in s: 
                counter[ord(c) - ord('a')] += 1
            
            key = tuple(counter)

            if Counters.get(key, {}):
                Counters[key].append(s)
            else:
                Counters[key] = []
                Counters[key].append(s)

        return list(Counters.values())