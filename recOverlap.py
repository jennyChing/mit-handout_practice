class Solution(object):
    def computeOverlap(self,A,B,C,D,E,F,G,H):
        isPair = False
        overlap = max(0,min(C,G)-max(A,E))*min(0,min(D,H)-max(B,F))
        if overlap != 0:
            return True
if __name__ == "__main__":
    try:
        rec =

