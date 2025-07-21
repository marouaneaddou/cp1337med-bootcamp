
import itertools
import sys

def main():
    data    = sys.stdin.read().split()
    index   = 0
    try:
        n = int(data[index]); index += 1
        m = int(data[index]); index += 1
        q = int(data[index]); index += 1

        arr = [[0] * m for _ in range(n)]

        # print( arr )
        for i in range( n ):
            for j in range( m ):  
                arr[i][j]     =     int(data[index]); index += 1
                up          =   arr[ i - 1 ][j] if  i - 1 > -1 else 0 
                left        =   arr[i][ j - 1 ] if  j - 1 > -1 else 0 
                corner      =   arr[ i - 1 ][j - 1] if  i - 1 > -1 and j - 1 > -1 else 0 
                arr[i][j]   =    (up + left + arr[i][j]) - corner
        for i in range( q ):
            sum = 0
            x1 = int(data[index]) - 1; index += 1
            y1 = int(data[index]) - 1; index += 1
            x2 = int(data[index]) - 1; index += 1 
            y2 = int(data[index]) - 1; index += 1
            sum += arr[x2][y2]
            if x1 > 0:
                sum -= arr[x1 - 1][y2]
            if y1 > 0:
                sum -= arr[x2][y1 - 1]
            if x1 > 0 and y1 > 0:
                sum += arr[x1 - 1][y1 - 1]
            sys.stdout.write( sum )
    except (IndexError, ValueError):
        print("❌ Error: Input too short or invalid", file=sys.stderr)
        sys.exit(1)
if __name__ == "__main__":
    main()
# if i == 1 :
# break
    # break
        # print( arr[i][j] )
        # print( arr )
        # print( j )
# n , m , q = map( int, input().split(' ') )
# arr = []

# for i in range( n ):
#     raw = list( map( int, input().split(' ') ) ) 
#     if i == 0 :
#         arr.append( list(itertools.accumulate(raw)) )
#     else :
#         j = 0
#         while j < m :
#             up      = arr[ i - 1 ][j] if  i - 1 > -1 else 0 
#             left    = raw[ j - 1 ] if  j - 1 > -1 else 0 
#             corner  = arr[ i - 1 ][j - 1] if  i - 1 > -1 and j - 1 > -1 else 0 
#             raw[j] =   (up + left + raw[j]) - corner
#             j += 1
#         arr.append( raw )
# for _ in range(q) : 
#     sum = 0
#     x1 ,y1 ,x2 ,y2 = map( int, input().split(' ') )
#     x1 -= 1
#     y1 -= 1
#     x2 -= 1 
#     y2 -= 1
#     sum += arr[x2][y2]
#     if x1 > 0:
#         sum -= arr[x1 - 1][y2]
#     if y1 > 0:
#         sum -= arr[x2][y1 - 1]
#     if x1 > 0 and y1 > 0:
#         sum += arr[x1 - 1][y1 - 1]

