class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []

        for current_day in range(n):
            current_temp = temperatures[current_day]

            while stack and temperatures[stack[-1]] < current_temp:
                waiting_day = stack.pop()
                result[waiting_day] = current_day - waiting_day

            stack.append(current_day)

        return result