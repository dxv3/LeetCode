class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        final = ""
        for word in words:
            if len(word) < 3:
                final += word.lower() + " "
            elif len(word) >= 3:
                final += word[0].capitalize()+word[1:len(word)].lower() + " "
        
        return final.strip()


sol = Solution()
result = sol.capitalizeTitle("capiTalIze tHe titLe")
print(result)