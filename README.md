# Column data parcer

## Description

-   Takes data from lines where odd lines are variant (3) + answer letter(A) like `3A` and even lines - scores `2`. For example `data.txt`

```
3A
2
```

-   Outputs `json` file containing array of objects with a key: answer number `3`) and value: array of variant `A` and score `2`. For example `out.json`:

```
{ "3": ["A", 2] }
```
