class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        S, B = nums1, nums2
        if len(S) > len(B):
            S, B = B, S
        
        total = len(S) + len(B)
        half = total // 2
        l, r = 0, len(S)

        while l <= r:
            i = (l + r) // 2
            j = half - i

            S_left = S[i - 1] if i > 0 else float("-inf")
            S_right = S[i] if i < len(S) else float("inf")
            B_left = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j] if j < len(B) else float("inf")

            if S_left <= B_right and B_left <= S_right:
                if total % 2 == 1:
                    return float(min(S_right, B_right))
                return (max(S_left, B_left) + min(S_right, B_right)) / 2.0
            elif S_left > B_right:
                r = i - 1
            else:
                l = i + 1

        return 0.0