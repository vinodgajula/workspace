
def locate_card_optimized(cards, query):
    lo, hi = 0, len(cards) - 1
    result = -1  # To store the index of the first occurrence

    while lo <= hi:
        mid = (lo + hi) // 2
        
        if cards[mid] == query:
            result = mid  # Update the result with the current index
            hi = mid - 1  # Continue searching in the left half
        elif cards[mid] < query:
            hi = mid - 1  # Search in the left half
        else:
            lo = mid + 1  # Search in the right half

    return result  # Return the first occurrence index or -1 if not found
test_sample = {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}
print(f"binary search result {locate_card_optimized(**test_sample)}")
