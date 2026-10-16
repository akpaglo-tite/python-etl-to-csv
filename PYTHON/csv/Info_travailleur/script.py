import csv

Destinaton_file = "Extraction python des pages web/PYTHON/csv/Info_travailleur/output.csv"

source_csv = "Extraction python des pages web/PYTHON/csv/Info_travailleur/input.csv"


with (
    open(source_csv, mode='r',newline="", encoding='utf-8') as file,
    open(Destinaton_file, mode='w', newline="", encoding='utf-8') as file_des,):

    reader_csv = csv.reader(file,delimiter=',')
    writer_csv = csv.writer(file_des,delimiter=',')

    i = 0
    valeur = True
    for line in reader_csv :
        
        if valeur :
            en_tete = [line[i],"salaire"]
            writer_csv.writerow(en_tete)
            valeur = False
        else:
            salaire = f"{int(line[i + 1]) * 15} F"
            writer_csv.writerow([line[i], salaire])
        