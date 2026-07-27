class Solution:
    def climbStairs(self, n: int) -> int:
        one,two = 1,1
        for i in range(n-1):
            temp = one
            one = one+two
            two = temp
        return one

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # 'one' stores the number of ways to reach the current step.
        # 'two' stores the number of ways to reach the previous step.
        # Initially:
        # ways(1) = 1
        # ways(0) = 1 (there is one way to stay at the ground)
        one, two = 1, 1

        # We already know the answer for n = 0 and n = 1.
        # So, repeat the calculation (n - 1) times to reach step n.
        for i in range(n - 1):

            # Save the current value of 'one'
            # because it will become the new value of 'two'
            temp = one

            # Calculate the number of ways for the next step.
            # To reach the next step, you can:
            # 1. Take one step from the current step.
            # 2. Take two steps from the previous step.
            # Therefore:
            # next = current + previous
            one = one + two

            # Update 'two' to the previous value of 'one'
            # so it is ready for the next iteration.
            two = temp

        # After the loop, 'one' contains the answer for step n.
        return one

"""


        