/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
    const arr = ([...nums1, ...nums2]).sort((a, b) => a - b)
    const mid = parseInt(arr.length / 2)

    return arr.length % 2 === 0 ?
        (arr[mid] + arr[mid - 1]) / 2 : arr[mid]

};