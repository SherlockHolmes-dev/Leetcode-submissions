class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)  # frequency map
        
        for card in sorted(count):  # process in sorted order
            freq = count[card]
            if freq > 0:  # we need to form groups starting with this card
                for i in range(groupSize):
                    next_card = card + i
                    if count[next_card] < freq:
                        return False  # not enough cards to form group
                    count[next_card] -= freq  # use them up
        return True
        