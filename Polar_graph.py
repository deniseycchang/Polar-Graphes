import matplotlib.pyplot as plt
import numpy as np
import os



# Set angular coordinates (angle, polar angle)
x = np.linspace(0, 2 * np.pi, 400)


# Set radial coordinates (radius), the distance from the pole
y00 = np.sin(3 * x)
y01 = np.sin(4 * x)
y02 = -2 * np.cos(x)
y10 = np.sin(0.5*x)
y11 = 1 + np.cos(x)
y12 = x


# Six polar axes
f, axarr = plt.subplots(2, 3, subplot_kw=dict(projection='polar'))

axarr[0, 0].plot(x, y00)
axarr[0, 0].set_title('(I)', loc='left')
axarr[0, 1].plot(x, y01)
axarr[0, 1].set_title('(II)', loc='left')
axarr[0, 2].plot(x, y02)
axarr[0, 2].set_title('(III)', loc='left')
axarr[1, 0].plot(x, y10)
axarr[1, 0].set_title('(IV)', loc='left')
axarr[1, 1].plot(x, y11)
axarr[1, 1].set_title('(V)', loc='left')
axarr[1, 2].plot(x, y12)
axarr[1, 2].set_title('(VI)', loc='left')


# Fine-tune figure; make subplots farther from each other.
f.subplots_adjust(hspace=0.5)

# Set polar labels in radian instead of degree
xT=plt.xticks()[0]
xL=['0',r'$\frac{\pi}{4}$',r'$\frac{\pi}{2}$',r'$\frac{3\pi}{4}$',\
    r'$\pi$',r'$\frac{5\pi}{4}$',r'$\frac{3\pi}{2}$',r'$\frac{7\pi}{4}$']
plt.setp(axarr, xticks=xT, xticklabels=xL)



# Present the graph
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized() # Maximize the graph

# Save graphes in eps and png in the same folder
script_dir = os.path.dirname(__file__) 
filename_eps = script_dir + '/polar.eps'
filename_png = script_dir + '/polar.png'
f.savefig(filename_eps)
f.savefig(filename_png)

plt.show()