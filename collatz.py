import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def collatz(n):
    # Generate the Collatz sequence for the given number
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Set up the plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

# Add a slider for the input number
slider_ax = plt.axes([0.1, 0.1, 0.8, 0.03])
slider = Slider(slider_ax, 'Number', 1, 1000, valinit=1, valstep=1, valfmt='%0.0f')

# Function to update the plot when the slider is moved
def update(val):
    # Clear the previous plot
    ax.clear()
    
    # Generate the Collatz sequence and plot it
    sequence = collatz(int(val))
    ax.plot(sequence, 'o-')
    
    # Update the plot labels and title
    ax.set_xlabel('Steps')
    ax.set_ylabel('Number')
    ax.set_title('Collatz sequence for {}'.format(int(val)))
    fig.canvas.draw_idle()

# Update the plot when the slider is moved
slider.on_changed(update)

# Show the plot
plt.show()
