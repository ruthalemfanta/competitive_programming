def highestAltitudes(gain):
    altitudes = [0]

    for i in gain:
        altitudes.append(altitudes[-1] + i)

    return max(altitudes)


