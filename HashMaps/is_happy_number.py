import sys


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # hash table method:
        list_of_sums = set()

        def sum_of_squares(num):
            sum = 0
            while num > 0:
                sum += (num % 10) ** 2
                num //= 10
            return sum

        while n != 1 and n not in list_of_sums:
            list_of_sums.add(n)
            n = sum_of_squares(n)

        return n == 1

    # floyd's tortoise and hare method:
    
    # requires the sum_of_sqaures function
    # then:
    slow = n
    fast = sum_of_squares(n)
    while fast != 1 and slow != fast:
        slow = sum_of_squares(slow)
        fast = sum_of_squares(fast)

    return fast == 1



if __name__ == "__main__":
    # Read argument from terminal
    if len(sys.argv) != 2:
        print("Usage: python solution.py <integer>")
        sys.exit(1)

    # Get the integer
    num = int(sys.argv[1])

    # Call the function
    sol = Solution()
    result = sol.isHappy(num)

    # Print the result
    print(result)
