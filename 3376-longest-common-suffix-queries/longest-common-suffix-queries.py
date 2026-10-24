class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        trie = {}
        best = {}

        shortest = min(range(len(wordsContainer)),
                       key=lambda i: (len(wordsContainer[i]), i))

        for i, word in enumerate(wordsContainer):
            node = trie
            best[id(node)] = shortest
            for ch in reversed(word):
                node = node.setdefault(ch, {})
                best[id(node)] = min(
                    [best.get(id(node), i), i],
                    key=lambda j: (len(wordsContainer[j]), j)
                )

        ans = []
        for query in wordsQuery:
            node = trie
            res = shortest

            for ch in reversed(query):
                if ch not in node:
                    break
                node = node[ch]
                res = best[id(node)]

            ans.append(res)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna