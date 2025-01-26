# Learning Content

## QUICK SORT
▶ Quick sort selects a pivot to divide the list into smaller parts, recursively sorts each part, and then combines the sorted portions to produce the final sorted list.

▶ Quick sort terminates when all partitions are reduced to individual elements, leaving nothing further to sort or divide.

```Python
qsort [] = []
qsort [x:xs] = qsort smaller ++ [x] ++ qsort larger
                where 
                    smaller = filter(<=x) xs
                    larger = filter(>x) xs
```