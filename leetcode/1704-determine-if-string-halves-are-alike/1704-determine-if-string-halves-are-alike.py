class Solution:
    def halvesAreAlike(self, s: str) -> bool:
                
        if len(re.findall(r'[aeiou]', s[:len(s)//2].lower())) == len(re.findall(r'[aeiou]', s[len(s)//2:].lower())):
            return True
        else:
            return False
        
        
        
        