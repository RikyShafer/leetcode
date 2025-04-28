# Last updated: 28.4.2025, 13:53:16
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        numberA = int(a, 2)
        numberB = int(b, 2)

        num=numberA+numberB
        binary = bin(num)[2:]
        return binary
        