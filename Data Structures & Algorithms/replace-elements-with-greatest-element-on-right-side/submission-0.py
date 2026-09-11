class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            j = i+1
            arr[i] = max(arr[j:])

        arr[-1] = -1
        return arr