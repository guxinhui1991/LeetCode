class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        keysCurrent = self.trie.keys()
        if word in keysCurrent:
            self.trie[word] = self.trie[word] + 1
        else:
            self.trie[word] = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        keysCurrent = self.trie.keys()
        return word in keysCurrent



    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        keysCurrent = self.trie.keys()
        res = False
        for c in keysCurrent:
            if c.startswith(prefix):
                return True






# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)