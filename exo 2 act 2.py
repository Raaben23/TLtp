def replace_many(s, L1, L2):
    S2 = []
    for i in range(len(s)):
        S2.append(s[i])
    S3 = []
    for i in range(len(S2)):
        if S2[i]not in L1:
            S3.append(S2[i])
        else:
            for j in range(len(L1)):
                if S2[i] == L1[j]:
                    S3.append(L2[j])
    return  "" .join(S3)


print(replace_many("aabkc" , ["a", "b", "c"],["b", "a", "d"]))