#This is a sorting visulaizer program
#When prompted, type in your desired sorting algorithm and type in an array/list of your desired size
#See how each sorting algorithm sorts the array/list from step 0 until the final step


def bubble_sort(array):
    for i in range(0, len(array)):
        print("After", i, "iterations")
        print(array)
        for x in range(0, len(array)-1):
            if array[x]>array[x+1]:
                array[x+1], array[x] = array[x], array[x+1]
    print("FINAL ARRAY")
    print(array)


def selection_sort(array):
    for i in range(0, len(array)):
        print("After", i, "iterations")
        print(array)
        min = i
        for j in range(i+1, (len(array))):
            if array[min]>array[j]:
                min = j
        array[min],array[i] = array[i],array[min]
    print("FINAL ARRAY")
    print(array)
def insertion_sort(array):
    for i in range(1, len(array)):
        print("After", i-1, "iterations")
        print(array)
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
        array[j + 1] = key
    print("FINAL ARRAY")
    print(array)




def main():
    run = True
    while run == True:
        print("Sorting algorithms\n1) Bubble sort\n2) Selection Sort\n3) Insertion Sort")
        a = print("What type of sorting do you wish to see?")
        val = int(input())
        length = int(input("What is the length of the array?: "))
        array = []
        for i in range(0, length):
            z = int(input("Enter value: "))
            array.append(z)
        print("-----------------------")
        print("This is your array:")
        print(array)
        if (val==1):
            bubble_sort(array)
        elif (val==2):
            selection_sort(array)
        elif (val ==3):
            insertion_sort(array)
        print("-----------------------")
        print("Continue? Y/N")
        result = input()
        if result == "N":
            print("END OF PROGRAM")
            run = False
        else:
            print("-----------------------")

main()