def rech_naive1(motif, texte):
    i = 0
    j = 0

    while i < len(texte) and j < len(motif):
        if texte[i] == motif[j]:
            i += 1
            j += 1
        else:
            i += 1 - j
            j = 0
    if j >= len(motif):
        return i - len(motif)
    return None

assert rech_naive1("ab", "abcdef") == 0
assert rech_naive1("bc", "abdbc") == 3

def rech_naive2(motif, texte):
    occurences = [rech_naive1(motif, texte)]
    i = 0
    while len(texte) >= len(motif) and occurences[-1] is not None:
        texte = texte[(occurences[-1] + 1):]
        occurences[-1] += i
        i = occurences[-1] + 1
        occurences.append(rech_naive1(motif, texte))

    if occurences[-1] is None:
        occurences.pop()

    return occurences

assert rech_naive2("bc", "abdbcdabdbcebc") == [3, 9, 12]
assert rech_naive2("bc", "b") == []
assert rech_naive2("bc", "bc") == [0]
