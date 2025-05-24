def mergesort(liste):
    if len(liste) <= 1:
        return liste

    #divide
    s = 0
    e = len(liste)
    m = (s + e) // 2

    left = mergesort(liste[s:m])
    right = mergesort(liste[m:e])

    #merge
    return merge(left, right)

def merge(left, right):
    sorted_list = []
    i = j = 0

    # Compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add any remaining elements from the left half
    sorted_list.extend(left[i:])
    # Add any remaining elements from the right half
    sorted_list.extend(right[j:])

    return sorted_list

# Beispielnutzung
if __name__ == "__main__":
    from random import randint
    liste = [randint(1, 100) for _ in range(10)]
    print("Unsortierte Liste:", liste)
    print("Sortierte Liste:", mergesort(liste))



