# Numerical library
import numpy as np

# Visualization library
import matplotlib.pyplot as plt

# Interactive library
import ipywidgets as widgets

class PID_Controller(object):
    """
    Class containing all relevant information for the PID controller
    Funktionen:
        set_params(self, K_p=1, K_i=1, K_d=1)
        set_target(self, target=1)
        reset(self)
        __call__(self, x_vec, dt)
    """

    def __init__(self):
        """set all attributes of the controller"""
        self.set_params()
        self.set_target()
        self.reset()

    def set_params(self, K_p=1, K_i=1, K_d=1):
        """set and reset the controller parameters"""
        self.K_p, self.K_i, self.K_d = K_p, K_i, K_d

    def set_target(self, target=1):
        """Set the desired position"""
        self.target = target

    def reset(self):
        """Reset the control errors"""
        self.int_err, self.last_err = 0, 0

    def __call__(self, x_vec, dt):
        """
        The control function with the PID control:
        - Proportional Difference
        - Integral Difference
        - Differential Difference
        """
        # current system vector
        x, dx = x_vec
        # calculate current error
        # P-Part
        err = self.target - x
        p_part = self.K_p * err
        # calculate the integral error
        # I-Part
        self.int_err += dt * err
        i_part = self.K_i * self.int_err
        # calculate the difference error using temporal differences
        # D-Part
        diff_err = (err - self.last_err) / dt
        d_part = self.K_d * diff_err
        # update last err
        self.last_err = err
        # Sum the parts together
        u = p_part + i_part + d_part
        return u

    def call1(self, x_vec, dt):
        """
        The control function with the PID control:
        - Proportional Difference
        - Integral Difference
        - Differential Difference
        """
        # current system vector
        x, dx = x_vec
        # calculate current error
        # P-Part
        err = self.target - x
        p_part = self.K_p * err
        # calculate the integral error
        # I-Part
        self.int_err += dt * err
        i_part = self.K_i * self.int_err
        # calculate the difference error using temporal differences
        # D-Part
        diff_err = (err - self.last_err) / dt
        d_part = self.K_d * diff_err
        # update last err
        self.last_err = err
        # Sum the parts together
        u = p_part + i_part + d_part
        return u

class Ode_Model(PID_Controller):

    def __init__(self):
        """Initialise the ODE object"""
        #self.controller = controller
        super().__init__()

class Euler_Simulator(Ode_Model):
    """class containing general simulator information"""

    def __init__(self):
        """setup for simulator"""
        self.set_simulation_params()
        #self.system = system
        super().__init__()

    def set_simulation_params(self, t0=0, tf=10, dt=0.05):
        """set the simulation parameters"""
        self.t0, self.tf, self.dt = t0, tf, dt

    def __call__(self, x0):
        """perform the simulation"""
        # reset before simulation
        sim.reset()

        # time vector
        tt = np.arange(self.t0, self.tf + self.dt, self.dt)

        # init the trajectory
        x_traj = np.zeros([tt.shape[0], 2])

        # iterate through the vector
        for i, t in enumerate(tt):
            x_traj[i, :] = x0

            dxdt = self(x0, self.dt)
            x0 += dxdt * self.dt

        return x_traj

    def call2(self, x0):
        """perform the simulation"""
        # reset before simulation
        sim.reset()

        # time vector
        tt = np.arange(self.t0, self.tf + self.dt, self.dt)

        # init the trajectory
        x_traj = np.zeros([tt.shape[0], 2])

        # iterate through the vector
        for i, t in enumerate(tt):
            x_traj[i, :] = x0

            dxdt = self(x0, self.dt)
            x0 += dxdt * self.dt

        return x_traj

# Define update Function
def update_demo(argument):
    print(2 * argument)






def visualize_results(t, x_traj, x_des, figsize=(10,6)):
    """function to visualize all results"""
    fig = plt.figure(figsize=figsize)
    plt.plot(t, x_traj[:, 0], label='position')
    plt.plot(t, x_traj[:, 1], label='velocity')
    plt.plot(t, x_des, 'r--', label='x_des')
    plt.grid(0.1)
    plt.ylim([-2, 5])
    plt.legend()
    plt.xlabel('time in s')
    plt.ylabel('x')
    plt.show()



def update_controls(K_p, K_i, K_d):
    """
    linked function to sliders and replots
    """
    # perform calculation
    sim.set_params(K_p=K_p, K_i=K_i, K_d=K_d)
    x_traj = sim(x0)
    # visualize result
    visualize_results(t, x_traj, x_des)


if __name__ == "__main__":
    # Setup the objects
    #controller = PID_Controller()
    #system = Ode_Model(controller)
    sim = Euler_Simulator()

    # initial state
    x0 = [0, 0]
    x_traj = sim(x0)

    # vectors for plotting
    t = np.arange(sim.t0, sim.tf + sim.dt, sim.dt)
    x_des = np.ones(t.shape) * sim.target




    K_p = widgets.FloatSlider(min=0, max=10, value=5, description='P:')
    K_i = widgets.FloatSlider(min=0, max=10, value=5, description='I:')
    K_d = widgets.FloatSlider(min=0, max=10, value=5, description='D:')

    widgets.interactive(update_controls, K_p=K_p, K_i=K_i, K_d=K_d)