// https://leetcode.com/problems/k-closest-points-to-origin

class Solution:

    def distance(self,point):
        return point[0]**2 + point[1]**2

    def partition(self,points, l, r):
        pivot = points[r]
        i = l
        for j in range(l, r):
            if self.distance(points[j]) <= self.distance(pivot):
                points[i], points[j] = points[j], points[i]
                i += 1
        points[i], points[r] = points[r], points[i]
        return i

    def kClosest(self,points, K):
        l, r = 0, len(points) - 1
        while l <= r:
            pivot_idx = random.randint(l, r)
            pivot_dist = self.distance(points[pivot_idx])
            points[r], points[pivot_idx] = points[pivot_idx], points[r]
            mid = self.partition(points, l, r)
            if mid == K:
                break
            elif mid < K:
                l = mid + 1
            else:
                r = mid - 1
        return points[:K]
