import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

fig, ax = plt.subplots(figsize=(2.5,2.5))

plt.xlim(1.000000e-03, 1.000000e+02)
plt.ylim(1.000000e-03, 1.000000e+02)

x = np.array([1.000000e-03,1.122018e-03,1.258925e-03,1.412538e-03,1.584893e-03,1.778279e-03,1.995262e-03,2.238721e-03,2.511886e-03,2.818383e-03,3.162278e-03,3.548134e-03,3.981072e-03,4.466836e-03,5.011872e-03,5.623413e-03,6.309573e-03,7.079458e-03,7.943282e-03,8.912509e-03,1.000000e-02,1.122018e-02,1.258925e-02,1.412538e-02,1.584893e-02,1.778279e-02,1.995262e-02,2.238721e-02,2.511886e-02,2.818383e-02,3.162278e-02,3.548134e-02,3.981072e-02,4.466836e-02,5.011872e-02,5.623413e-02,6.309573e-02,7.079458e-02,7.943282e-02,8.912509e-02,1.000000e-01,1.122018e-01,1.258925e-01,1.412538e-01,1.584893e-01,1.778279e-01,1.995262e-01,2.238721e-01,2.511886e-01,2.818383e-01,3.162278e-01,3.548134e-01,3.981072e-01,4.466836e-01,5.011872e-01,5.623413e-01,6.309573e-01,7.079458e-01,7.943282e-01,8.912509e-01,1.000000e+00,1.122018e+00,1.258925e+00,1.412538e+00,1.584893e+00,1.778279e+00,1.995262e+00,2.238721e+00,2.511886e+00,2.818383e+00,3.162278e+00,3.548134e+00,3.981072e+00,4.466836e+00,5.011872e+00,5.623413e+00,6.309573e+00,7.079458e+00,7.943282e+00,8.912509e+00,1.000000e+01,1.122018e+01,1.258925e+01,1.412538e+01,1.584893e+01,1.778279e+01,1.995262e+01,2.238721e+01,2.511886e+01,2.818383e+01,3.162278e+01,3.548134e+01,3.981072e+01,4.466836e+01,5.011872e+01,5.623413e+01,6.309573e+01,7.079458e+01,7.943282e+01,8.912509e+01,1.000000e+02,])
y = np.array([3.121630e+00,3.112679e+00,3.101986e+00,3.089228e+00,3.074030e+00,3.055959e+00,3.034516e+00,3.009138e+00,2.979192e+00,2.943982e+00,2.902754e+00,2.854717e+00,2.799063e+00,2.735008e+00,2.661841e+00,2.578986e+00,2.486076e+00,2.383029e+00,2.270122e+00,2.148050e+00,2.017956e+00,1.881426e+00,1.740429e+00,1.597219e+00,1.454196e+00,1.313749e+00,1.178096e+00,1.049152e+00,9.284354e-01,8.170210e-01,7.155357e-01,6.241967e-01,5.428725e-01,4.711584e-01,4.084534e-01,3.540313e-01,3.071016e-01,2.668574e-01,2.325106e-01,2.033161e-01,1.785870e-01,1.577016e-01,1.401061e-01,1.253133e-01,1.128986e-01,1.024950e-01,9.378752e-02,8.650716e-02,8.042529e-02,7.534829e-02,7.111267e-02,6.758079e-02,6.463696e-02,6.218412e-02,6.014098e-02,5.843952e-02,5.702288e-02,5.584360e-02,5.486202e-02,5.404512e-02,5.336532e-02,5.279966e-02,5.232901e-02,5.193743e-02,5.161165e-02,5.134063e-02,5.111517e-02,5.092761e-02,5.077159e-02,5.064181e-02,5.053385e-02,5.044405e-02,5.036935e-02,5.030722e-02,5.025554e-02,5.021255e-02,5.017680e-02,5.014705e-02,5.012231e-02,5.010174e-02,5.008462e-02,5.007039e-02,5.005854e-02,5.004870e-02,5.004050e-02,5.003369e-02,5.002802e-02,5.002331e-02,5.001939e-02,5.001612e-02,5.001341e-02,5.001116e-02,5.000928e-02,5.000772e-02,5.000642e-02,5.000534e-02,5.000444e-02,5.000369e-02,5.000307e-02,5.000256e-02,5.000213e-02,])
c = "#3ba9e0"

hi_x = np.array([3.400000e-03,3.400000e-03,])
hi_y = np.array([2.873356e+00,2.873356e+00,])
lo_x = np.array([2.800000e+00,2.800000e+00,])
lo_y = np.array([5.064856e-02,5.064856e-02,])

plt.loglog(x,y,lw=3,color=c)
plt.scatter(hi_x,hi_y,marker='o',s=50,color='black',zorder=10)
plt.scatter(lo_x,lo_y,marker='o',s=50,edgecolors='black',color='none',zorder=10)

plt.title("$3 / A1_AmtR")

ax.xaxis.set_major_locator(ticker.LogLocator(numticks=3))
ax.yaxis.set_major_locator(ticker.LogLocator(numticks=3))

ax.set_aspect('equal')
plt.tight_layout()

plt.savefig("/root/output/response_plot_$3_A1_AmtR.png", bbox_inches='tight')
