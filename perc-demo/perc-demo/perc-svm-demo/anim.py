import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)
print line
line2, = ax.plot([], [], lw=1)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    line2.set_data([], [])
    return line, line2

# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(-10, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    line2.set_data(y, x)
    
    return line, line2

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=1, blit=True)

plt.show()
