
def subsetA(arr):

    result = []
    def sum(array):
        totalSum = 0
        for i in range(len(array)):
            totalSum  = totalSum + array[i]

        return totalSum

    def allSubset(array, answer):
        if len(array) == 0:
            result.append(answer)
            return

        allSubset(array[1:len(array)], answer + [array[0]])
        allSubset(array[1:len(array)], answer )

    allSubset(arr, [])
    print(result)


    # Write your code here
if __name__ == '__main__':
    array = [3,7,5,6,2]
    array = [1,4,2]
    subsetA(array)