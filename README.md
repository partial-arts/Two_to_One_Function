Example applications of the program:
Function from 5 values to 1 value
Function from 1 value to 5 values

Notation: {p, q} -> r

Notation meaning: Function from {p, q} to r, where p ranges from 0 to t1-1, q ranges from 0 to t2-1, r ranges from 0 to t1•t2 -1.

Implementing the first part of the program, with the notation replaced by appropriate p, q, and r values for each line:

{Value1, Value2} -> K1

{Value3, Value4} -> K2

{K1, K2} -> K3

{K3, Value5} -> x

When all combined, it is essentially a function from {Value1, Value2, Value3, Value4, Value5} to x.

Similarly, reversing those operations using the second part of the program, we get a function from x to {Value1, Value2, Value3, Value4, Value5}.

x -> {K3, Value5}

K3 -> {K1, K2}

K2 -> {Value3, Value4}

K1 -> {Value1, Value2}
