class TrieSet(object):

    class Node(object):

        def __init__(self):
            self.next = {}
            self.end = False

        def add(self, word):
            if len(word) == 0:
                self.end = True
            elif word[0] in self.next:
                self.next[word[0]].add(word[1:])
            else:
                self.next[word[0]] = TrieSet.Node()
                self.next[word[0]].add(word[1:])

        def has_word(self, word):
            if len(word) == 0:
                return self.end
            elif word[0] in self.next:
                return self.next[word[0]].has_word(word[1:])
            else:
                return False

        def remove(self, word):
            if self.next[word[0]].end == True and len(word) == 1:
                self.next[word[0]].end = False
            if not self.next[word[0]].next and self.next[word[0]].end == False:
                del self.next[word[0]]
            if len(word) > 1:
                self.next[word[0]].remove(word[1:])
                if not self.next[word[0]].next:
                    del self.next[word[0]]

        def has_prefix(self, prefix):
            if prefix == "":
                return True
            elif prefix[0] in self.next:
                return self.next[prefix[0]].has_prefix(prefix[1:])
            else:
                return False

        def get_prefix_trie(self, prefix):
            if len(prefix) == 1:
                return self.next[prefix]
            else:
                return self.next[prefix[0]].get_prefix_trie(prefix[1:])
    
    def __init__(self):
        self.trie = self.Node()


    def add(self, word):
        self.trie.add(word)


    def remove(self, word):
        if self.has_word(word) == False or word == "":
            raise KeyError
        else:
            self.trie.remove(word)


    def has_word(self, word):
        return self.trie.has_word(word)


    def has_prefix(self, prefix):
        if prefix == "":
            return False
        else:
            return self.trie.has_prefix(prefix)


    def get_prefix_trie(self, prefix):
        if not self.has_prefix(prefix):
            raise KeyError
        else:
            return self.trie.get_prefix_trie(prefix)



        
                
                

        
