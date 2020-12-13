
membros = {
    1: 'Rolien', 
    2: 'Naej', 
    3: 'Elehcim', 
    4: 'Odranoel'
}

casos = int(input())

for i in range(casos):
    feedbacks = int(input())
    for j in range(feedbacks):
        categoria = int(input())
        print(membros[categoria])
