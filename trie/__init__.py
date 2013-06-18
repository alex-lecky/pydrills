class TrieSet(object):

    def __init__(self, head = True):
        self.next = {}
        self.end = False
        self.head = head


    def add(self, word):
        if len(word) == 0:
            self.end = True
        elif word[0] in self.next:
            self.next[word[0]].add(word[1:])
        else:
            self.next[word[0]] = TrieSet(False)
            self.next[word[0]].add(word[1:])

    def remove(self, word):
        if (self.has_word(word) == False or word == "") and self.head == True:
            raise KeyError
        else:
            if self.next[word[0]].end == True and len(word) == 1:
                self.next[word[0]].end = False
            if not self.next[word[0]].next and self.next[word[0]].end == False:
                del self.next[word[0]]
            if len(word) > 1:
                self.next[word[0]].remove(word[1:])
                if not self.next[word[0]].next:
                    del self.next[word[0]]

    def has_word(self, word):
        if len(word) == 0:
            return self.end
        elif word[0] in self.next:
            return self.next[word[0]].has_word(word[1:])
        else:
            return False


    def has_prefix(self, prefix):
        if prefix == "" and self.head == True:
            return False
        else:
            if prefix == "":
                return True
            elif prefix[0] in self.next:
                return self.next[prefix[0]].has_prefix(prefix[1:])
            else:
                return False


    def get_prefix_trie(self, prefix):
        if (not self.has_prefix(prefix)) and self.head == True:
            raise KeyError
        else:
            if len(prefix) == 1:
                sub_trie = self.next[prefix]
                sub_trie.head = True
                return sub_trie
            else:
                return self.next[prefix[0]].get_prefix_trie(prefix[1:])


        
                
                

        
