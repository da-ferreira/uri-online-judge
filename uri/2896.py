
casos = int(input())

for i in range(casos):
    refrigerantes, garrafas = map(int, input().split())
    
    result = refrigerantes // garrafas
    result += refrigerantes % garrafas 
    
    print(result)
