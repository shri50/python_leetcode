


def perfect_sqrt(num: int)-> bool:

    
    low,high = 1, num//2
    

    while(low <= high):
        mid = (low + high) // 2
        print(low,mid,high)
        square = mid * mid
        print(square)
        if square == num:
            return True
        elif square < num:
            low = mid+1
            print(f"{low=}")
        else:
            high = mid-1
            print(f"{high=}")
    return False


print(perfect_sqrt(24))