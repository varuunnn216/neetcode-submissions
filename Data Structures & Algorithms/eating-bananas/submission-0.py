class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k):
            total_hours = 0
            for pile in piles:
                total_hours += (pile + k - 1) // k
            return total_hours

        lp = 1
        rp = max(piles)
        best_k = rp

        while lp <= rp:
            mid_k = (lp + rp) // 2
            hours = hours_needed(mid_k)

            if hours <= h:
                best_k = mid_k
                rp = mid_k - 1
            else:
                lp = mid_k + 1

        return best_k 