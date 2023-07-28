import numpy as np

def get_lane_center(lanes:np.ndarray):
    height, width, depth = img.shape()
    center = width/2
    min = 10000000000
    closest_lane = np.zeros_like(lane[1])
    for lane in lanes:
        # [[[x1,y1,x2,y2],slope,intercept],[[x1,y1,x2,y2],slope,intercept]]
        intercepts = lane[:,2]
        for i in range(0,len(intercepts)-1):
            if intercepts[i]<min:
                min = intercepts[i]
                closest_lane = lane
        midpoint1 = [(lane[0,2]-lane[1,2])/2,0]
        midpoint2 = [((lane[0,2]+lane[0,1])-(lane[1,2]+lane[1,1])),1]
        center_slope = (midpoint1[1]-midpoint2[1])/(midpoint1[0]-midpoint2[0])
        center_intercept = midpoint1[0]
    # [[[[x1,y1,x2,y2],slope,intercept],[[x1,y1,x2,y2],slope,intercept]]]
    return(center_intercept, center_slope)
