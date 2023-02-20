import numpy as np
import imageio

png=imageio.imread("Frame 66.png")
W=np.array([0.299, 0.587, 0.114, 1])
imageio.imwrite("Frame_gray.png", png.dot(W))
