#python learning 2
#week 6 - OOP

# Week 6 project, building a simple version of blackjack


# Tips for building the thing!:
    # ace is either one or 11, the dealer wins ties
    # you would never count two aces and the dealer must count the ace as 11 unless they go bust
        # hand_value = sum(cards_in_hand, where ace = 1)
        # if no aces:
            #return hand_value
        # else: (one or more aces)
            # if hand_value + 10 <= 21:
                # return hand_value + 10
            # else return hand_value

    # After the player stands provided they aren't bust, need to determine when the dealer goes bust - WHILE LOOP:
    # maap out the potential outcomes with pen and paper, then translate this into logic, then pseudocode, then code
