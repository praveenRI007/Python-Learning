# Python3 implementation of the approach

# Function to return the maximum profit
# that can be made after buying and
# selling the given stocks


def maxProfit(price, start, end):
    # If the stocks can't be bought
    if (end <= start):
        return 0

    # Initialise the profit
    profit = 0

    # The day at which the stock
    # must be bought
    for i in range(start, end, 1):

        # The day at which the
        # stock must be sold
        for j in range(i + 1, end + 1):

            # If buying the stock at ith day and
            # selling it at jth day is profitable
            if (price[j] > price[i]):
                # Update the current profit
                curr_profit = price[j] - price[i] + \
                              maxProfit(price, start, i - 1) + \
                              maxProfit(price, j + 1, end)

                # Update the maximum profit so far
                profit = max(profit, curr_profit)

    return profit


price = [100, 180, 260, 310, 40, 535, 695]
n = len(price)

print(maxProfit(price, 0, n - 1))


# Input: arr[] = {100, 180, 260, 310, 40, 535, 695}
# Output: 865
# Explanation: Buy the stock on day 0 and sell it on day 3 => 310 – 100 = 210
#                        Buy the stock on day 4 and sell it on day 6 => 695 – 40 = 655
#                        Maximum Profit  = 210 + 655 = 865


# Python3 Program to find
# best buying and selling days

# This function finds the buy sell
# schedule for maximum profit


def stockBuySell(price, n):
    # Prices must be given for at least two days
    if (n == 1):
        return

    # Traverse through given price array
    i = 0
    while (i < (n - 1)):

        # Find Local Minima
        # Note that the limit is (n-2) as we are
        # comparing present element to the next element
        while ((i < (n - 1)) and
               (price[i + 1] <= price[i])):
            i += 1

        # If we reached the end, break
        # as no further solution possible
        if (i == n - 1):
            break

        # Store the index of minima
        buy = i
        i += 1

        # Find Local Maxima
        # Note that the limit is (n-1) as we are
        # comparing to previous element
        while ((i < n) and (price[i] >= price[i - 1])):
            i += 1

        # Store the index of maxima
        sell = i - 1

        print("Buy on day: ", buy, "\t",
              "Sell on day: ", sell)


# Driver code


# Stock prices on consecutive days
price = [100, 180, 260, 310, 40, 535, 695]
n = len(price)

# Function call
stockBuySell(price, n)
