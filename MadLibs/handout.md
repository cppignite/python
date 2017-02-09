# Handout #2 

### Array/Lists
 
Arrays are ordered arrangement of things that are related in some way. Ex: grocery list, to do lists...

#### Initialization/Creation

To create an empty list/array, we will use:

`list = []`

To create a predetermined array, we can use:

`list = ["a thing", "another thing"]`

#### Access

To get to a specific _element_ in the list, we will need an _index_. Indices starts from **0** as the first _element_ and count onwards.

```
value = list[0] 
#This will take the first element of list and assign it to value.

value2 = list[4] 
#This will take the fifth element of list and assign it to value2.
``` 
#### Assignment & Modification

We might need to add or modify some elements:

```
list[0] = "first element"
list[0] = "changed element"
```

#### Methods

Methods are additional tools that can be used, we will use the following to add an element to the end of list:

`list.append("new element")`

### String

Strings are sequences of characters, that is a ordered arrangement of characters.

#### Initialization
There are many ways to create a string:
```
string = "whatever betweeen these"
string2 = 'or these'
string3 = '''even these!'''
paragraph = """These can extend
 				 on multiple
 				 lines"""
```
 
#### Operators
 
Operators are symbols that define actions on things. With strings, we can do the following:

```
concatenation = "hello" + " world"
#This will join the 2 strings together, resulting in "hello world"

fanatic = "cats! " * 3
#This will assign fanatic "cats! cats! cats! "
```

#### Formatting

We create more versatile and powerful string using formatting. Formatting requires placeholders to indicate strings to look for.

```
aGreeting = "Hello, {}!"
print(aGreeting.format("Dave"))
#This will print out "Hello, Dave!" to the console

aComplicatedFormula = "{} + {} = {}"
print(aComplicatedFormula.format("Dave","Cats","Happy Dave"))
#We can even do multiple placeholders!
```

## Additional Reference

### Lists

#### Initialization

You can even mix different _types_ together:

`list = ["a string", 1, 'C', 12.5]`

Even other Lists!

`list = [[1,2], [3,4]]`

#### Access

Phython suppose _negative indicing_, that means negative values will count from the back!

```
secondLast = list[-2] 
#This will assign secondLast the second last element in list
```

Python makes getting part of the list (sublist/splicing) really easy!

```
list = [0,1,2,4]

secondHalf = list[2:]
#This will assign secondHalf with list's elements starting from index 2 to the end of list

middleOnly = list[1:3]
#This will assign middleOnly with list's elements from index 1 to 2, excluding 3
```

#### Assignment & Modification

We can also delete elements from the list:

```
del list[1]
#This will delete the element
```

#### Methods

List have the following methods:

| Python List Methods | functionality                                              |
|---------------------|------------------------------------------------------------|
| append()            | Add an element to the end of the list                      |
| extend()            | Add all elements of a list to the another list             |
| insert()            | Insert an item at the defined index                        |
| remove()            | Removes an item from the list                              |
| pop()               | Removes and returns an element at the given index          |
| clear()             | Removes all items from the list                            |
| index()             | Returns the index of the first matched item                |
| count()             | Returns the count of number of items passed as an argument |
| sort()              | Sort items in a list in ascending order                    |
| reverse()           | Reverse the order of items in the list                     |
| copy()              | Returns a shallow copy of the list                         |

### Strings

#### Escape Sequences

Sometimes we want to type a quote or special symbols that are already mean something in python, we will need to _escape_ it:

```
aYodaQuote = ""Do or do not, there is no try.""
#This will not work!
aBetterQuote = "\"To the hand you talk, because listening I\'m not.\""
#All the Offending characters are preceeded by a '\'
```

| Escape Sequence | Description                         |
|-----------------|-------------------------------------|
| \newline        | Backslash and newline ignored       |
| \\\             | Backslash                           |
| \\'             | Single quote                        |
| \\"             | Double quote                        |
| \\a             | ASCII Bell                          |
| \b              | ASCII Backspace                     |
| \f              | ASCII Formfeed                      |
| \n              | ASCII Linefeed                      |
| \r              | ASCII Carriage Return               |
| \t              | ASCII Horizontal Tab                |
| \v              | ASCII Vertical Tab                  |
| \ooo            | Character with octal value ooo      |
| \xHH            | Character with hexadecimal value HH |

