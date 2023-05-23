# Response of First Order System

This Python script, named `Response_of_First_Order_System.py`, demonstrates the response of a first-order system using the scipy library for numerical integration (`odeint`), numpy for numerical computations, and matplotlib for plotting.

The script simulates the response of a first-order system to a step input. It calculates the response curve and plots it along with the input gain value. The user can interactively change the gain and time constant values using sliders, and the plot will update accordingly.

## Prerequisites

Make sure you have the following libraries installed:

- scipy
- numpy
- matplotlib

## Usage

1. Run the script using a Python interpreter.
2. A plot window will open, showing the response of the dynamic system.
3. Use the sliders to adjust the system parameters:
   - **Gain**: Controls the gain value of the system.
   - **Time Constant**: Controls the time constant of the system.
4. The plot will dynamically update to reflect the changes in the system parameters.
5. Click the **Reset** button to reset the sliders to their initial values.

    ![](plot_1.PNG)

    ![](plot_2.PNG)


## System Description

The dynamic system is represented by the following first-order ordinary differential equation (ODE):

```math
\frac{dy}{dt} = \frac{k \cdot u - y}{\tau}
```



where:
- `y` is the system response variable.
- `t` is the time variable.
- `k` is the gain parameter.
- `tau` is the time constant parameter.
- `u` is the input, which is set to a constant value of 1.

## Visualized Data

The script visualizes the following data:

- **Response**: The system response variable `y` over time.
- **Gain**: The constant gain value of the system.

    ![](plot_1.PNG)

## Customization

You can modify the following parameters in the script to customize the simulation:

- `num`: Number of points in the time array.
- `t`: Time array defining the simulation duration.
- `y0`: Initial condition for the system response.
- `k`: Initial value for the gain.
- `tou`: Initial value for the time constant.

## License

This code is provided under an MIT License. Refer to the license file for more information.

## Author

- Prajwal Dutta
- GitHub: [SciNoLimits](https://github.com/SciNoLimits)
