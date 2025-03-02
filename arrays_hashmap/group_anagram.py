class Solution:
    def groupAnagrams(self, strs: List[str]):        
        dic=defaultdict(list)
        for str in strs:            
            sorted_str=''.join(sorted(str))
            dic[sorted_str].append(str)        
        return(list(dic.values()))