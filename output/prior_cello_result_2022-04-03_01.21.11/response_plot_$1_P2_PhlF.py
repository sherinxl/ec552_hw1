import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

fig, ax = plt.subplots(figsize=(2.5,2.5))

plt.xlim(1.000000e-03, 1.000000e+02)
plt.ylim(1.000000e-03, 1.000000e+02)

x = np.array([1.000000e-03,1.122018e-03,1.258925e-03,1.412538e-03,1.584893e-03,1.778279e-03,1.995262e-03,2.238721e-03,2.511886e-03,2.818383e-03,3.162278e-03,3.548134e-03,3.981072e-03,4.466836e-03,5.011872e-03,5.623413e-03,6.309573e-03,7.079458e-03,7.943282e-03,8.912509e-03,1.000000e-02,1.122018e-02,1.258925e-02,1.412538e-02,1.584893e-02,1.778279e-02,1.995262e-02,2.238721e-02,2.511886e-02,2.818383e-02,3.162278e-02,3.548134e-02,3.981072e-02,4.466836e-02,5.011872e-02,5.623413e-02,6.309573e-02,7.079458e-02,7.943282e-02,8.912509e-02,1.000000e-01,1.122018e-01,1.258925e-01,1.412538e-01,1.584893e-01,1.778279e-01,1.995262e-01,2.238721e-01,2.511886e-01,2.818383e-01,3.162278e-01,3.548134e-01,3.981072e-01,4.466836e-01,5.011872e-01,5.623413e-01,6.309573e-01,7.079458e-01,7.943282e-01,8.912509e-01,1.000000e+00,1.122018e+00,1.258925e+00,1.412538e+00,1.584893e+00,1.778279e+00,1.995262e+00,2.238721e+00,2.511886e+00,2.818383e+00,3.162278e+00,3.548134e+00,3.981072e+00,4.466836e+00,5.011872e+00,5.623413e+00,6.309573e+00,7.079458e+00,7.943282e+00,8.912509e+00,1.000000e+01,1.122018e+01,1.258925e+01,1.412538e+01,1.584893e+01,1.778279e+01,1.995262e+01,2.238721e+01,2.511886e+01,2.818383e+01,3.162278e+01,3.548134e+01,3.981072e+01,4.466836e+01,5.011872e+01,5.623413e+01,6.309573e+01,7.079458e+01,7.943282e+01,8.912509e+01,1.000000e+02,])
y = np.array([4.100000e+00,4.100000e+00,4.100000e+00,4.100000e+00,4.100000e+00,4.100000e+00,4.100000e+00,4.099999e+00,4.099999e+00,4.099998e+00,4.099997e+00,4.099996e+00,4.099993e+00,4.099990e+00,4.099984e+00,4.099975e+00,4.099961e+00,4.099940e+00,4.099907e+00,4.099855e+00,4.099775e+00,4.099651e+00,4.099458e+00,4.099159e+00,4.098694e+00,4.097972e+00,4.096851e+00,4.095111e+00,4.092413e+00,4.088229e+00,4.081749e+00,4.071726e+00,4.056258e+00,4.032468e+00,3.996073e+00,3.940841e+00,3.858043e+00,3.736169e+00,3.561518e+00,3.320614e+00,3.005250e+00,2.619517e+00,2.185055e+00,1.738900e+00,1.322166e+00,9.659854e-01,6.839446e-01,4.738165e-01,3.242673e-01,2.212647e-01,1.519130e-01,1.059291e-01,7.574851e-02,5.607240e-02,4.330065e-02,3.503404e-02,2.969325e-02,2.624684e-02,2.402458e-02,2.259237e-02,2.166962e-02,2.107524e-02,2.069242e-02,2.044588e-02,2.028712e-02,2.018488e-02,2.011905e-02,2.007666e-02,2.004936e-02,2.003178e-02,2.002047e-02,2.001318e-02,2.000849e-02,2.000546e-02,2.000352e-02,2.000227e-02,2.000146e-02,2.000094e-02,2.000060e-02,2.000039e-02,2.000025e-02,2.000016e-02,2.000010e-02,2.000007e-02,2.000004e-02,2.000003e-02,2.000002e-02,2.000001e-02,2.000001e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,])
c = "#f9a427"

hi_x = np.array([7.315833e-02,])
hi_y = np.array([3.692351e+00,])
lo_x = np.array([4.566456e+00,2.136604e+00,2.503010e+00,])
lo_y = np.array([2.000502e-02,2.009164e-02,2.005003e-02,])

plt.loglog(x,y,lw=3,color=c)
plt.scatter(hi_x,hi_y,marker='o',s=50,color='black',zorder=10)
plt.scatter(lo_x,lo_y,marker='o',s=50,edgecolors='black',color='none',zorder=10)

plt.title("$1 / P2_PhlF")

ax.xaxis.set_major_locator(ticker.LogLocator(numticks=3))
ax.yaxis.set_major_locator(ticker.LogLocator(numticks=3))

ax.set_aspect('equal')
plt.tight_layout()

plt.savefig("/root/output/response_plot_$1_P2_PhlF.png", bbox_inches='tight')
