def quicksort(items):
    if len(items) <= 1:
        return 1

    pivot = items.pop()

    small_item = []
    large_item = []

    if 