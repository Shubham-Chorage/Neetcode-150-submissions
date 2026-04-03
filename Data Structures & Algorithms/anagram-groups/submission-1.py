from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dictionary = defaultdict(list)

        for str in strs:
            key = tuple(sorted(str))
            if str not in dictionary:
                dictionary[key].append(str)
        #print (dictionary.values())
        return list(dictionary.values())
