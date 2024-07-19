#!/usr/bin/python3.11

import sys

def harmonic_mean(*Y1):
    s=0
    if 0.0 in Y1:
      sys.exit('0 cannot be used!')
    else:
        for y1 in Y1:
          s+=1/y1
    s=len(Y1)/s
    return s

def main():
  n = int(input("How many elements? "))
  X1 = list(map(float, input("\nEnter the numbers : ").strip().split()))[:n]
  print(f"{harmonic_mean(*X1)}")

if __name__ == '__main__':
    main()


