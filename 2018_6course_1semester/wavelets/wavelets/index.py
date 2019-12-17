from wavelets import haar_my
from WorkWData import signals, output_res
import matplotlib.pyplot as plt


# save fig, output in file, output in console
def output(type_signal, type_transform, u, x, y):
    output_res.plot_wt(type_signal, type_transform, u, x, y)
    output_res.file_output('signals/' + type_signal + '_' + type_transform + '_all.txt', u, x, y)
    output_res.console_output(u, x, y)


if __name__ == "__main__":
    # type transform: haar (1), DobWT (2)
    # type signal: constant, linear, quadratic, linear_with_noise
    type_transform = "DobWT"; type_signal = "nonlinear_w_noise"

    u = output_res.write_to_list('signals/adaptive_func_w_noise.txt')
    x = output_res.write_to_list('signals/adaptive_func_w_noise_wt.txt')
    y = output_res.write_to_list('signals/adaptive_func_w_noise_inv.txt')

    # output_res.write_to_file(u, 'signals/' + type_signal + '.txt')
    output(type_signal, type_transform, u, x, y)
