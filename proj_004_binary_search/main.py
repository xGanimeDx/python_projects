import random

start = random.randint(0, 100)
lst = []

# generate ordered sequence
for i in range(100):
    lst.append(start)
    start += 2

# check the values inside sequence
print(lst)
# ask user for the search value
usr_input = int(input('Enter integer value for search: '))

def binary_search(sequence: list[int], value: int) -> int:
    # left border of the sequence
    low = 0
    # right border of the sequence
    high = len(sequence) - 1

    # we will repeat search until the low and high borders meet each other
    while low <= high:
        # find the middle element in sequence
        mid = low + (high - low) // 2

        # if middle element is the search value - return it
        if sequence[mid] == value:
            return mid
        # if the middle element is less than search value, we should move low border to the next element after middle
        # so that we will have right half of the sequence for the further search
        elif sequence[mid] < value:
            low = mid + 1
        # if the middle element is greater than search value, we should move high border to the previous element before middle
        # so that we will have left half of the sequence for the further search
        else:
            high = mid - 1
    # if sequence doesn't contain search value we'll return -1 as no result
    return -1

result = binary_search(lst, usr_input)
if result != -1:
    print(f'Found at index {result}')
    print(lst[result])
else:
    print('Not found')
