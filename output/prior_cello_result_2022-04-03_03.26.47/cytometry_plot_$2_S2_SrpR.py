import matplotlib.pyplot as plt
import numpy as np

num_plots = 4

fig, ax = plt.subplots(num_plots, 1, sharex=True, sharey=True)
fig.set_size_inches(4, 1*num_plots)

fig.suptitle("$2 / S2_SrpR")

for a in ax:
    a.set_xscale('log')
    a.set_yscale('log')
    a.set_xlim(1.000000e-03, 1.000000e+02)

ax[0].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,2.162850e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,2.162850e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,3.380186e-05,0.000000e+00,2.162850e-05,0.000000e+00,5.543036e-05,0.000000e+00,0.000000e+00,0.000000e+00,4.325699e-05,5.543036e-05,0.000000e+00,5.543036e-05,4.325699e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,2.162850e-05,0.000000e+00,8.923222e-05,2.162850e-05,9.868735e-05,5.543036e-05,5.543036e-05,5.543036e-05,6.488549e-05,3.380186e-05,4.325699e-05,5.543036e-05,4.325699e-05,8.923222e-05,5.543036e-05,7.705885e-05,2.162850e-05,0.000000e+00,2.162850e-05,4.325699e-05,2.162850e-05,2.162850e-05,1.014056e-04,0.000000e+00,3.380186e-05,2.162850e-05,2.162850e-05,0.000000e+00,3.380186e-05,0.000000e+00,0.000000e+00,0.000000e+00,2.162850e-05,0.000000e+00,4.325699e-05,5.543036e-05,0.000000e+00,5.543036e-05,0.000000e+00,0.000000e+00,3.380186e-05,0.000000e+00,0.000000e+00,0.000000e+00,5.543036e-05,0.000000e+00,0.000000e+00,0.000000e+00,2.162850e-05,3.380186e-05,0.000000e+00,0.000000e+00,2.162850e-05,6.760372e-05,3.380186e-05,6.760372e-05,3.380186e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,3.380186e-05,1.352074e-04,2.366130e-04,2.366130e-04,4.948546e-04,7.990713e-04,1.800954e-03,2.554050e-03,3.934490e-03,5.836849e-03,8.371989e-03,1.072453e-02,1.569872e-02,1.986971e-02,2.382027e-02,3.151587e-02,3.758083e-02,4.364720e-02,4.921269e-02,5.398609e-02,5.728036e-02,5.849924e-02,6.188286e-02,6.381418e-02,6.038518e-02,5.443664e-02,4.946115e-02,4.645822e-02,3.844386e-02,3.555723e-02,2.970749e-02,2.431219e-02,2.107288e-02,1.561009e-02,1.247101e-02,9.396809e-03,8.126165e-03,6.141545e-03,4.661352e-03,4.784386e-03,3.340478e-03,3.245927e-03,2.899754e-03,2.445555e-03,1.889951e-03,1.412707e-03,1.495202e-03,1.236960e-03,9.152511e-04,5.245204e-04,8.760128e-04,6.286442e-04,5.826690e-04,4.866999e-04,3.055172e-04,3.082354e-04,1.973747e-04,4.312695e-04,2.311766e-04,2.866069e-04,2.311766e-04,2.217214e-04,1.662911e-04,5.543036e-05,1.635728e-04,2.162850e-05,1.108607e-04,0.000000e+00,0.000000e+00,4.325699e-05,0.000000e+00,6.760372e-05,0.000000e+00,2.162850e-05,2.162850e-05,0.000000e+00,4.325699e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[1].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,2.162850e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,2.162850e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,3.380186e-05,0.000000e+00,2.162850e-05,0.000000e+00,5.543036e-05,0.000000e+00,0.000000e+00,0.000000e+00,4.325699e-05,5.543036e-05,0.000000e+00,5.543036e-05,4.325699e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,2.162850e-05,0.000000e+00,8.923222e-05,2.162850e-05,9.868735e-05,5.543036e-05,5.543036e-05,5.543036e-05,6.488549e-05,3.380186e-05,4.325699e-05,5.543036e-05,4.325699e-05,8.923222e-05,5.543036e-05,7.705885e-05,2.162850e-05,0.000000e+00,2.162850e-05,4.325699e-05,2.162850e-05,2.162850e-05,1.014056e-04,0.000000e+00,3.380186e-05,2.162850e-05,2.162850e-05,0.000000e+00,3.380186e-05,0.000000e+00,0.000000e+00,0.000000e+00,2.162850e-05,0.000000e+00,4.325699e-05,5.543036e-05,0.000000e+00,5.543036e-05,0.000000e+00,0.000000e+00,3.380186e-05,0.000000e+00,0.000000e+00,0.000000e+00,5.543036e-05,0.000000e+00,0.000000e+00,0.000000e+00,2.162850e-05,3.380186e-05,0.000000e+00,0.000000e+00,2.162850e-05,6.760372e-05,3.380186e-05,6.760372e-05,3.380186e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,3.380186e-05,1.352074e-04,2.366130e-04,2.366130e-04,4.948546e-04,7.990713e-04,1.800954e-03,2.554050e-03,3.934490e-03,5.836849e-03,8.371989e-03,1.072453e-02,1.569872e-02,1.986971e-02,2.382027e-02,3.151587e-02,3.758083e-02,4.364720e-02,4.921269e-02,5.398609e-02,5.728036e-02,5.849924e-02,6.188286e-02,6.381418e-02,6.038518e-02,5.443664e-02,4.946115e-02,4.645822e-02,3.844386e-02,3.555723e-02,2.970749e-02,2.431219e-02,2.107288e-02,1.561009e-02,1.247101e-02,9.396809e-03,8.126165e-03,6.141545e-03,4.661352e-03,4.784386e-03,3.340478e-03,3.245927e-03,2.899754e-03,2.445555e-03,1.889951e-03,1.412707e-03,1.495202e-03,1.236960e-03,9.152511e-04,5.245204e-04,8.760128e-04,6.286442e-04,5.826690e-04,4.866999e-04,3.055172e-04,3.082354e-04,1.973747e-04,4.312695e-04,2.311766e-04,2.866069e-04,2.311766e-04,2.217214e-04,1.662911e-04,5.543036e-05,1.635728e-04,2.162850e-05,1.108607e-04,0.000000e+00,0.000000e+00,4.325699e-05,0.000000e+00,6.760372e-05,0.000000e+00,2.162850e-05,2.162850e-05,0.000000e+00,4.325699e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[2].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,6.125081e-03,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.890755e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,6.739335e-03,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,5.672264e-05,0.000000e+00,0.000000e+00,0.000000e+00,6.685407e-03,0.000000e+00,0.000000e+00,5.672264e-05,0.000000e+00,0.000000e+00,7.945968e-03,0.000000e+00,7.563019e-05,0.000000e+00,8.384465e-03,0.000000e+00,1.701679e-04,0.000000e+00,7.824794e-03,2.780238e-04,7.563019e-05,7.358350e-03,3.725615e-04,7.861298e-03,3.403359e-04,7.520962e-03,4.131713e-04,8.161024e-03,3.564487e-04,8.571401e-03,6.316778e-04,9.630396e-03,8.948896e-03,7.318049e-04,9.820127e-03,8.913220e-03,9.628913e-03,9.858598e-03,9.317179e-03,9.898552e-03,1.023050e-02,1.013317e-02,1.184620e-02,1.038242e-02,2.017115e-02,1.215711e-02,2.143533e-02,1.255286e-02,2.190392e-02,2.089457e-02,1.390581e-02,2.236263e-02,2.006561e-02,2.867845e-02,2.267799e-02,2.105456e-02,2.908013e-02,2.708759e-02,2.764529e-02,2.525225e-02,2.478384e-02,2.261620e-02,2.693833e-02,2.545088e-02,2.330922e-02,2.363576e-02,2.464362e-02,1.943628e-02,2.103538e-02,2.148161e-02,1.737453e-02,1.716375e-02,1.794966e-02,1.411221e-02,1.360088e-02,1.353019e-02,1.057384e-02,9.916186e-03,7.445196e-03,9.454676e-03,7.849328e-03,6.521348e-03,6.313365e-03,4.893642e-03,4.546232e-03,4.004814e-03,4.541298e-03,3.252617e-03,2.648887e-03,3.395494e-03,2.959136e-03,2.587230e-03,2.503871e-03,2.153012e-03,1.760059e-03,2.199211e-03,1.722244e-03,1.754469e-03,1.458194e-03,1.191349e-03,1.145149e-03,1.196938e-03,1.048472e-03,9.840210e-04,5.203718e-04,7.732432e-04,8.467341e-04,6.198435e-04,3.908137e-04,5.820284e-04,5.336899e-04,4.447416e-04,5.175771e-04,2.563215e-04,3.830850e-04,3.747008e-04,2.507321e-04,1.968042e-04,5.581869e-04,2.185064e-04,1.078559e-04,1.267634e-04,1.295581e-04,1.995989e-04,2.829578e-04,1.484657e-04,1.456710e-04,1.617838e-04,1.617838e-04,1.239687e-04,7.283548e-05,9.174303e-05,3.502039e-05,3.502039e-05,1.078559e-04,1.078559e-04,3.781509e-05,1.078559e-04,1.645785e-04,3.502039e-05,3.502039e-05,1.050612e-04,3.781509e-05,5.672264e-05,5.392793e-05,3.502039e-05,5.392793e-05,3.502039e-05,3.781509e-05,5.392793e-05,1.890755e-05,5.392793e-05,7.004077e-05,0.000000e+00,3.502039e-05,3.781509e-05,0.000000e+00,0.000000e+00,0.000000e+00,1.890755e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.890755e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.890755e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[3].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,6.125081e-03,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.890755e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,6.739335e-03,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,5.672264e-05,0.000000e+00,0.000000e+00,0.000000e+00,6.685407e-03,0.000000e+00,0.000000e+00,5.672264e-05,0.000000e+00,0.000000e+00,7.945968e-03,0.000000e+00,7.563019e-05,0.000000e+00,8.384465e-03,0.000000e+00,1.701679e-04,0.000000e+00,7.824794e-03,2.780238e-04,7.563019e-05,7.358350e-03,3.725615e-04,7.861298e-03,3.403359e-04,7.520962e-03,4.131713e-04,8.161024e-03,3.564487e-04,8.571401e-03,6.316778e-04,9.630396e-03,8.948896e-03,7.318049e-04,9.820127e-03,8.913220e-03,9.628913e-03,9.858598e-03,9.317179e-03,9.898552e-03,1.023050e-02,1.013317e-02,1.184620e-02,1.038242e-02,2.017115e-02,1.215711e-02,2.143533e-02,1.255286e-02,2.190392e-02,2.089457e-02,1.390581e-02,2.236263e-02,2.006561e-02,2.867845e-02,2.267799e-02,2.105456e-02,2.908013e-02,2.708759e-02,2.764529e-02,2.525225e-02,2.478384e-02,2.261620e-02,2.693833e-02,2.545088e-02,2.330922e-02,2.363576e-02,2.464362e-02,1.943628e-02,2.103538e-02,2.148161e-02,1.737453e-02,1.716375e-02,1.794966e-02,1.411221e-02,1.360088e-02,1.353019e-02,1.057384e-02,9.916186e-03,7.445196e-03,9.454676e-03,7.849328e-03,6.521348e-03,6.313365e-03,4.893642e-03,4.546232e-03,4.004814e-03,4.541298e-03,3.252617e-03,2.648887e-03,3.395494e-03,2.959136e-03,2.587230e-03,2.503871e-03,2.153012e-03,1.760059e-03,2.199211e-03,1.722244e-03,1.754469e-03,1.458194e-03,1.191349e-03,1.145149e-03,1.196938e-03,1.048472e-03,9.840210e-04,5.203718e-04,7.732432e-04,8.467341e-04,6.198435e-04,3.908137e-04,5.820284e-04,5.336899e-04,4.447416e-04,5.175771e-04,2.563215e-04,3.830850e-04,3.747008e-04,2.507321e-04,1.968042e-04,5.581869e-04,2.185064e-04,1.078559e-04,1.267634e-04,1.295581e-04,1.995989e-04,2.829578e-04,1.484657e-04,1.456710e-04,1.617838e-04,1.617838e-04,1.239687e-04,7.283548e-05,9.174303e-05,3.502039e-05,3.502039e-05,1.078559e-04,1.078559e-04,3.781509e-05,1.078559e-04,1.645785e-04,3.502039e-05,3.502039e-05,1.050612e-04,3.781509e-05,5.672264e-05,5.392793e-05,3.502039e-05,5.392793e-05,3.502039e-05,3.781509e-05,5.392793e-05,1.890755e-05,5.392793e-05,7.004077e-05,0.000000e+00,3.502039e-05,3.781509e-05,0.000000e+00,0.000000e+00,0.000000e+00,1.890755e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.890755e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.890755e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])


plt.savefig("/root/output/cytometry_plot_$2_S2_SrpR.png", bbox_inches='tight')