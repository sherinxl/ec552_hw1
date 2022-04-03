import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

fig, ax = plt.subplots(figsize=(2.5,2.5))

plt.xlim(1.000000e-03, 1.000000e+02)
plt.ylim(1.000000e-03, 1.000000e+02)

x = np.array([1.000000e-03,1.122018e-03,1.258925e-03,1.412538e-03,1.584893e-03,1.778279e-03,1.995262e-03,2.238721e-03,2.511886e-03,2.818383e-03,3.162278e-03,3.548134e-03,3.981072e-03,4.466836e-03,5.011872e-03,5.623413e-03,6.309573e-03,7.079458e-03,7.943282e-03,8.912509e-03,1.000000e-02,1.122018e-02,1.258925e-02,1.412538e-02,1.584893e-02,1.778279e-02,1.995262e-02,2.238721e-02,2.511886e-02,2.818383e-02,3.162278e-02,3.548134e-02,3.981072e-02,4.466836e-02,5.011872e-02,5.623413e-02,6.309573e-02,7.079458e-02,7.943282e-02,8.912509e-02,1.000000e-01,1.122018e-01,1.258925e-01,1.412538e-01,1.584893e-01,1.778279e-01,1.995262e-01,2.238721e-01,2.511886e-01,2.818383e-01,3.162278e-01,3.548134e-01,3.981072e-01,4.466836e-01,5.011872e-01,5.623413e-01,6.309573e-01,7.079458e-01,7.943282e-01,8.912509e-01,1.000000e+00,1.122018e+00,1.258925e+00,1.412538e+00,1.584893e+00,1.778279e+00,1.995262e+00,2.238721e+00,2.511886e+00,2.818383e+00,3.162278e+00,3.548134e+00,3.981072e+00,4.466836e+00,5.011872e+00,5.623413e+00,6.309573e+00,7.079458e+00,7.943282e+00,8.912509e+00,1.000000e+01,1.122018e+01,1.258925e+01,1.412538e+01,1.584893e+01,1.778279e+01,1.995262e+01,2.238721e+01,2.511886e+01,2.818383e+01,3.162278e+01,3.548134e+01,3.981072e+01,4.466836e+01,5.011872e+01,5.623413e+01,6.309573e+01,7.079458e+01,7.943282e+01,8.912509e+01,1.000000e+02,])
y = np.array([2.099995e+00,2.099993e+00,2.099990e+00,2.099986e+00,2.099981e+00,2.099974e+00,2.099964e+00,2.099950e+00,2.099931e+00,2.099904e+00,2.099868e+00,2.099818e+00,2.099748e+00,2.099653e+00,2.099521e+00,2.099338e+00,2.099087e+00,2.098740e+00,2.098261e+00,2.097600e+00,2.096688e+00,2.095431e+00,2.093698e+00,2.091311e+00,2.088025e+00,2.083506e+00,2.077300e+00,2.068793e+00,2.057166e+00,2.041329e+00,2.019866e+00,1.990973e+00,1.952424e+00,1.901610e+00,1.835676e+00,1.751856e+00,1.648024e+00,1.523459e+00,1.379632e+00,1.220730e+00,1.053500e+00,8.862698e-01,7.273677e-01,5.835415e-01,4.589756e-01,3.551445e-01,2.713241e-01,2.053900e-01,1.545755e-01,1.160274e-01,8.713365e-02,6.567070e-02,4.983404e-02,3.820651e-02,2.970038e-02,2.349427e-02,1.897505e-02,1.568886e-02,1.330173e-02,1.156899e-02,1.031193e-02,9.400330e-03,8.739435e-03,8.260398e-03,7.913229e-03,7.661655e-03,7.479369e-03,7.347294e-03,7.251604e-03,7.182277e-03,7.132051e-03,7.095664e-03,7.069303e-03,7.050206e-03,7.036372e-03,7.026349e-03,7.019088e-03,7.013828e-03,7.010018e-03,7.007257e-03,7.005257e-03,7.003809e-03,7.002759e-03,7.001999e-03,7.001448e-03,7.001049e-03,7.000760e-03,7.000551e-03,7.000399e-03,7.000289e-03,7.000209e-03,7.000152e-03,7.000110e-03,7.000080e-03,7.000058e-03,7.000042e-03,7.000030e-03,7.000022e-03,7.000016e-03,7.000012e-03,7.000008e-03,])
c = "#006838"

hi_x = np.array([2.600000e-03,2.600000e-03,])
hi_y = np.array([2.099924e+00,2.099924e+00,])
lo_x = np.array([8.800000e+00,8.800000e+00,])
lo_y = np.array([7.007520e-03,7.007520e-03,])

plt.loglog(x,y,lw=3,color=c)
plt.scatter(hi_x,hi_y,marker='o',s=50,color='black',zorder=10)
plt.scatter(lo_x,lo_y,marker='o',s=50,edgecolors='black',color='none',zorder=10)

plt.title("$3 / S4_SrpR")

ax.xaxis.set_major_locator(ticker.LogLocator(numticks=3))
ax.yaxis.set_major_locator(ticker.LogLocator(numticks=3))

ax.set_aspect('equal')
plt.tight_layout()

plt.savefig("/root/output/response_plot_$3_S4_SrpR.png", bbox_inches='tight')
