class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        result = []

        for item in asteroids:
            result.append(item)

            while len(result) > 1 and result[-1] < 0 and result[-2] > 0:
                last = result.pop()

                if abs(last) > result[-1]:
                    result[-1] = last
                elif abs(last) == result[-1]:
                    result.pop()

        return result

