#[1,2,3,4],target=6
#output: [[1,2,3],[2,4]]
#start from last index and check for (subset with last index) + (subset without last index)

def subsetSumTarget(arr, target):
    mem={}
    return subsetSumTargetMemoized(arr,target,len(arr)-1,mem)

def subsetSumTargetMemoized(arr,target,index,mem):

#assign key val pair with (target:arr[index])
#check if the key-val pair is already in mem. if yes, return that value(no need to compute again)
#if value==0, return 1(empty set is one set)
#if index<0, return 0
#if target<the value at that array index, call recursively with all values same but index-1 and that that to memoized array for that target:index key
# if target>=the value, then add the following recursive calls and put that value in meoized array for that index keypair:
# (call recursively with all values same but index-1) + (call recursively with all values same but target=target-arr[index] and index-1 )

    keyPair= str(target)+':'+str(index)
    if keyPair in mem:
        return mem[keyPair]   
    if target==0:
        return 1
    elif index<0:
        return 0
    elif target<arr[index]:
        to_return = subsetSumTargetMemoized(arr, target, index-1, mem)
    else:
        to_return = subsetSumTargetMemoized(arr, target-arr[index], index - 1, mem) + subsetSumTargetMemoized(arr, target, index-1, mem)
    
    mem[keyPair]=to_return
    return to_return

print(subsetSumTarget([1,2,3,4],6))