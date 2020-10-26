### in place

> list.sort(reverse=True|False, key=\_fun\_returns\_key)
```
def myFunc(e): return len(e)
li = ['aaa', 'a', 'aa']
li.sort(key=myFunc)
print(li) ['a', 'aa', 'aaa']
```
