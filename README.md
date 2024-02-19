# Merge Sort

Merge sort is a divide and conquer algorithm.

The array is recursively splitted in half. The sub-arrays are splitted again until it reaches a two length array. In this moment, the array is sorted by merging the values of the left and right sub-arrays, releasing the previous recursion call stack do to the same.

The original array is sorted by merging its two sorted halves, which were sorted by the recursive calls.

**`Time complexity lower bound`**: O(n \* log n)
**`Time complexity upper bound`**: O(n \* log n)

Different from the quick sort algorithm, in merge sort the array is always splitted in half, which optimizes the time complexity as shown below.

1. Splitting a 16 size array in half (always the case for merge sort)

```js
               16              //  ---> 16 items processed
            /      \
          8          8         //  ---> 16 items processed
        /  \        /  \
       4    4      4    4      //  ---> 16 items processed
      / \  / \    / \   / \
     2  2  2  2  2  2   2  2   //  ---> 16 items processed
```

64 items are processed along the sorting of all the arrays, following a n log(n) complexity
**`n log(n) = 16 * log2(16) = 64`**

2. Splitting a 16 size array by one value (worst case of quick sort, when the array is already sorted)

```js
                  16    //  ---> 16 items sorted
                 /
               15       //  ---> 15 items sorted
              /
            14          //  ---> 14 items sorted
           /
         13             //  ---> 13 items sorted
        /
      12                //  ---> 12 items sorted
     /
   ...                  //  ---> 63 items sorted
   /
  2                     //  ---> 2 items sorted
```

135 items are processed along the sorting of all the arrays, following a quadratic time complexity
**`(n (n - 1)) / 2 = (n^2 - n) / 2 = (16^2 - 16) / 2 = 120 (roughly 135)`**
