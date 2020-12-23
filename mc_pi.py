import numpy as np
import cv2 
import random
import math
import matplotlib.pyplot as plt


def point(img,w,h,colour):
    img[h,w]=colour


def mc_pi(window_size,points):
    r = window_size//2
    height, width = window_size+1, window_size+1
    img = np.zeros((height, width, 3), np.uint8)

    cv2.rectangle(img,(0,0),(r*2,r*2),(255,255,255),2)
    cv2.circle(img,(r,r), r, (255,255,255), 2)


    total_counter = 0
    circle_counter = 0
    while True:
        for _ in range(10):
            x = random.randint(0,2*r)
            y = random.randint(0,2*r)

            dist = math.sqrt( (r - x)**2 + (r - y)**2 )

            if dist < r:
                point(img,x,y,(0,255,0))
                circle_counter += 1
                
            else:
                point(img,x,y,(0,0,255))

            total_counter += 1
        

            pi = (circle_counter/total_counter) * 4

        if(total_counter > points):
            print("points =",points," : ","pi =",pi)
            break

        cv2.imshow('pi', img)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    return pi

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords="offset points",
                    ha='center', va='bottom')




points = []
pies = []
while True:
    print("Enter number of points")
    key = input()
    if(key == "q"):
        break
    num_of_points = int(key)
    if num_of_points > 0 :
        points.append(num_of_points)
        pi = mc_pi(600,num_of_points)
        pies.append(pi)
points.sort()

x = np.arange(len(points))
width = 0.35

fig, ax = plt.subplots()
rect1 = ax.bar(x , pies, width)


ax.set_ylabel('PI')
ax.set_title('Number Of Points')
ax.set_xticks(x)
ax.set_xticklabels(points)

autolabel(rect1)

fig.tight_layout()

plt.show() 

