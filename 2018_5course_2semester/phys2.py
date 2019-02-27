import matplotlib.pyplot as plt
import matplotlib.widgets as wdg

def do_slider(pos, name, min, max, valinit, update_fn, fig):
    slide_ax = plt.axes(pos)
    slider = wdg.Slider(slide_ax, name, min, max, valinit)

    def update(val):
        slider_value = slider.val
        update_fn(slider_value)
        fig.canvas.draw_idle()
    slider.on_changed(update)

if __name__ == '__main__':
    slider_position = [0, 0, 1, 1]