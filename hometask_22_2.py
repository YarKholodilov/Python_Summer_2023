tree = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7), (7, 8)]
finish = int(input('введите число из дерева: '))
roadmap = []
root = 0

while finish != 1:
    for i in range(len(tree)):
        for j in range(len(tree[i])):
            if tree[i][1] == finish:
                root += 1
                roadmap.append(finish)
                finish = tree[i][0]
                if finish == 1:
                    roadmap.append(finish)

print(root, roadmap)
