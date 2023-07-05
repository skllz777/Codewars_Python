def count_smileys(arr):
    smiles = []
    for smile in arr:
        if len(smile) == 2 and smile[0] in [':', ';'] and smile[1] in [')', 'D']:
            smiles.append(smile)
        elif len(smile) > 2 and smile[0] in [':', ';'] and smile [1] in ['-', '~'] and smile[2] in [')', 'D']:
            smiles.append(smile)
    return len(smiles)