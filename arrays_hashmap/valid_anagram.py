class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        
        counter_s={}
        counter_t={}
        for char in s:
            counter_s[char]=s.count(char)
        for char in t:
            counter_t[char]=t.count(char)
        print(counter_s)
        print(counter_t)
        value='True'
        for char in s:
            if char in counter_t:
                if counter_s[char]!=counter_t[char]:
                    value='False'
                    break
            else:
                value='False'

        return False if value=='False' else True

if __name__=='__main__':
    sol=Solution()
    value=sol.isAnagram("anagram","naagram")
    print(value)