import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib.animation as animation

#@Time and classical path
t1, t2 = 0, 1
q1, q2 = 0, 1
t = np.linspace(t1, t2, 200)
q_classical = q1 + (q2 - q1)*(t - t1)/(t2 - t1)

#@Variation functions
def f1(t): return np.sin(np.pi*(t - t1)/(t2 - t1))
def f2(t): return np.sin(2*np.pi*(t - t1)/(t2 - t1))

#@Create figure and axes
fig = plt.figure(figsize=(18,5))
ax_param = fig.add_subplot(1,3,1)
ax_path = fig.add_subplot(1,3,2)
ax_3d = fig.add_subplot(1,3,3, projection='3d')
plt.subplots_adjust(bottom=0.23, left=0.058, right=0.955, top=0.88, wspace=0.345, hspace=0.28)

#@Sliders
ax_a = plt.axes([0.15, 0.12, 0.7, 0.03])
ax_b = plt.axes([0.15, 0.07, 0.7, 0.03])
slider_a = Slider(ax_a, 'A', -1, 1, valinit=0.0)
slider_b = Slider(ax_b, 'B', -1, 1, valinit=0.0)

#@2D path plot
line_classical, = ax_path.plot(t, q_classical, 'k--', lw=2, label='Classical Path')
line_current, = ax_path.plot(t, q_classical, 'r', lw=2, label='Current Path')
line_f1, = ax_path.plot(t, slider_a.val*f1(t), 'g--', alpha=0.3, label='a*f1')
line_f2, = ax_path.plot(t, slider_b.val*f2(t), 'b--', alpha=0.3, label='b*f2')
ax_path.plot([t1, t2], [q1, q2], 'bo', label='Boundary Conditions')
ax_path.set_xlabel('Time')
ax_path.set_ylabel('Position q(t)')
ax_path.set_title('Path Variation')
ax_path.set_ylim(min(q1,q2)-0.5, max(q1,q2)+0.5)
ax_path.legend()

#@2D parameter space
a_vals = np.linspace(-1,1,100)
b_vals = np.linspace(-1,1,100)
A, B = np.meshgrid(a_vals, b_vals)
S = 0.5 + (np.pi**2/4)*A**2 + 2*np.pi**2*B**2
CS = ax_param.contour(A, B, S, levels=15, colors='w', linewidths=0.1)
ax_param.clabel(CS, inline=True, fontsize=8)
c = ax_param.pcolormesh(A, B, S, shading='auto', cmap='cividis', alpha=0.6)
fig.colorbar(c, ax=ax_param, label='Action S(a,b)')
selected_point, = ax_param.plot(0,0,'ro')
ax_param.set_xlabel('a')
ax_param.set_ylabel('b')
ax_param.set_title('Parameter Space [a x b]')
ax_param.set_xlim(-1,1)
ax_param.set_ylim(-1,1)
ax_param.axhline(0, color='white', lw=0.5)
ax_param.axvline(0, color='white', lw=0.5)

#@3D action surface
a_vals3d = np.linspace(-1,1,50)
b_vals3d = np.linspace(-1,1,50)
A3, B3 = np.meshgrid(a_vals3d, b_vals3d)
S3 = 0.5 + (np.pi**2/4)*A3**2 + 2*np.pi**2*B3**2
S_relative = S3 - 0.5
surf = ax_3d.plot_surface(A3, B3, S_relative, cmap='cividis', alpha=0.8)
ax_3d.scatter(0,0,0, color='red', s=50, label='Classical Path')  #@ ΔS = 0
dot_var = ax_3d.scatter(0,0,0, color='blue', s=50, label='Current Variation')
ax_3d.set_xlabel('a')
ax_3d.set_ylabel('b')
ax_3d.set_zlabel('ΔS')
ax_3d.set_title('Action Surface')
ax_3d.legend()

#@Update function
def update(val):
    a = slider_a.val
    b = slider_b.val
    #@ Update 2D path
    q_current = q_classical + a*f1(t) + b*f2(t)
    line_current.set_ydata(q_current)
    line_f1.set_ydata(a*f1(t))
    line_f2.set_ydata(b*f2(t))
    #@ Update 2D param
    selected_point.set_data(a,b)
    #@ Update 3D variation dot (ΔS surface)
    S_val = 0.5 + (np.pi**2/4)*a**2 + 2*np.pi**2*b**2
    dot_var._offsets3d = ([a],[b],[S_val-0.5])
    fig.canvas.draw_idle()

slider_a.on_changed(update)
slider_b.on_changed(update)

#@Parameter space click
def on_click(event):
    if event.inaxes != ax_param:
        return
    slider_a.set_val(event.xdata)
    slider_b.set_val(event.ydata)
fig.canvas.mpl_connect('button_press_event', on_click)

#@Animate particle along current path
particle, = ax_path.plot(t1, q_classical[0], 'ro', markersize=8)
def animate(i):
    a = slider_a.val
    b = slider_b.val
    q_current = q_classical + a*f1(t) + b*f2(t)
    particle.set_data(t[i], q_current[i])
    return particle,
ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=50, blit=False)

plt.show()
