def clamp(val, minval, maxval):
    if val < minval: return minval
    if val > maxval: return maxval
    return val