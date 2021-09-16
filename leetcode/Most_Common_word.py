import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub('[^a-zA-Z0-9]',' ',paragraph).lower().split() if word not in banned]
        most = collections.Counter(words).most_common()
        return (most[0][0])
    