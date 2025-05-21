

n , m , q = map( int, input().split(' ') )
arr = []

    # Brute force ---> Time limit
for _ in range( n ):
    arr.append( list( map( int, input().split(' ') ) ) )
for _ in range( q ):
    sum = 0
    x1 ,y1 ,x2 ,y2 = map( int, input().split(' ') )
    i = x1 - 1
    while i < x2 :
        j = y1 - 1
        while j < y2 :
            sum += arr[i][j]
            j += 1
        i += 1
    print( sum )