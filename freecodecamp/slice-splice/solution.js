const frankenSplice = (arr1, arr2, indx) => {
  const result_array = Array.from(arr2)
  result_array.splice(indx, 0, arr1)
  return result_array.flat()
}

console.log(frankenSplice([1, 2, 3], [4, 5], 1))
console.log(frankenSplice([1, 2], ["a", "b"], 1))
console.log(frankenSplice(["claw", "tentacle"], ["head", "shoulders", "knees", "toes"], 2))
console.log(frankenSplice([1, 2, 3, 4], [], 0))
