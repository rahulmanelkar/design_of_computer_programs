import random

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def deal(numhands, n=5, deck=mydeck):
    handlist = []
    k_list=[]
    for _ in range(len(mydeck)):
        k_list.append(random.randint(0,len(mydeck))-1)
    print(k_list)
    k=0    
    for i in range(numhands):
        hand=''
        for j in range(n):            
            hand+=(mydeck[k_list[k]] + ' ')
            k+=1            
        handlist.append(hand.rstrip())
    return handlist


def poker(hands):
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    # Your code here.
    rank_list = [key(x) for x in iterable]
    rank_list_sorted = sorted(rank_list,key=lambda x:x[0])
    max = rank_list_sorted[-1][0]
    final_list = []
    for i in range(len(iterable)):
        if rank_list[i][0]==max:
            final_list.append(iterable[i])
    return final_list

    


def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand) 
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)

def card_ranks(cards):    
    "Return a list of the ranks, sorted with higher first."
    ranks = [r for r,s in cards]
    rank_dict = {'T':10,'J':11,'Q':12,'K':13,'A':14}
    ranks = [(lambda x:rank_dict[x] if x in rank_dict else int(x))(x) for x in ranks]
    ranks.sort(reverse=True)
    return [5,4,3,2,1] if (ranks == [14,5,4,3,2]) else ranks

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    # Your code here.
    if len(set(ranks))==len(ranks) and (ranks[0]-ranks[4])==4:
        return True
    else:
        return False

def flush(hand):
    "Return True if all the cards have the same suit."
    # Your code here.
    if len(set([s for r,s in hand])) == 1:
        return True
    else:
        return False
    
def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    # Your code here.
    if len(set(ranks)) == len(ranks):
        return None
    counts = [(x,ranks.count(x)) for x in ranks]
    for rank_count in counts:
        if rank_count[1] == n:
            return rank_count[0]        


def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    # Your code here.
    return_dict={}
    for rank in ranks:
        if rank in return_dict.keys():
            return_dict[rank]+=1
        else:
            return_dict[rank]=1
    if len(return_dict.keys())==3 and max(list(return_dict.values()))==2:
        b=list(return_dict.keys())
        b.sort(reverse=True)
        return tuple(b[:2])
    
def test():
    "Test cases for the functions in poker program."
    sf1 = "6C 7C 8C 9C TC".split() # Straight Flush
    sf2 = "6D 7D 8D 9D TD".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    assert poker([sf1, sf2, fk, fh]) == [sf1, sf2]
    #poker([sf1, sf2, fk, fh]) 
    return 'tests pass'

print(deal(4))