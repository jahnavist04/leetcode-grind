from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):

        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)

        word_count = Counter(words)
        result = []

        for i in range(word_len):
            left = i
            seen = Counter()

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]

                if word in word_count:
                    seen[word] += 1

                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len

                    if j + word_len - left == total_len:
                        result.append(left)

                else:
                    seen.clear()
                    left = j + word_len

        return result