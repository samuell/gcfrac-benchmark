#!/usr/bin/env python
import string
 
A,T,G,C,N = map(ord, "ATGCN")

def main():
    file = open("chry_multiplied.fa","rb")
    a = 0
    t = 0
    g = 0
    c = 0
    for line in file:
        if line[0] != 62 and len(line) != line.count(N) + 1:
            g += line.count(G)
            c += line.count(C)
            a += line.count(A)
            t += line.count(T)
    totalBaseCount = a + t + c + g
    gcCount = g + c

    gcFraction = float(gcCount) / totalBaseCount
    print( gcFraction * 100 )
 
if __name__ == '__main__':
    main()