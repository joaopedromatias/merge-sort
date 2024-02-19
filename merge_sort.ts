function mergeSort(arr: (number | string)[]) {
  if (arr.length > 1) {
    const middle = Math.floor(arr.length / 2)
    const leftArr = arr.slice(0, middle)
    const rightArr = arr.slice(middle)

    mergeSort(leftArr)
    mergeSort(rightArr)

    let indexFillingArr = 0
    let indexSearchingLeftArr = 0
    let indexSearchingRightArr = 0

    while (indexSearchingLeftArr < leftArr.length && indexSearchingRightArr < rightArr.length) {
      const leftValue = leftArr[indexSearchingLeftArr]
      const rightValue = rightArr[indexSearchingRightArr]

      if (leftValue < rightValue) {
        arr[indexFillingArr] = leftValue
        indexSearchingLeftArr++
      } else {
        arr[indexFillingArr] = rightValue
        indexSearchingRightArr++
      }
      indexFillingArr++
    }

    while (indexSearchingLeftArr < leftArr.length) {
      arr[indexFillingArr] = leftArr[indexSearchingLeftArr]
      indexFillingArr++
      indexSearchingLeftArr++
    }

    while (indexSearchingRightArr < rightArr.length) {
      arr[indexFillingArr] = rightArr[indexSearchingRightArr]
      indexFillingArr++
      indexSearchingRightArr++
    }
  }
  return arr
}

const arr = [100, -5, 14, -98, 167, 8, 4, 2, 51, 86, 57, 3, 1, -200]
console.log(mergeSort(arr))

export {}
