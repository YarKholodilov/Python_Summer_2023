def polymorph(t1, t2):
    if len(t2) != len(t1):
        return False
    else:
        base = dict(zip(t1, t2))
        t_list1,  t_list2 = list(t1), list(t2)
        compare_t1, compare_t2 = [], []
        for i in range(len(t_list1)):
            if t_list1[i] in base.keys():
                compare_t2.append(base[t_list1[i]])

        for j in range(len(t_list2)):
            for k, v in base.items():
                if t_list2[j] == v:
                    compare_t1.append(k)
        # print(t2, t_list2, compare_t1)
        if compare_t1 == t_list1 and compare_t2 == t_list2:
            return True
        else:
            return False


text1 = 'rambunctiously'
text2 = 'thermodynamics'
print(polymorph(text1, text2))
