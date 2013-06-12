# trie

## Assignments

### Implement TrieSet

A trie (sometimes called a prefix tree) is a specialized tree data structure that provides efficient insertion, lookup,
and removal.  But lots of other structures do that!  What makes a trie special?  It can efficiently determine if
elements starting with a prefix exist.  In fact, this is as easy for it as normal lookup.  Witchcraft, you say?

No!  Science!

Tries are implemented as nodes in a tree that maintains a set of children keyed on a letter.  Storing the word 'dog'
would result in a chain of four nodes, `node - 'd' -> node -> 'o' -> node -> 'g' -> node`.  Checking for the existence
of a word or prefix is simply a matter of traversing the tree.

A cursory google should turn up detailed explanations, as well as algorithms and example implementations.

Your assignment is create a class, `TrieSet`, which will .You must implement the `TrieSet` class with the following
methods:
* `add`:  add a word to the TrieSet.  After doing so, `has_word` should return True, as should `has_prefix` on all
non-zero length prefixes.
* `remove`: remove a word from the TrieSet.
* `has_word`: returns True if a word has been `add`ed to the TrieSet, else False.
* `has_prefix`: returns True if a prefix exists, else False.
* `get_prefix_trie`: returns the sub-trie under a prefix.  If a trie contains the words 'one', 'on', and 'ok',
`get_prefix_trie('o')` will return a trie containing the words 'ne', 'n', and 'k'.

This class has been stubbed out for you in `__init__.py`.

#### Tips
* Consider what sorts of data structures you will need to implement `TrieSet`.
* The tests in `test.py` are your friends.  Read them.  Run them as you code.
* The tests are not exhaustive.  You might need to write more as you work.

#### Challenges
* Will the TrieSet work with objects other than strings?  What about tuples and lists?
