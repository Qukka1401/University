import csv

def get_books(str):
    dict = []
    with open("books.csv", 'r', encoding='UTF-8') as file:
        tekst = csv.reader(file, delimiter='|')
        for row in tekst:
            if str.lower() in row[1].lower():
                dict.append(row)
    return dict
print(get_books('python'))

def get_totals(dict):
    cort = []
    for chicl in dict:
        sym = float(chicl[3])*float(chicl[4])
        if sym>=500:
            cort.append((chicl[0], sym))
        else:
            cort.append((chicl[0], sym+100))
    return cort
print(get_totals(get_books('python')))