class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n1 = nums1.length, n2 = nums2.length;
        int[] nums3 = new int[n1 + n2];
        int p1 = 0, p2 = 0, p3 = 0;
        while (p1 < n1 && p2 < n2) {
            if (nums1[p1] <= nums2[p2])
                nums3[p3++] = nums1[p1++];
            else
                nums3[p3++] = nums2[p2++];
        }
        while (p1 < n1)
            nums3[p3++] = nums1[p1++];
        while (p2 < n2)
            nums3[p3++] = nums2[p2++];
        int n = nums3.length;
        if (n % 2 == 1) {
            return nums3[n / 2];
        } else {
            return (nums3[n / 2 - 1] + nums3[n / 2]) / 2.0;
        }
    }
}