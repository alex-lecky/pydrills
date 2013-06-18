class TrieSet(object):
    """Creates a trie that stores and returns strings"""
    
    def __init__(self, head = True):
        """Creates the head node of the trie"""
        self.next = {}          #Creates an empty dictionary of nodes
        self.end = False        #This node is not the end of a word
        self.head = head        #This node is the head node of a tree


    def add(self, word):
        """Adds a word by creating nodes"""
        if self.head == True and word == "":    #Check for empty input
            raise KeyError
        if len(word) == 0:                      #Is this node the end of a word?
            self.end = True
        elif word[0] in self.next:              #If the next node exists
            self.next[word[0]].add(word[1:])    #add the word to it
        else:
            self.next[word[0]] = TrieSet(False) #If the next node does not exist
            self.next[word[0]].add(word[1:])    #create it and then add the word

    def remove(self, word):
        """Removes a word and its unused nodes"""
        #Runs checks that only apply to the head node
        #
        #Resets to False a node that was the end of a word
        #Removes a node if it is not used by any other word
        #Recursively calls remove() until it reaches the end and works back
        if self.head == True and (self.has_word(word) == False or word == ""):
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
        """Returns True if a word exists in the trie"""
        if len(word) == 0:                      
            return self.end
        elif word[0] in self.next:
            return self.next[word[0]].has_word(word[1:])
        else:
            return False


    def has_prefix(self, prefix):
        """Returns True if a prefix exists in the trie"""
        if self.head == True and prefix == "":
            return False
        else:
            if prefix == "":
                return True             
            elif prefix[0] in self.next:
                return self.next[prefix[0]].has_prefix(prefix[1:])
            else:
                return False


    def get_prefix_trie(self, prefix):
        """Returns a TrieSet object containing all nodes after a prefix"""
        if self.head == True and (not self.has_prefix(prefix)):
            raise KeyError
        else:
            if len(prefix) == 1:
                sub_trie = self.next[prefix]
                sub_trie.head = True
                return sub_trie
            else:
                return self.next[prefix[0]].get_prefix_trie(prefix[1:])


        
                
                

        
