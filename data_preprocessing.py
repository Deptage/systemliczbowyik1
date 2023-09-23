#data=pd.read_csv("/kaggle/working/data.csv")
data=pd.read_csv("/kaggle/input/syslicz/data.csv")
data.columns=["indeks","liczba"]
#uznamy, że max długość liczby to będzie 18, z czego 6 znaków z lewej, środkowy, 11 z prawej
# Funkcja do formatowania pojedynczego ciągu
max_dl=18
def formatuj_ciag(ciag):
    lewa, separator, prawo = ciag.partition('x') if 'x' in ciag else ciag.partition('o')
    lewa = lewa.rjust(6,'0')
    prawo = prawo.ljust(11,'0')
    if separator=='x':
        separator='1'
    else:
        separator='0'
    
    return f"{lewa}{separator}{prawo}"

data['sformatowana_liczba'] = data['liczba'].apply(formatuj_ciag)

predictors=data.sformatowana_liczba.to_numpy()
target=data.indeks.to_numpy()
#print(predictors)
#print(target)
pred=[]
# Użyj wyrażenia listowego do rozdzielenia stringa na pojedyncze cyfry i utworzenia tablicy
for prediction in predictors:
    digit_array = [int(digit) for digit in prediction]
    pred.append(digit_array)
    #print(pred)
with open('/kaggle/working/almostdone.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i, row_data in enumerate(pred):
        writer.writerow([i + 1] + list(row_data))
    file.close()


