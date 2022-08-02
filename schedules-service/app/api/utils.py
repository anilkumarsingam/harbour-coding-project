def find_overlap(a, b):
    if not a or not b:
        return []

    i = 0
    j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i][1] < b[j][0]:
            # a[i] is too small to overlap
            i += 1
        elif b[j][1] < a[i][0]:
           # b[j] is too small to overlap
            j += 1
        else:
            start = max(a[i][0], b[j][0])
            end = min(a[i][1], b[j][1])
            result.append([start, end])
            # whichever ends first will be removed from consideration as
            # the next interval in the series might still overlap
            if a[i][1] <= b[j][1]:
                i += 1
            else:
                j += 1
    return result
