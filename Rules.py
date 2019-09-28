def rules(str):
    for i in range(len(str)-1):
        if str.isalpha() == False:
            return 'Строка состоит не только из слов '
        if str[i] == 'ж' or str[i] == 'ш' or str[i] == 'Ж' or str[i] == 'Ш' and str[i+1] == 'ы':
            return 'Ошибка в написании жи/ши'
        elif str[i] == 'ч' or str[i] == 'щ' or str[i] == 'Ч' or str[i] == 'Ш' and str[i+1] == 'я':
            return 'Ошибка в написании ча/ща'
        else:
            return 'Ошибок нет'
str=input('Введите строку: ')
print(rules(str))