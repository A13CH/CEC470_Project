import matplotlib.pyplot as plt
import matplotlib.animation as animation

def gen_animated_graph(generator,sample_data:list,name:str):
    """animated plot generation function"""
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(sample_data)), sample_data, color='skyblue')

    # Formatting the plot
    ax.set_title(f"{name} Visualization")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")

    def update(arr):
        for bar, height in zip(bars, arr):
            bar.set_height(height)
        return bars

    """Uses the animation function to animate the grpah"""
    ani = animation.FuncAnimation(fig, func=update, frames=generator, repeat=False, blit=False, interval=300)
    ani = animation.FuncAnimation(
        fig, func=update, frames=generator,
        repeat=False, blit=False, interval=10
    )
    plt.show()