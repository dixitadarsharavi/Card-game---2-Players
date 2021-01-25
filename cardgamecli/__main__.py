import random

# Declaring constant values
CARD_OCCURANCE_TIME = 4
MIN_VALUE_OF_CARD = 1
MAX_VALUE_OF_CARD = 10
REQUIRED_LENGTH_OF_DECK = 40

# Length of the list
def len_of_deck(lst):
    if len(lst) != REQUIRED_LENGTH_OF_DECK:
        raise ValueError("The length of the deck should be 40.")
    return len(lst)

# Shuffeling the cards
def deck_shuffle(lst):
    random.shuffle(lst)
    return lst

# Compare the cards and determine the greatest or equal
def compare_cards(player_1_card,player_2_card):
    if player_1_card > player_2_card:
        return "Player 1 wins this round"
    elif player_2_card > player_1_card:
        return "Player 2 wins this round"
    else:
        return "No winner in this round"

# Shuffle and distribute cards from discard pile
def distribure_discard_pile(player_1_draw_size,player_2_draw_size):
    if player_1_draw_size == 0 and player_2_draw_size == 0:
        return "Shuffle discard_pile of both players"
    if player_1_draw_size == 0:
        return "Player 1 discard_piles will be shuffled"
    if player_2_draw_size == 0:
        return "Player 2 discard_piles will be shuffled"

# Start the game
def start_game(shuffled_deck):

    # Create draw pile for Players
    player_1_draw_pile = []
    player_2_draw_pile = []

    # Stack cards for each player
    i = 0
    while i < len(shuffled_deck):
        player_1_draw_pile.append(shuffled_deck[i])
        i = i +1
        player_2_draw_pile.append(shuffled_deck[i])
        i = i +1 

    # Create discarded pile for players
    player_1_discard_pile = []
    player_2_discard_pile = []

    # Total cards for each player:
    player_1_total_cards = len(player_1_draw_pile) + len(player_1_discard_pile)
    player_2_total_cards = len(player_2_draw_pile) + len(player_2_discard_pile)
    
    # When both players are showing same cards, store the cards till the player wins in the next round
    tmp_list = []

    # LIFO during drawing the cards
    j = len(player_1_draw_pile) - 1
    k = len(player_2_draw_pile) - 1

    while True:
        # Player 2 wins the game if Player 1 runs out of cards
        if len(player_1_draw_pile) == 0 and len(player_1_discard_pile) == 0:
            print("\nPlayer 2 wins the game!")
            break

        # Player 1 wins the game if Player 2 runs out of cards
        elif len(player_2_draw_pile) == 0 and len(player_2_discard_pile) == 0:
            print("\nPlayer 1 wins the game!")
            break
        
        # For distributing discarded_pile after shuffling
        elif len(player_1_draw_pile) == 0 or len(player_2_draw_pile) == 0:
            dist_discard_piles = distribure_discard_pile(len(player_1_draw_pile),len(player_2_draw_pile))
            # If both players run out of cards in draw_pile 
            if dist_discard_piles == "Shuffle discard_pile of both players":
                random.shuffle(player_1_discard_pile)
                for x in player_1_discard_pile:
                    player_1_draw_pile.append(x)
            
                random.shuffle(player_2_discard_pile)
                for y in player_2_discard_pile:
                    player_2_draw_pile.append(y)
                
                player_1_discard_pile.clear()
                player_2_discard_pile.clear()
                j = len(player_1_draw_pile) - 1
                k = len(player_2_draw_pile) - 1
            
            # If Player 1 runs out of cards in draw_pile 
            elif dist_discard_piles == "Player 1 discard_piles will be shuffled":
                random.shuffle(player_1_discard_pile)
                for x in player_1_discard_pile:
                    player_1_draw_pile.append(x)
                player_1_discard_pile.clear()
                j = len(player_1_draw_pile) - 1
            
            # If Player 2 runs out of cards in draw_pile
            elif dist_discard_piles == "Player 2 discard_piles will be shuffled":
                random.shuffle(player_2_discard_pile)
                for y in player_2_discard_pile:
                    player_2_draw_pile.append(y)
                player_2_discard_pile.clear()
                k = len(player_2_draw_pile) - 1
        
        else:
            print(f"\nPlayer 1 ({player_1_total_cards} cards):",player_1_draw_pile[j])
            print(f"Player 2 ({player_2_total_cards} cards):",player_2_draw_pile[k])
            
            # Compare cards and declare winner for the round
            result = compare_cards(player_1_draw_pile[j],player_2_draw_pile[k])
            if result == "Player 1 wins this round":
                print(result)
                player_1_discard_pile.append(player_1_draw_pile[j])
                player_1_discard_pile.append(player_2_draw_pile[k])
                player_1_discard_pile.extend(tmp_list)
                player_1_total_cards = player_1_total_cards + 1 + len(tmp_list)
                player_2_total_cards = player_2_total_cards - 1
                tmp_list.clear()
            elif result == "Player 2 wins this round":
                print(result)
                player_2_discard_pile.append(player_1_draw_pile[j])
                player_2_discard_pile.append(player_2_draw_pile[k])
                player_2_discard_pile.extend(tmp_list)
                player_2_total_cards = player_2_total_cards + 1 + len(tmp_list)
                player_1_total_cards = player_1_total_cards - 1
                tmp_list.clear()
            else:
                print("No winner in this round")
                tmp_list.append(player_1_draw_pile[j])
                tmp_list.append(player_2_draw_pile[k])
                player_1_total_cards = player_1_total_cards - 1
                player_2_total_cards = player_2_total_cards - 1
            player_1_draw_pile.pop()
            player_2_draw_pile.pop()
            j = j - 1
            k = k - 1

def main():
    my_cards = []

    # Creating a deck of size 40
    for i in range(CARD_OCCURANCE_TIME):
        for j in range(MIN_VALUE_OF_CARD,MAX_VALUE_OF_CARD + 1,1):
            my_cards.append(j)
    print(my_cards)
    # Record shuffled cards
    shuffled_deck = deck_shuffle(my_cards)

    # Start the game
    start_game(shuffled_deck)

if __name__ == '__main__':
    main()