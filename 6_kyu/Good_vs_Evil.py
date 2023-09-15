def good_vs_evil(good, evil):
    g = [1, 2, 3, 3, 4, 10]
    e = [1, 2, 2, 2, 3, 5, 10]
    return "Battle Result: Good triumphs over Evil" if sum(g[i] * int(j) for i, j in enumerate(good.split())) > sum(e[i] * int(j) for i, j in enumerate(evil.split())) else "Battle Result: Evil eradicates all trace of Good" if sum(g[i] * int(j) for i, j in enumerate(good.split())) < sum(e[i] * int(j) for i, j in enumerate(evil.split())) else "Battle Result: No victor on this battle field"