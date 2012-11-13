Graphs manually edited by outputing .txt file from the .py file,
(i.e. run python X.py > X.txt)
and then using .txt file to generate the .eps file, 
(i.e. run dot -Teps X.txt > X.eps, as in edz.sh)
(or run neato -Teps X.txt > X.eps)
are the following.

ex_K_f5 >ex_K_f5_fix 
(Edge labels: a=x1, b=x2, c=x3, x=z1, y=z2, z=z3, r=y1, s=y2, t=y3, )
labels of edges adjusted
45 > 43= a1 (moves left)
3 > 4= a1
3 > 2=c1 (moves left and down)
1 > 2=b1 (moves down)
44 > 30=z1 (moves left)
2 > 29=c2 (down, right)
25 > 35=y1 (left)
25 > 34=b2 (left)
25 > 49=x1 (left)
49 > 36=a1
36 > 38=x2 (more left than x1)
13 > 30=b3 (down, left)
36 > 29=z2 (down)
13 > 31=a2 (up, left)
31 > 32=a1
39 > 42=z3 (more left than z1)
39 > 32=x1 (left a little bit)
30 > 42=c1
15 > 31=x1 
35 > 13=b4 (up left)
34 > 13=c3 (down)
15 > 39=a3 (down) 

ex_K_folded 
overlap=scalexy;nodesep=0.5;rotate=270;

u1 (up, left)
y3 (right)

8 > 54=x3 (up)
7 > 8=t1 (right)
6 > 7=r1 (right)
6 > 5=s1 (up left)
4 > 5=y2 (up)
28 > 20=y5 (left, a little)
21 > 20=u2 (down )
51 > 17=x4 (right)
16 > 17=a4 (right)
25 > 34=b4
25 > 49=x5 (up, left)
25 > 35=y4 (down)
25 > 38=a5 (down, left)
49 > 36=a6 (down and left more)
34 > 13=c1
1 > 25=a7 (right and up)
36 > 1=a8 (left and up)
36 > 29=z4 (right a little)
1 > 13=z5 (up and left)
1 > 12=y6 (down and right)
1 > 2=b5 (right)
45 > 43=a1
45 > 2=z6 (up right) 
43 > 3=b6 (up right)
2 > 10=a9 (left up)
54 > 10=z5
15 > 31=x3
31 > 15=x6
31 > 32=a11
14 > 15=a10 (up)
15 > 39=a1
13 > 30=b7
44 > 30=z1
32 > 39=x7 (down)
39 > 32=x8 (down right)
30 > 42=c4 (left)
29 > 30=c3
12 > 29=b4
2 > 29=c1
32 > 14=a7
14 > 13=x5
13 > 14=x5
43 > 1=y6
12 > 13=y7