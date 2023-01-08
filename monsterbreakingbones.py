import random
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Initialize the figure and the axes
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

# Add the logarithmic slider
axcolor = 'lightgoldenrodyellow'
ax_trials = plt.axes([0.1, 0.1, 0.8, 0.03], facecolor=axcolor)
trials_slider = Slider(ax_trials, 'Trials', 1, 1000000, valinit=100, valstep=1, valfmt='%d')

# Initialize variables to store the results and the overall average
results = []
overall_average = 0

def update(val):
    global results, overall_average

    # Get the number of trials from the slider
    num_trials = int(trials_slider.val)

    # Run the calculation num_trials times
    results = []
    overall_average = 0
    for i in range(num_trials):
        # Generate two random numbers between 0 and 1
        num1 = random.uniform(0, 1)
        num2 = random.uniform(0, 1)

        # Determine which number is larger and which is smaller
        if num1 > num2:
            larger = num1
            smaller = num2
        else:
            larger = num2
            smaller = num1

        # Calculate and store the quotient
        quotient = larger / smaller
        results.append(quotient)
        overall_average += quotient

    # Calculate the overall average
    overall_average /= num_trials

    # Clear the plot and create the scatterplot
    ax.clear()
    ax.scatter(range(num_trials), results, s=1)

    # Add a red line to show the average and a label next to the line displaying the average value
    ax.axhline(y=overall_average, color='red')
    ax.text(num_trials + 5, overall_average, f"Average: {overall_average:.2f}", color='red')

    # Update the plot
    fig.canvas.draw_idle()

# Set the update function as the slider's onchange event handler
trials_slider.on_changed(update)

# Show the plot
plt.show()
