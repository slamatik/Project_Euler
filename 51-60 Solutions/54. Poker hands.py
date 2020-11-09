def poker_hands(both_hands):
    left_hand = both_hands[:14]
    right_hand = both_hands[15:]

    left_score = get_hand_score(left_hand)
    right_score = get_hand_score(right_hand)
    return left_score > right_score


def get_hand_score(hand):
    ranks = card_ranks(hand)
    suits = card_suits(hand)
    kicker = high_card(ranks)

    if royal_flush(ranks) and flush(suits):
        return 10, kicker
    elif straight_flush(ranks) and flush(suits):
        return 9, kicker
    elif n_cards(ranks, 4):
        return 8, n_cards(ranks, 4), n_cards(ranks, 1)
    elif n_cards(ranks, 3) and n_cards(ranks, 2):
        return 7, n_cards(ranks, 3), n_cards(ranks, 2)
    elif flush(suits):
        return 6, kicker
    elif straight(ranks):
        return 5, kicker
    elif n_cards(ranks, 3):
        return 4, n_cards(ranks, 3), ranks
    elif two_pairs(ranks):
        return 3, two_pairs(ranks), ranks
    elif n_cards(ranks, 2):
        return 2, n_cards(ranks, 2), ranks
    else:
        return 1, ranks


def card_ranks(hand):
    ranks = ['__23456789TJQKA'.index(i[0]) for i in hand.split()]
    return sorted(ranks, reverse=True)


def card_suits(hand):
    suits = [i[1] for i in hand.split()]
    return suits


def royal_flush(ranks):
    if sum(ranks) == 60:
        return True


def straight_flush(ranks):
    if max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5:
        return True


def flush(suits):
    if len(set(suits)) == 1:
        return True


def straight(ranks):
    if max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5:
        return True


def two_pairs(ranks):
    solution = tuple(sorted(set([i for i in ranks if ranks.count(i) == 2]), reverse=True))
    return solution if len(solution) == 2 else None


def high_card(ranks):
    return max(ranks)


def n_cards(hand, n):
    for i in hand:
        if hand.count(i) == n:
            return i
    return None


def func():
    with open('p054_poker.txt') as f:
        data = f.read().split('\n')
    cnt = 0
    for i in data:
        if poker_hands(i):
            cnt += 1
    return cnt


print(func())
