import random, sys

HEARTS      = chr(9829)
DIAMONDS    = chr(9830)
SPADES      = chr(9824)
CLUBS       = chr(9827)
BACKSIDE = 'backside'


def main():
    money = 5000
    while True:
        if money <= 0:
            print("You're out of money! You lose!")
            sys.exit()

        print(f"Money: {money}")
        bet = get_bet(money)
        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        print(f"Bet: {bet}")
        while True:
            display_hands(player_hand, dealer_hand, False)
            print()

            if get_hand_value(player_hand) > 21:
                break

            move = get_move(player_hand, money - bet)
            if move == 'd':
                additional_bet = get_bet(min(bet, (money - bet)))
                bet += additional_bet
                print(f"Bet increased to {bet}")
                print(f"Bet: {bet}")
            if move in ('h', 'd'):
                new_card = deck.pop()
                rank, suit = new_card
                print(f"You drew a {rank} of {suit}")
                player_hand.append(new_card)
                if get_hand_value(player_hand) > 21:
                    continue
            if move in ('s', 'd'):
                break

        if get_hand_value(player_hand) <= 21: 
            while get_hand_value(dealer_hand) < 17:
                print('Dealer hits...')
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)

                if get_hand_value(dealer_hand) > 21:
                    break
                input('Press Enter to continue...')
                print('\n\n')
        
        display_hands(player_hand, dealer_hand, True)
        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)
        if dealer_value > 21:
            print(f"Dealer busts! You win {bet}!")
            money += bet
        elif (player_value > 21) or (player_value < dealer_value):
            print('You lose!')
            money -= bet
        elif player_value > dealer_value:
            print(f"You win ${bet}!")
            money += bet
        elif player_value == dealer_value:
            print('Tie! Returning money...')

        input('Press Enter to continue...')
        print('\n\n')


def get_bet(max_bet):
    while True:
        print(f"How much will you bet? (1 .. {max_bet}, or QUIT)")
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Goodbye')
            sys.exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet


def get_deck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck 


def get_hand_value(hand):
    value = 0
    aces_count = 0
    
    for card in hand:
        rank = card[0]
        if rank == 'A':
            aces_count += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)

    value += aces_count
    for i in range(aces_count):
        if value + 10 <= 21:
            value += 10
    
    return value 


def display_hands(player_hand, dealer_hand, show_dealer_hand):
    print()
    if show_dealer_hand:
        print(f"DEALER: {get_hand_value(dealer_hand)}")
        display_cards(dealer_hand)
    else:
        print('DEALER: ???')
        display_cards([BACKSIDE] + dealer_hand[1:])
    print(f"PLAYER: {get_hand_value(player_hand)}")
    display_cards(player_hand)


def display_cards(hand):
    rows = ['', '', '', '', '']

    for card in hand:
        rows[0] += ' ___  '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '| # | '
            rows[3] += '| ##| '
        else:
            rank, suit = card
            rows[1] += f"|{rank.ljust(2)} | "
            rows[2] += f"| {suit} | "
            rows[3] += f"|_{rank.rjust(2, '_')}| "

    for row in rows:
        print(row)


def get_move(player_hand, money):
    """
    'h' for hit, 's' for stand, 'd' for double-down.
    """
    while True:
        moves = ['(h)it', '(s)tand']

        if len(player_hand) == 2 and money > 0:
            moves.append('(d)ouble-down')
        
        move_prompt = ", ".join(moves) + '\n> '
        move = input(move_prompt).lower()
        if move in ('h', 's'):
            return move
        if move == 'd' and '(d)ouble-down' in moves:
            return move


if __name__ == '__main__':
    main()
