"""
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.
"""


class Solution(object):
    def lemonadeChange(self,bills):

        nota_de_5 = 0
        nota_de_10 = 0    

        for nota in bills:
            
            if nota == 5:
                nota_de_5 += 1
            elif nota == 10:
                nota_de_5 -= 1
                nota_de_10 += 1
            elif nota == 20:
                if nota_de_10 >= 1:
                    nota_de_10 -= 1
                    nota_de_5 -= 1
                else:
                    nota_de_5 -= 3

            if nota_de_5 < 0 or nota_de_10 < 0:
                return False
        
        return True