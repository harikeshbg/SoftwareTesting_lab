def get_pivot_position(array,start,end):
    i=start-1
    for j in range(start,end):
        if array[j]<array[end]:
            i+=1
            array[i],array[j]=array[j],array[i]
    array[i+1],array[end]=array[end],array[i+1]
    return i+1

def quick_sort(array,start,end):
    if start<end:
        pivot_pos=get_pivot_position(array,start,end)
        quick_sort(array,start,pivot_pos-1)
        quick_sort(array,pivot_pos+1,end)

if __name__ == "__main__":
    array=[]
    n=int(input("Enter the number of elements:"))
    print("Enter the elements:")
    for i in range(n):
        elem=int(input())
        array.append(elem)
    quick_sort(array,0,n-1)
    print("Sorted array:")
    for i in range(n):
        print(array[i],end=" ")
    print("\n")