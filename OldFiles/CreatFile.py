import csv;

from OldFiles import powerSetFinder as psf

# columnsNames = ['name', 'year', 'grapes', 'country', 'region', 'description', 'picture']


columnsNames = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

powersetNames = psf.listToPowerset(columnsNames)
arr = []

for (cols) in powersetNames:
    arr.append(', '.join(cols))

# le = preprocessing.LabelEncoder()
# le.fit(columnsNames)
# columns = le.transform(columnsNames)

# powerset = psf.listToPowerset(columns)

# with open('queries.csv', 'w', newline='') as csvfile:
#     # fieldnames = ['select', 'columns', 'from', 'table']
#     # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer = csv.DictWriter(csvfile, fieldnames=['sel'])
#     writer.writeheader()
#     # for (str) in powerset:
#     # for (pw) in powersetNames:
#     for (str) in arr:
#         b = le.fit(columnsNames).transform(str)
#         for a in b:
#             writer.writerow({'sel': [a,]})
#         # writer.writerow({'select': 'select', 'columns': str, 'from': 'from', 'table': 'wines'})


with open('kmeansQueries.csv', 'w', newline='') as csvfile:
    fieldnames = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    # a, b, c, d, e, f, g = 0
    for (pw) in powersetNames:
        if 'A' in pw:
            a = 1
        if 'B' in pw:
            b = 1
        if 'C' in pw:
            c = 1
        if 'D' in pw:
            d = 1
        if 'E' in pw:
            e = 1
        if 'F' in pw:
            f = 1
        if 'G' in pw:
            g = 1

        writer.writerow({'A': a, 'B': b, 'C': c, 'D': d, 'E': e, 'F': f, 'G': g})

        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        g = 0
