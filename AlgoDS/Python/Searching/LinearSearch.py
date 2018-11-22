#Linear search implementation

def seqentialSearch(arr,k):

    for i in range(0,len(arr)):

        if arr[i]==k:
            return 'Element {} found at {}'.format(k,i)
    return 'Element {} not found'.format(k)

arr=[1,2,5,9,3]

print(seqentialSearch(arr,5))