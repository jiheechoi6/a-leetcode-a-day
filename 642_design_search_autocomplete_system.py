class Node:
    def __init__(self):
        self.children = {}
        self.sentences = []

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.freq_cache = defaultdict(int)
        self.root = Node()
        self.prefix = ""

        for i, s in enumerate(sentences):
            self._add_sentence(s)
            self.freq_cache[s] = times[i]
    
    def _add_sentence(self, sentence):
        node = self.root
        for ch in sentence:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
            node.sentences.append(sentence)

    def _search(self):
        node = self.root
        for ch in self.prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        
        return [(-self.freq_cache[sen], sen) for sen in node.sentences]

    def input(self, c: str) -> List[str]:
        if c != '#':
            self.prefix += c
            sens = self._search()

            return [sen[1] for sen in sorted(sens)[:3]]
        else:
            if self.prefix not in self.freq_cache: self._add_sentence(self.prefix)
            self.freq_cache[self.prefix] += 1
            self.prefix = ""

            return []


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
