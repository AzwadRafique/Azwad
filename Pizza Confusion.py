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
    for position in range(len(scores) - 1):
        if scores[position] < scores[position + 1]:
            swapped = True
            temporary_score = scores[position + 1]
            scores[position + 1] = scores[position]
            scores[position] = temporary_score
            temporary_names = names[position + 1]
            names[position + 1] = names[position]
            names[position] = temporary_names

        if not swapped:
            break

for y in range(len(names)):
    for placement in range(len(names) - 1):
        if scores[placement] == scores[placement + 1]:
            if names[placement] > names[placement + 1]:
                temporary_alphabet = names[placement + 1]
                names[placement + 1] = names[placement]
                names[placement] = temporary_alphabet

print(names[0])
