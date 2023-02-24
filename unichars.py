import pandas as pd

chinese_nonrep = set()
lista_csvs = ["Boss Text.csv","Level Name.csv","UI Text.csv"]
for archive in lista_csvs:
    df = pd.read_csv(archive)
    chinese_col = df["Chinese (Simplified)(zh-CN)"].tolist()
    #print(chinese_col)
    
    
    chinese_chars = []
    unicode_list = []
    
    for phrase in chinese_col:
        if type(phrase) is str:
            for letter in phrase:
                chinese_chars.append(letter)
            
    #print(chinese_chars)
    
    chinese_nonrep.update(chinese_chars)
    #print(chinese_nonrep)
    #print(len(chinese_nonrep))
    
for character in chinese_nonrep:
    uni_char = hex(ord(character))[2:]  #converting each sole character into unicode
    unicode_list.append(uni_char)


print(unicode_list)
print(len(unicode_list))
    
frase_FER = ''
for unic in unicode_list:
    frase_FER += unic +','
#print(frase_FER)

with open('fer.txt', 'w') as f:
    f.write(frase_FER)
f.close()

#result for fer:
#for element in chinese_nonrep:
#    print(element, " ")
