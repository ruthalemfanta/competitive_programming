class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        def xend(point):
            return point[1]

        points.sort(key=xend)
        arrows = 1
        arrow_pos = points[0][1]

        for start, end in points:
            if start > arrow_pos:
                arrows += 1
                arrow_pos = end

        return arrows
