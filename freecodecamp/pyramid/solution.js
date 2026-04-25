const pyramid = (pattern, rows, isDownwards) => {
  let string = ""
  let counter = 1
  let space = rows-1

  const formatTo = () =>
    `${" ".repeat(space--)}${pattern.repeat(counter)}\n`

  for (let i = 0; i < rows; i++) {
    string = isDownwards ?
      formatTo() + string
      : string + formatTo()
    counter += 2
  }

  return `\n${string}`
}

console.log(pyramid("p", 5, true))