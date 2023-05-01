def findMedian(list):
    low = 0
    high = len(list) - 1

    print(f"Low: {low}")
    print(f"High: {high}")

    median = low + ((high - low)//2)
    print(f"Median: {median}")

findMedian([16,1,0,9,100])