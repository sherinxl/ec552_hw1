import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

fig, ax = plt.subplots(figsize=(2.5,2.5))

plt.xlim(1.000000e-03, 1.000000e+02)
plt.ylim(1.000000e-03, 1.000000e+02)

x = np.array([1.000000e-03,1.122018e-03,1.258925e-03,1.412538e-03,1.584893e-03,1.778279e-03,1.995262e-03,2.238721e-03,2.511886e-03,2.818383e-03,3.162278e-03,3.548134e-03,3.981072e-03,4.466836e-03,5.011872e-03,5.623413e-03,6.309573e-03,7.079458e-03,7.943282e-03,8.912509e-03,1.000000e-02,1.122018e-02,1.258925e-02,1.412538e-02,1.584893e-02,1.778279e-02,1.995262e-02,2.238721e-02,2.511886e-02,2.818383e-02,3.162278e-02,3.548134e-02,3.981072e-02,4.466836e-02,5.011872e-02,5.623413e-02,6.309573e-02,7.079458e-02,7.943282e-02,8.912509e-02,1.000000e-01,1.122018e-01,1.258925e-01,1.412538e-01,1.584893e-01,1.778279e-01,1.995262e-01,2.238721e-01,2.511886e-01,2.818383e-01,3.162278e-01,3.548134e-01,3.981072e-01,4.466836e-01,5.011872e-01,5.623413e-01,6.309573e-01,7.079458e-01,7.943282e-01,8.912509e-01,1.000000e+00,1.122018e+00,1.258925e+00,1.412538e+00,1.584893e+00,1.778279e+00,1.995262e+00,2.238721e+00,2.511886e+00,2.818383e+00,3.162278e+00,3.548134e+00,3.981072e+00,4.466836e+00,5.011872e+00,5.623413e+00,6.309573e+00,7.079458e+00,7.943282e+00,8.912509e+00,1.000000e+01,1.122018e+01,1.258925e+01,1.412538e+01,1.584893e+01,1.778279e+01,1.995262e+01,2.238721e+01,2.511886e+01,2.818383e+01,3.162278e+01,3.548134e+01,3.981072e+01,4.466836e+01,5.011872e+01,5.623413e+01,6.309573e+01,7.079458e+01,7.943282e+01,8.912509e+01,1.000000e+02,])
y = np.array([6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.800000e+00,6.799999e+00,6.799999e+00,6.799999e+00,6.799998e+00,6.799996e+00,6.799994e+00,6.799990e+00,6.799984e+00,6.799974e+00,6.799957e+00,6.799930e+00,6.799887e+00,6.799817e+00,6.799703e+00,6.799519e+00,6.799220e+00,6.798734e+00,6.797948e+00,6.796672e+00,6.794604e+00,6.791254e+00,6.785826e+00,6.777043e+00,6.762846e+00,6.739948e+00,6.703141e+00,6.644296e+00,6.551033e+00,6.405237e+00,6.182138e+00,5.851683e+00,5.385069e+00,4.768830e+00,4.023115e+00,3.210560e+00,2.420368e+00,1.732510e+00,1.189147e+00,7.919257e-01,5.176907e-01,3.357604e-01,2.182360e-01,1.436171e-01,9.675825e-02,6.753509e-02,4.938890e-02,3.815121e-02,3.120345e-02,2.691237e-02,2.426380e-02,2.262967e-02,2.162168e-02,2.100001e-02,2.061664e-02,2.038023e-02,2.023445e-02,2.014456e-02,2.008914e-02,2.005496e-02,2.003389e-02,2.002090e-02,2.001288e-02,2.000794e-02,2.000490e-02,2.000302e-02,2.000186e-02,2.000115e-02,2.000071e-02,2.000044e-02,2.000027e-02,2.000017e-02,2.000010e-02,2.000006e-02,2.000004e-02,2.000002e-02,2.000001e-02,2.000001e-02,2.000001e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,])
c = "#f9a427"

hi_x = np.array([1.526875e-01,])
hi_y = np.array([6.585990e+00,])
lo_x = np.array([7.570643e+00,3.870191e+00,3.853139e+00,])
lo_y = np.array([2.001577e-02,2.026398e-02,2.026892e-02,])

plt.loglog(x,y,lw=3,color=c)
plt.scatter(hi_x,hi_y,marker='o',s=50,color='black',zorder=10)
plt.scatter(lo_x,lo_y,marker='o',s=50,edgecolors='black',color='none',zorder=10)

plt.title("$1 / P3_PhlF")

ax.xaxis.set_major_locator(ticker.LogLocator(numticks=3))
ax.yaxis.set_major_locator(ticker.LogLocator(numticks=3))

ax.set_aspect('equal')
plt.tight_layout()

plt.savefig("/root/output/response_plot_$1_P3_PhlF.png", bbox_inches='tight')