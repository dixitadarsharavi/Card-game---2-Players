import unittest
from cardgamecli.__main__ import len_of_deck,deck_shuffle,compare_cards,distribure_discard_pile

class TestCalc(unittest.TestCase):
    def test_deckSize(self):
        my_lst = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(len_of_deck(my_lst),40)
    def test_is_shuffled(self):
        my_lst = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
        self.assertNotEqual(deck_shuffle(my_lst),[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10])

    def test_compare_cards(self):
        # Note: compare_cards(player_1_card_value,player_2_card_Value)
        self.assertEqual(compare_cards(2,1),"Player 1 wins this round")
        self.assertEqual(compare_cards(1,6),"Player 2 wins this round")
        self.assertEqual(compare_cards(1,1),"No winner in this round")
    
    def test_shuffle_discarded_cards(self):
        # Note: distribure_discard_pile(len(player_1_deck),len(player_2_deck))
        self.assertEqual(distribure_discard_pile(0,0),"Shuffle discard_pile of both players")
        self.assertEqual(distribure_discard_pile(0,1),"Player 1 discard_piles will be shuffled")
        self.assertEqual(distribure_discard_pile(1,0),"Player 2 discard_piles will be shuffled")
    
    def test_values(self):
        # value errors are thrown for invalid decksize
        self.assertRaises(ValueError,len_of_deck,["asbhdfagzsu"])
        self.assertRaises(ValueError,len_of_deck,[1,2,3,4])
