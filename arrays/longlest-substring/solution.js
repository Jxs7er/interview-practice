/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  const map_aux = new Map();

  let maxLength = 0;
  let left = 0;

  const array = [...s]; //Convert to array

  for (let right = 0; right < array.length; right++) {
    let char = array[right];

    left =
      map_aux.get(char) !== undefined && map_aux.get(char) >= left
        ? map_aux.get(char) + 1
        : left;

    map_aux.set(char, right);
    maxLength = Math.max(maxLength, right - left + 1);
  }

  return maxLength;
};
