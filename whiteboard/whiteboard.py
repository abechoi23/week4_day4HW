# Task:
# Find out "B"(Bug) in a lot of "A"(Apple).
# There will always be one bug in apple, not need to consider the situation that without bug or more than one bugs.
# input: string Array apple
# output: Location of "B", [x,y]
apple=[
        ["A","A","A","A","A"],
        ["A","A","A","A","A"],
        ["A","A","A","B","A"],
        ["A","A","A","A","A"],
        ["A","A","A","A","A"]
        ]
# def find_bug(apple):
#     print(apple[0])
#     for a in range(len(apple)):
#         for b in range(len(apple[a])):
#             print([a,b])
#             if apple[a][b] == "B":
#               return [a,b]
#             else:
#                 None
#     return [a,b]
# print(find_bug(apple))


def find_bug(apple):
    for i, row in enumerate(apple):
        if 'B' in row:
            j = row.index('B')
            return [i, j]

location = find_bug(apple)
print(location)
