
import numpy as np
def main():
# p = 4
# q = 20 (0,1,2,3,4,5,6,7,8,....19)
p = 4
q = 20
x = []
while len(x) < p:
tmp = np.random.randint(1,q)
if tmp not in x:
x.append(tmp)


return (x)


main()


#def ransac(P1, P2):

#    iterate 100 times;
smallest = np.inf
for i in range(100):
#step 1: randomly select points pairs
random select 4 pairs of points as q1 , q2
#step 2: compute H by using q1 and q2
H = computeH(q1,q2)
P1 = normalize(P1)
P2 = normalize(P2)
x = H * P2
x = normalize(x)
# step 3: compute SSD
using the median norm (P1-x) as los
ssd = sqrt(sum(los).^2))
current = ssd
# step 4: find biggest 'current' save into smallest
if current < smallest:
smallest = current
P1_inliers = extract the inliers from P1(idx,:)
P2_inliers = extract the inliers from P2(idx,:)
# step 5: reconstruct H from inliers points pair
bestH = computeH(P1_inliers,P2_inliers)

end



#
# Your previous C++ content is preserved below:
#
# How would you select P random distinct numbers out of 0..Q-1 (with P <= Q)?
#
#

