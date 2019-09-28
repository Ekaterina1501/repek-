def dist(n):
    all_way = 0
    distance_to_home = 0
    for i in range(1,n+1):
        all_way += 1/i
        distance_to_home += (-1)**(i+1)/i
    return 'Весь путь: ', all_way, 'Расстояние до дома: ', distance_to_home

print(dist(int(input('Введите n: '))))