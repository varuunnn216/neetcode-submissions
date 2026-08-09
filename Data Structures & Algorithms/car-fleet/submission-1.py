class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key = lambda car:car[0], reverse = True)

        stack = []

        for pos, spd in cars:
            ttrt = (target - pos) / spd

            if not stack or ttrt > stack[-1]:
                stack.append(ttrt)

        return len(stack)