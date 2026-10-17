class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # distance = 0
        # for i in range(len(points)):
        #     for j in range(i+1,len(points)):
        #         a = abs(points[i][0] - points[j][0])
        #         distance = max(distance,a)

        # return distance


        x_coords = sorted([p[0] for p in points])
        max_width = 0
 
        for i in range(1, len(x_coords)):
            width = x_coords[i] - x_coords[i - 1]
            max_width = max(max_width, width)
            
        return max_width