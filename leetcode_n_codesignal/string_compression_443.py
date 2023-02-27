# Problem: String Compression
# Leetcode 443
def compress(chars: List[str]) -> int:
    slow_p = chars[0]
    counts = 0
    l3 = []

    for fast_p in chars:
        if fast_p == slow_p:
            counts += 1
        else:
            if counts > 1:
                l3.append([slow_p, counts])
            else:
                l3.append([slow_p])

            slow_p = fast_p
            counts = 1

    if counts > 1:
        l3.append([fast_p, counts])
    else:
        l3.append([fast_p])
    chars[:] = [
        y for y in "".join([str(item) for sublist in l3 for item in sublist])
    ]
    return len(chars)
