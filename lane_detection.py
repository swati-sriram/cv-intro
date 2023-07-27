import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_lines(img, threshold1:int = 50, threshold2:int = 150, apertureSize:int=3, minLineLength:int=100, maxLineGap:int=10):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to grayscale
    edges = cv2.Canny(gray, threshold1, threshold2, apertureSize) # detect edges
    lines = cv2.HoughLinesP(
                    edges,
                    1,
                    np.pi/180,
                    100,
                    minLineLength,
                    maxLineGap,
            ) # detect lines
    return lines



def draw_lines(img:str, lines:np.array, color:tuple = (0,255,0)):
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (color), 2)
        slope = (y2-y1)/(x2-x1)
        cv2.putText(img, f'{round(slope,3)}', (x1,y1),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1.5,
                    color=(225, 225, 225),
                    thickness=2)
    return plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))

def get_slopes_intercepts(lines):
    slopes = (lines[:, :, 3] - lines[:, :, 1]) / (lines[:, :, 1] - lines[:, :, 0])
    b = lines[:, :, 1] - slopes * lines[:, :, 0]
    intercepts = (np.zeros_like(slopes) - b) / slopes
    return slopes, intercepts


def detect_lanes(img, lines):
    
    def chunk(l, n):
        return [l[i:i+n] for i in range(0, len(l),n)]
    def avg_color(*colors):
        return np.average(colors)
    

    slopes, intercepts = get_slopes_intercepts(lines)
    sort = sorted(zip(lines, slopes, intercepts), key =lambda pair: pair[1])
    return chuck(sort)

def draw_lines(img, lanes):
    random_color = lambda: list(np.random.random(size=3) * 256)
    for pair in lanes:
        print(pair)
        color=random_color()
        for lane in pair:
            x1, y1, x2, y2 = lane[0][0]
            cv2.line(img, (x1,y1), (x2,y2), color, 2)