
a, b, c = map(int, input().split())

if (b < a and c >= b) or (b > a and c > b and ((c - b) >= (b - a))) \
     or (a > b and b > c and ((b - c) < (a - b))) or (a == b and c > b):
    print(':)')
elif (b > a and c <= b) or (b > a and c > b and ((c - b) < (b - a))) \
    or (b < a and c < b and ((b - c) >= (a - b))) or (a == b and c < b) \
        or (a == b and b == c and c == a):
    print(':(')
