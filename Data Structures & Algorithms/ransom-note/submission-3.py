class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #cannot use remove() here
        for i in magazine:
            if i in ransomNote:
                ransomNote = ransomNote.replace(i,"",1)
                magazine = magazine.replace(i,"",1)
                if len(ransomNote) == 0:
                    return True
        return False