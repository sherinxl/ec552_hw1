import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

fig, ax = plt.subplots(figsize=(2.5,2.5))

plt.xlim(1.000000e-03, 1.000000e+02)
plt.ylim(1.000000e-03, 1.000000e+02)

x = np.array([1.000000e-03,1.122018e-03,1.258925e-03,1.412538e-03,1.584893e-03,1.778279e-03,1.995262e-03,2.238721e-03,2.511886e-03,2.818383e-03,3.162278e-03,3.548134e-03,3.981072e-03,4.466836e-03,5.011872e-03,5.623413e-03,6.309573e-03,7.079458e-03,7.943282e-03,8.912509e-03,1.000000e-02,1.122018e-02,1.258925e-02,1.412538e-02,1.584893e-02,1.778279e-02,1.995262e-02,2.238721e-02,2.511886e-02,2.818383e-02,3.162278e-02,3.548134e-02,3.981072e-02,4.466836e-02,5.011872e-02,5.623413e-02,6.309573e-02,7.079458e-02,7.943282e-02,8.912509e-02,1.000000e-01,1.122018e-01,1.258925e-01,1.412538e-01,1.584893e-01,1.778279e-01,1.995262e-01,2.238721e-01,2.511886e-01,2.818383e-01,3.162278e-01,3.548134e-01,3.981072e-01,4.466836e-01,5.011872e-01,5.623413e-01,6.309573e-01,7.079458e-01,7.943282e-01,8.912509e-01,1.000000e+00,1.122018e+00,1.258925e+00,1.412538e+00,1.584893e+00,1.778279e+00,1.995262e+00,2.238721e+00,2.511886e+00,2.818383e+00,3.162278e+00,3.548134e+00,3.981072e+00,4.466836e+00,5.011872e+00,5.623413e+00,6.309573e+00,7.079458e+00,7.943282e+00,8.912509e+00,1.000000e+01,1.122018e+01,1.258925e+01,1.412538e+01,1.584893e+01,1.778279e+01,1.995262e+01,2.238721e+01,2.511886e+01,2.818383e+01,3.162278e+01,3.548134e+01,3.981072e+01,4.466836e+01,5.011872e+01,5.623413e+01,6.309573e+01,7.079458e+01,7.943282e+01,8.912509e+01,1.000000e+02,])
y = np.array([2.099978e+00,2.099970e+00,2.099958e+00,2.099942e+00,2.099920e+00,2.099890e+00,2.099848e+00,2.099790e+00,2.099710e+00,2.099600e+00,2.099447e+00,2.099237e+00,2.098947e+00,2.098547e+00,2.097995e+00,2.097233e+00,2.096183e+00,2.094734e+00,2.092738e+00,2.089989e+00,2.086206e+00,2.081006e+00,2.073871e+00,2.064102e+00,2.050768e+00,2.032643e+00,2.008144e+00,1.975283e+00,1.931653e+00,1.874506e+00,1.800968e+00,1.708469e+00,1.595392e+00,1.461884e+00,1.310575e+00,1.146845e+00,9.783090e-01,8.135188e-01,6.602928e-01,5.243389e-01,4.086330e-01,3.136008e-01,2.378025e-01,1.787464e-01,1.335693e-01,9.949133e-02,7.405687e-02,5.522351e-02,4.135975e-02,3.119834e-02,2.377416e-02,1.836245e-02,1.442436e-02,1.156215e-02,9.483742e-03,7.975486e-03,6.881491e-03,6.088247e-03,5.513217e-03,5.096447e-03,4.794420e-03,4.575566e-03,4.416993e-03,4.302101e-03,4.218862e-03,4.158556e-03,4.114866e-03,4.083214e-03,4.060284e-03,4.043672e-03,4.031638e-03,4.022920e-03,4.016604e-03,4.012029e-03,4.008714e-03,4.006313e-03,4.004573e-03,4.003313e-03,4.002400e-03,4.001739e-03,4.001260e-03,4.000912e-03,4.000661e-03,4.000479e-03,4.000347e-03,4.000251e-03,4.000182e-03,4.000132e-03,4.000096e-03,4.000069e-03,4.000050e-03,4.000036e-03,4.000026e-03,4.000019e-03,4.000014e-03,4.000010e-03,4.000007e-03,4.000005e-03,4.000004e-03,4.000003e-03,4.000002e-03,])
c = "#006838"

hi_x = np.array([2.500000e-02,2.500000e-02,])
hi_y = np.array([1.933698e+00,1.933698e+00,])
lo_x = np.array([3.100000e-01,3.100000e-01,])
lo_y = np.array([2.489540e-02,2.489540e-02,])

plt.loglog(x,y,lw=3,color=c)
plt.scatter(hi_x,hi_y,marker='o',s=50,color='black',zorder=10)
plt.scatter(lo_x,lo_y,marker='o',s=50,edgecolors='black',color='none',zorder=10)

plt.title("$2 / S3_SrpR")

ax.xaxis.set_major_locator(ticker.LogLocator(numticks=3))
ax.yaxis.set_major_locator(ticker.LogLocator(numticks=3))

ax.set_aspect('equal')
plt.tight_layout()

plt.savefig("/root/output/response_plot_$2_S3_SrpR.png", bbox_inches='tight')
