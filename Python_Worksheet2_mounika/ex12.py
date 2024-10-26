#program to implement an insertion sort algorithm
from random import randint
def main():
    A=[randint(15,55) for i in range(randint(5,10))]
    print('unsorted array',A)
    l=len(A)

    for i in range(1,l):
        key=A[i]
        j= i - 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j+1] =key

    print('sorted array',A)
if __name__ == "__main__":
   main()
