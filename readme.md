# Batch Rename

Batch rename or capitalize the first letter of all the files of a directory. Files can be ignored by placing in 'pfavd.txt' file.

Files will be renamed after arranging them according to their extension.

---



### Algorithm of  function ' arrange_by_extension() '

1. Get all the files of a directory in a list (which is randomly arranged).
2. Now extract all extensions using list comprehension and saving in a set to avoid repetitive values.
3. Convert the set back to list as subscripts can not be used with set.
4. Using functions to rename the files