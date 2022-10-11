#dictionary - это неупор.набор пары "ключ:значение".
#Словарь можно рассматривать как Массив со строчными индексами.
#в качестве ключей берутся неизм.значения: строки, номера, кортежи.
#items = key:value

dce = {}
dcp = {'olia': 13, 'kolya': 12, 'katya': '13', 'misha': 12}

print(len(dcp))
print(type(dcp))

print(dir(dcp))   #посмотреть набор существующих функций и методов для словаря.
print('or')
print(dir(dict))  #посмотреть набор существующих функций и методов для словаря.

print(dcp.keys())
print(dcp.values())
print(dcp.items())

print(help(dcp.pop))

dcp['vitya'] = 15
dcp['sveta'] = 16
print(dcp)
del dcp['vitya']
print(dcp)

print('-'*100)
def frev(dc):                    #frev = function reverse
    dcr = {}
    for k,v in dc.items():
            if not v in dcr: dcr[v] = []
            dcr[v].append(k)
    return dcr
print('bob' in dcp)
print('misha' in dcp)

for k in dcp:
    print(k, ':', dcp[k])

dc1 = frev(dcp)  # получаем значение нового словаря dc1 с именами учентков с одинаковыми возрастами.
print(dc1)
print(dcp)
print('-'*100)


st = 'we are study dictionary'
def ffreq(st):      #частотный словарь: то есть собирается словарь из {ключ:значение}={символ:частота его применения, сколько раз}
    dcf = {}    #пустой словарь dcf.
    for ch in st:   #для символа ch в строке st.
            if not ch in dcf: dcf[ch] = 0  #если символ не встречается в словаре, то ему присвоить значение 0.
            dcf[ch] += 1 #
    return dcf
dc2 = ffreq(st)
print(dc2)
print('-'*100)

ls = dc2.items()
print(ls)

print('*'*100)
def fcmp(a, b):
    if a[1] > b[1]: return 1
    if a[1] < b[1]: return -1
    return 0
lss = sorted(ls,fcmp)
print(lss)
print(lss[-1])

