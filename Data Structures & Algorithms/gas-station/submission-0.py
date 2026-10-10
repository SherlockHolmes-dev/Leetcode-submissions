class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_tank = 0  # Net fuel balance for the whole route
        curr_tank = 0   # Net fuel from current start position
        start = 0       # Candidate start station

        for i in range(n):
            # Update total and current balance
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            
            # If current tank becomes negative, this start fails
            if curr_tank < 0:
                # Next station is the new candidate start
                start = i + 1
                curr_tank = 0  # Reset for the new start

        # If overall gas >= cost, a solution exists and is unique
        return start if total_tank >= 0 else -1
        