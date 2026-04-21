/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
    if (s.length <= 1) return s;

    let maxDistance = 1;
    let begin = 0;
    const size = s.length;

    function expand(left, right) {
        while (
            left >= 0 &&
            right < size &&
            s[left] === s[right]
        ) {
            left--;
            right++;
        }

        return [left + 1, right - 1];
    }

    for (let i = 0; i < size; i++) {
        let [l1, r1] = expand(i, i);
        let [l2, r2] = expand(i, i + 1);

        if (r1 - l1 + 1 > maxDistance) {
            begin = l1;
            maxDistance = r1 - l1 + 1;
        }

        if (r2 - l2 + 1 > maxDistance) {
            begin = l2;
            maxDistance = r2 - l2 + 1;
        }
    }

    return s.slice(begin, begin + maxDistance);
};