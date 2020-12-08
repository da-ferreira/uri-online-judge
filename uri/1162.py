
def insertion_sort(array):
    swaps = 0
    
    for i in range(1, len(array)):
        area_ordenada = i

        while area_ordenada > 0 and array[area_ordenada] < array[area_ordenada - 1]:
            array[area_ordenada - 1], array[area_ordenada] = array[area_ordenada], array[area_ordenada - 1]
    
            swaps += 1
            area_ordenada -= 1    

    return swaps


casos = int(input())

for i in range(casos):
    n = int(input())

    vagoes = list(map(int, input().split()))
    
    print(f'Optimal train swapping takes {insertion_sort(vagoes)} swaps.')
