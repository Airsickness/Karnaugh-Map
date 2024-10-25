karnaughMap = [[1, 1, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0]]

def num_rows(array):
    numberOfRows = 0
    for index in array:
        numberOfRows+=1
    return numberOfRows


def look_for_eights(array):
    groupings_array = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    if num_rows(array) < 2:
        return False

    flat_list = [element for row in array for element in row]
    if all(element == flat_list[0] for element in flat_list):
        return False


    groupings = 0
    for counter in range(0, len(array)):
        if array[0][counter] == 1:
            groupings_array[0].pop(counter)
            groupings_array[0].insert(counter, array[0][counter])
            groupings = groupings + 1
    if groupings == 4:
        for counter in range(0, len(array)):
            if array[1][counter] == 1:
                groupings_array[1].pop(counter)
                groupings_array[1].insert(counter, array[1][counter])
                groupings = groupings + 1
    if groupings == 8:
        print(groupings_array)
        return True
    groupings = 0
    for counter in range(0, len(array)):
        if array[1][counter] == 1:
            groupings_array[1].pop(counter)
            groupings_array[1].insert(counter, array[1][counter])
            groupings = groupings + 1
    if groupings == 4:
        for counter in range(0, len(array)):
            if array[2][counter] == 1:
                groupings_array[2].pop(counter)
                groupings_array[2].insert(counter, array[2][counter])
                groupings = groupings + 1
    if groupings == 8:
        print(groupings_array)
        return True

    groupings = 0

    for counter in range(0, len(array)):
        if array[2][counter] == 1:
            groupings_array[2].pop(counter)
            groupings_array[2].insert(counter, array[2][counter])
            groupings = groupings + 1
    if groupings == 4:
        for counter in range(0, len(array)):
            if array[3][counter] == 1:
                groupings_array[3].pop(counter)
                groupings_array[3].insert(counter, array[3][counter])
                groupings = groupings + 1

    if groupings == 8:
        print(groupings_array)
        return True

    groupings = 0

    for counter in range(0, len(array)):
        if array[0][counter] == 1:
            groupings_array[0].pop(counter)
            groupings_array[0].insert(counter, array[0][counter])
            groupings = groupings + 1
    if groupings == 4:
        for counter in range(0, len(array)):
            if array[3][counter] == 1:
                groupings_array[3].pop(counter)
                groupings_array[3].insert(counter, array[3][counter])
                groupings = groupings + 1

    if groupings == 8:
        print(groupings_array)
        return True


    groupings = 0

    if array[0][0] == array[0][1] == array[1][0] == array[1][1] == array[2][0] == array[2][1] == array[3][0] == array[3][1] == 1:
        for row in range(0, len(groupings_array)):
            for col in range(0, 1):
                groupings_array[row][col] = 1
        print(groupings_array)
        return True
    elif array[0][1] == array[0][2] == array[1][1] == array[1][2] == array[2][1] == array[2][2] == array[3][1] == array[3][2] == 1:
        for row in range(0, len(groupings_array)):
            for col in range(0, 1):
                groupings_array[row][col] = 1
        print(groupings_array)
        return True
    elif array[0][2] == array[0][3] == array[1][2] == array[1][3] == array[2][2] == array[2][3] == array[3][2] == array[3][3] == 1:
        for row in range(0, len(groupings_array)):
            for col in range(0, 1):
                groupings_array[row][col] = 1
        print(groupings_array)
        return True
    elif array[0][1] == array[0][2] == array[1][1] == array[1][2] == array[2][1] == array[2][2] == array[3][1] == array[3][2] == 1:
        for row in range(0, len(groupings_array)):
            for col in range(0, 1):
                groupings_array[row][col] = 1
        print(groupings_array)
        return True
    elif array[0][0] == array[1][0] == array[2][0] == array[3][0] == array[0][3] == array[1][3] == array[2][3] == array[3][3] == 1:
        for row in range(0, len(groupings_array)):
            for col in range(0, 1):
                groupings_array[row][col] = 1
        print(groupings_array)
        return True
    else:
        return False


print(look_for_eights(karnaughMap))
