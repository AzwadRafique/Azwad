number_of_times = int(input())
names = []
scores = []
for x in range(number_of_times):
    line = input()
    array = line.split(" ")
    names.append(array[0])
    scores.append(int(array[1]))

swapped = True
for y in range(len(scores)):
    swapped = False
    for placement in range(len(scores) - 1):
        if scores[placement] < scores[placement + 1]:
            swapped = True
            temporary_score = scores[placement + 1]
            scores[placement + 1] = scores[placement]
            scores[placement] = temporary_score
            temporary_names = names[placement + 1]
            names[placement + 1] = names[placement]
            names[placement] = temporary_names
        if scores[placement] == scores[placement + 1]:
            if names[placement] > names[placement + 1]:
                temporary_alphabet = names[placement + 1]
                names[placement + 1] = names[placement]
                names[placement] = temporary_alphabet

    if not swapped:
        break


print(names[0])
