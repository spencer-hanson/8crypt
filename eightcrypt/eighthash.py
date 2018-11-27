def convert(val):
    eight = lambda x: -2911 * (x * x * x * x) / 119340 + (x * x * x) * 94643 / 119340 - 202471 * x * x / 29835 + 288581 * x / 9945 + 6
    result = []
    for v in val:
        result.append(chr(round(eight(ord(v.lower())-97) % 25)+97))
    out = "".join(result)
    return out


x = "beans"
print("In: {}".format(x))
x = convert(x)
print("Out: {}".format(x))
