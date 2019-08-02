# Проверка на ввод целого числа:

while True:
    
    file_size = (input("Enter the file size in bytes:\n"))

    try:
        file_size = int(file_size)
    except ValueError:
        print ("This is not an integer number, try again!\n")
    else:
        break

    
# Проверка на ввод неотрицательного числа:
while file_size < 0:
    file_size = int(input("The file size cannot be negative, enter a correct value!\n"))

# Перевод из байтов в мегабайты с округлением
print ("The file size in megabytes is:\n", round((file_size/1024**2),2), " Mb")
