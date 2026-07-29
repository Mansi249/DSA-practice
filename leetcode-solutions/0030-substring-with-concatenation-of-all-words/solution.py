from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        res = []
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len*num_words
        word_counts = Counter(words)
        for i in range(word_len):
            left = i
            right = i
            seen_words = Counter()
            count = 0
            while right+word_len <= len(s):
                word = s[right:right+word_len]
                right += word_len
                if word in word_counts:
                    seen_words[word] +=1
                    count+=1
                    while seen_words[word]>word_counts[word]:
                        left_word = s[left:left+word_len]
                        seen_words[left_word] -=1
                        count-=1
                        left+=word_len
                    if count == num_words:
                        res.append(left)
                else:
                    seen_words.clear()
                    count = 0
                    left = right
        return res



