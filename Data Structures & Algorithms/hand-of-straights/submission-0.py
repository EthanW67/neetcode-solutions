class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        freq = Counter(hand)
        hand.sort()
        for card in hand:
            if freq[card] == 0:
                continue

            for i in range(groupSize):
                if freq[i + card] == 0:
                    return False

                freq[i + card] -= 1

        return True