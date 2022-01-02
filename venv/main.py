import openpyxl

book = openpyxl.load_workbook('test.xlsx')

sheet = book.active

cells = sheet['F2': 'G40']

counter = 2

total_min = 0

for c1, c2 in cells:
    print(counter, c1.value)
    if (c1.value is None):
        break
    char_index = c1.value.find(':')
    total_min += int(c1.value[:char_index]) * 60
    total_min += int(c1.value[char_index+1:])

    counter += 1

sheet['F'+str(counter)] = 'total hour'
sheet['G'+str(counter)] = total_min / 60

book.save("sample.xlsx")