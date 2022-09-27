import sys
import argparse


def createParser():
    parser=argparse.ArgumentParser()
    parser.add_argument('number', type=int)
    parser.add_argument('-n', nargs='?', type=int)

    return parser


i=1
def fib(n):
    if n<=2:
        return(1)
    else:
        A=[1, 1]
        i=2
        while i<n:
            i+=1
            t=A[1]
            A[1]+=A[0]
            A[0]=t
        return(A[1])

        


if __name__ == "__main__":
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        sys.exit("error: exactly 1 argument is required")

    parser = createParser()
    args = parser.parse_args()

    n=args.n
    if n is None:
        n=args.number

    print(fib(n))   

    
