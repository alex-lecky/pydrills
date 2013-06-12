from unittest import TestCase
from trie import TrieSet

class TrieSetTest(TestCase):

    def setUp(self):
        pass

    def test_trie_has_words_after_adding(self):
        words = ('the', 'quick', 'brown', 'fox', 'jumped', 'over', 'lazy', 'dogs')
        trie = TrieSet()
        for word in words:
            self.assertFalse(trie.has_word(word))
            trie.add(word)
        for word in words:
            self.assertTrue(trie.has_word(word))
            trie.remove(word)
        for word in words:
            self.assertFalse(trie.has_word(word))

    def test_trie_raises_key_error_on_empty_word(self):
        trie = TrieSet()
        self.assertRaises(KeyError, lambda: trie.remove(''))
        self.assertRaises(KeyError, lambda: trie.get_prefix_trie(''))

    def test_trie_raises_key_error_on_missing_word(self):
        trie = TrieSet()
        trie.add('dog')
        self.assertRaises(KeyError, lambda: trie.remove('dogfood'))
        self.assertRaises(KeyError, lambda: trie.get_prefix_trie('dogfood'))

    def test_trie_does_not_have_empty_prefix(self):
        trie = TrieSet()
        self.assertFalse(trie.has_prefix(''))

    def test_trie_has_all_prefixes_of_word(self):
        magic_word = 'abracadabra'
        other_magic_word = 'please'
        trie = TrieSet()
        trie.add(magic_word)
        trie.add(other_magic_word)

        prefix = ''
        bad_prefix = '@'
        for letter in magic_word:
            prefix += letter
            bad_prefix += letter
            self.assertTrue(trie.has_prefix(prefix))
            self.assertFalse(trie.has_prefix(bad_prefix))

        prefix = ''
        bad_prefix = '@'
        for letter in other_magic_word:
            prefix += letter
            bad_prefix += letter
            self.assertTrue(trie.has_prefix(prefix))
            self.assertFalse(trie.has_prefix(bad_prefix))

    def test_get_prefix_trie_will_return_sub_trie(self):
        word = '0123456789101112'
        remaining_word = word
        trie = TrieSet()
        trie.add(word)
        for letter in word:
            remaining_word = remaining_word[1:]
            trie = trie.get_prefix_trie(letter)
            self.assertTrue(trie.has_word(remaining_word))

    def test_putting_it_all_together(self):
        trie = TrieSet()
        trie.add('This Word Is A Sentence')
        trie.add('This')
        trie.add('This American Life')
        trie.add('Think')
        trie.add('Think harder!')

        self.assertFalse(trie.has_word('That Dinkum Thinkum'))

        self.assertTrue(trie.has_prefix('Thi'))
        self.assertTrue(trie.has_prefix('This '))
        self.assertTrue(trie.has_prefix('Think'))
        self.assertFalse(trie.has_prefix('Thunk'))

        self.assertFalse(trie.has_word('This Word'))
        self.assertFalse(trie.has_word('Think hard'))

        sub_trie = trie.get_prefix_trie('Thi')
        self.assertTrue(sub_trie.has_prefix('s'))
        self.assertTrue(sub_trie.has_prefix('nk'))
        self.assertTrue(sub_trie.has_word('s'))
        self.assertTrue(sub_trie.has_word('s American Life'))
        self.assertTrue(sub_trie.has_word('s Word Is A Sentence'))
        self.assertTrue(sub_trie.has_word('nk'))
        self.assertTrue(sub_trie.has_word('nk harder!'))

        sub_trie.remove('s Word Is A Sentence')
        self.assertFalse(trie.has_word('This Word Is A Sentence'))
        self.assertTrue(sub_trie.has_prefix('s'))