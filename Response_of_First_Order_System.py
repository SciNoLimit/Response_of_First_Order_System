from scipy.integrate import odeint 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

fig, ax = plt.subplots()
plt.subplots_adjust(left = 0.1, bottom = 0.35)

num = 51
t = np.linspace(0, 35, num) 
Gain = np.zeros(num)

y0 = 0
k = 6.00
tou = 3.00
Gain[0:]= k  # step input

def eqn(y, t, k, tou):
    u = 1
    dydt = ((k*u)-y)/tou
    return dydt

soln = odeint(eqn, y0, t, args = (k, tou))
#plotting Response curve
Plot_Data, = plt.plot(t, soln, label = 'Response') 
# plotting gain value
Plot_Gain, = plt.plot(t, Gain, color='orange', linestyle='dashed', label = 'Gain')
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.legend()
plt.ylim(0, 11) # putting y limits
#ax.margins(x=0, y=0)


# configuring sliders

Gain_slider_config = plt.axes([0.2, 0.1, 0.7, 0.05])
Time_Const_slider_config = plt.axes([0.2, 0.2, 0.7, 0.05])

# making sliders

Gain_slider = Slider(   ax= Gain_slider_config,
                        label= 'Gain',
                        valmin= 0,
                        valmax= 10,
                        valinit= k,
                        valfmt= '%.2f',
                        color= 'orange' )

Time_Const_slider = Slider( ax= Time_Const_slider_config,
                            label= 'Time Constant',
                            valmin= 0,
                            valmax= 6,
                            valinit= tou,
                            valfmt= '%.2f' )

# Refreshing  when gain and tou is changed

def refresh(val):
    k = Gain_slider.val
    tou = Time_Const_slider.val
    Plot_Gain.set_ydata(k)

    y0 = 0
    soln = odeint(eqn, y0, t, args = (k, tou))
    Plot_Data.set_ydata(soln)
    plt.draw()

Gain_slider.on_changed(refresh)
Time_Const_slider.on_changed(refresh)

#making reset botton

Reset_config = plt.axes([0.1, 0.9, 0.1, 0.04])
Reset_button = Button(ax= Reset_config, label = 'Reset')

# resetting

def Reset(event):
    Gain_slider.reset()
    Time_Const_slider.reset()

Reset_button.on_clicked(Reset) 

plt.show()


