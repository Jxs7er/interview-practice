/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
    if (s.length === 1) return s
    let palindromic = s[0];
    let left = 0
    let right = 1

    let sub_reverse = s[left] //a
    let subtext = sub_reverse //a

    let stop = false
    while (!stop) {
        sub_reverse = s[right] + sub_reverse // ba /bba
        subtext += s[right] // ab / abb

        palindromic = subtext === sub_reverse ?
            palindromic.length < sub_reverse.length ?
                subtext 
                : palindromic
            : palindromic //a /a

        if (right === (s.length - 1)) {
            left += 1 //l:1
            right = left + 1 //r:2 
            if (left >= s.length - 1) break
            subtext = s[left] //b
            sub_reverse = s[left] //b
        } else right++ //r: 2

        stop = left === s.length - 1 //f /
    }

    return palindromic
};