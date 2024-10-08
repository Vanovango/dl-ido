numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

lost_el = 0
sum = 0

for i in range(len(numbers)):
    if numbers[i] is None:
        lost_el = i
    else:
        sum += numbers[i]

numbers[lost_el] = sum / len(numbers)


print("Измененный список:", numbers)
