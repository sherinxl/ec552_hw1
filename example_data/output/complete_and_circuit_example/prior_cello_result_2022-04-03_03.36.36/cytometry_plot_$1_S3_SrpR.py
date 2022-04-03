import matplotlib.pyplot as plt
import numpy as np

num_plots = 4

fig, ax = plt.subplots(num_plots, 1, sharex=True, sharey=True)
fig.set_size_inches(4, 1*num_plots)

fig.suptitle("$1 / S3_SrpR")

for a in ax:
    a.set_xscale('log')
    a.set_yscale('log')
    a.set_xlim(1.000000e-03, 1.000000e+02)

ax[0].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [2.876909e-04,1.232961e-04,1.780944e-04,2.054935e-04,1.506953e-04,3.561888e-04,1.095965e-04,2.876909e-04,1.095965e-04,2.739914e-04,2.328927e-04,2.465922e-04,2.191931e-04,3.287896e-04,2.876909e-04,2.876909e-04,3.561888e-04,1.917940e-04,5.342832e-04,3.561888e-04,4.657853e-04,3.561888e-04,3.424892e-04,4.520858e-04,6.027810e-04,5.205836e-04,5.342832e-04,7.534763e-04,7.671758e-04,7.671758e-04,7.808754e-04,8.493732e-04,7.945750e-04,7.808754e-04,5.616823e-04,9.863689e-04,8.493732e-04,1.000068e-03,1.438455e-03,1.383656e-03,1.082266e-03,1.219262e-03,8.904720e-04,1.411056e-03,1.753545e-03,1.822043e-03,1.589150e-03,1.548051e-03,1.835742e-03,2.465922e-03,1.945339e-03,1.822043e-03,2.411124e-03,2.918008e-03,2.356326e-03,2.644017e-03,3.753682e-03,2.657716e-03,3.548188e-03,3.835879e-03,3.452291e-03,4.082471e-03,3.835879e-03,4.589355e-03,4.890746e-03,4.438660e-03,6.315501e-03,5.438729e-03,6.055209e-03,7.507364e-03,6.712789e-03,7.384067e-03,7.123776e-03,7.781355e-03,8.712926e-03,9.178711e-03,9.754093e-03,1.067196e-02,1.141174e-02,1.209672e-02,1.198712e-02,1.417905e-02,1.393246e-02,1.554901e-02,1.598740e-02,1.546681e-02,1.838482e-02,1.946709e-02,2.054935e-02,2.082334e-02,2.190561e-02,2.250839e-02,2.254949e-02,2.333037e-02,2.519351e-02,2.624837e-02,2.782382e-02,2.820741e-02,2.905678e-02,2.886499e-02,2.854990e-02,2.902939e-02,2.733064e-02,2.742654e-02,2.745394e-02,2.719364e-02,2.468662e-02,2.374135e-02,2.179601e-02,1.998767e-02,1.775464e-02,1.637098e-02,1.468594e-02,1.219262e-02,1.021988e-02,7.877252e-03,6.877183e-03,5.096239e-03,4.548257e-03,3.397493e-03,2.753613e-03,2.027536e-03,2.068635e-03,1.315159e-03,9.178711e-04,1.027468e-03,6.986780e-04,8.219741e-04,4.520858e-04,3.561888e-04,3.972875e-04,2.602918e-04,2.191931e-04,3.013905e-04,2.328927e-04,2.465922e-04,1.643948e-04,1.095965e-04,1.506953e-04,1.369957e-04,5.479827e-05,1.643948e-04,1.095965e-04,1.095965e-04,9.589698e-05,2.739914e-05,1.369957e-04,1.369957e-05,6.849784e-05,2.739914e-05,1.232961e-04,5.479827e-05,4.109871e-05,6.849784e-05,2.739914e-05,5.479827e-05,8.219741e-05,8.219741e-05,4.109871e-05,1.369957e-05,1.369957e-05,2.739914e-05,4.109871e-05,1.369957e-05,2.739914e-05,0.000000e+00,1.369957e-05,1.369957e-05,2.739914e-05,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,1.369957e-05,1.369957e-05,5.479827e-05,4.109871e-05,0.000000e+00,1.369957e-05,2.739914e-05,4.109871e-05,0.000000e+00,0.000000e+00,2.739914e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[1].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [2.876909e-04,1.232961e-04,1.780944e-04,2.054935e-04,1.506953e-04,3.561888e-04,1.095965e-04,2.876909e-04,1.095965e-04,2.739914e-04,2.328927e-04,2.465922e-04,2.191931e-04,3.287896e-04,2.876909e-04,2.876909e-04,3.561888e-04,1.917940e-04,5.342832e-04,3.561888e-04,4.657853e-04,3.561888e-04,3.424892e-04,4.520858e-04,6.027810e-04,5.205836e-04,5.342832e-04,7.534763e-04,7.671758e-04,7.671758e-04,7.808754e-04,8.493732e-04,7.945750e-04,7.808754e-04,5.616823e-04,9.863689e-04,8.493732e-04,1.000068e-03,1.438455e-03,1.383656e-03,1.082266e-03,1.219262e-03,8.904720e-04,1.411056e-03,1.753545e-03,1.822043e-03,1.589150e-03,1.548051e-03,1.835742e-03,2.465922e-03,1.945339e-03,1.822043e-03,2.411124e-03,2.918008e-03,2.356326e-03,2.644017e-03,3.753682e-03,2.657716e-03,3.548188e-03,3.835879e-03,3.452291e-03,4.082471e-03,3.835879e-03,4.589355e-03,4.890746e-03,4.438660e-03,6.315501e-03,5.438729e-03,6.055209e-03,7.507364e-03,6.712789e-03,7.384067e-03,7.123776e-03,7.781355e-03,8.712926e-03,9.178711e-03,9.754093e-03,1.067196e-02,1.141174e-02,1.209672e-02,1.198712e-02,1.417905e-02,1.393246e-02,1.554901e-02,1.598740e-02,1.546681e-02,1.838482e-02,1.946709e-02,2.054935e-02,2.082334e-02,2.190561e-02,2.250839e-02,2.254949e-02,2.333037e-02,2.519351e-02,2.624837e-02,2.782382e-02,2.820741e-02,2.905678e-02,2.886499e-02,2.854990e-02,2.902939e-02,2.733064e-02,2.742654e-02,2.745394e-02,2.719364e-02,2.468662e-02,2.374135e-02,2.179601e-02,1.998767e-02,1.775464e-02,1.637098e-02,1.468594e-02,1.219262e-02,1.021988e-02,7.877252e-03,6.877183e-03,5.096239e-03,4.548257e-03,3.397493e-03,2.753613e-03,2.027536e-03,2.068635e-03,1.315159e-03,9.178711e-04,1.027468e-03,6.986780e-04,8.219741e-04,4.520858e-04,3.561888e-04,3.972875e-04,2.602918e-04,2.191931e-04,3.013905e-04,2.328927e-04,2.465922e-04,1.643948e-04,1.095965e-04,1.506953e-04,1.369957e-04,5.479827e-05,1.643948e-04,1.095965e-04,1.095965e-04,9.589698e-05,2.739914e-05,1.369957e-04,1.369957e-05,6.849784e-05,2.739914e-05,1.232961e-04,5.479827e-05,4.109871e-05,6.849784e-05,2.739914e-05,5.479827e-05,8.219741e-05,8.219741e-05,4.109871e-05,1.369957e-05,1.369957e-05,2.739914e-05,4.109871e-05,1.369957e-05,2.739914e-05,0.000000e+00,1.369957e-05,1.369957e-05,2.739914e-05,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,1.369957e-05,1.369957e-05,5.479827e-05,4.109871e-05,0.000000e+00,1.369957e-05,2.739914e-05,4.109871e-05,0.000000e+00,0.000000e+00,2.739914e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[2].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [2.876909e-04,1.232961e-04,1.780944e-04,2.054935e-04,1.506953e-04,3.561888e-04,1.095965e-04,2.876909e-04,1.095965e-04,2.739914e-04,2.328927e-04,2.465922e-04,2.191931e-04,3.287896e-04,2.876909e-04,2.876909e-04,3.561888e-04,1.917940e-04,5.342832e-04,3.561888e-04,4.657853e-04,3.561888e-04,3.424892e-04,4.520858e-04,6.027810e-04,5.205836e-04,5.342832e-04,7.534763e-04,7.671758e-04,7.671758e-04,7.808754e-04,8.493732e-04,7.945750e-04,7.808754e-04,5.616823e-04,9.863689e-04,8.493732e-04,1.000068e-03,1.438455e-03,1.383656e-03,1.082266e-03,1.219262e-03,8.904720e-04,1.411056e-03,1.753545e-03,1.822043e-03,1.589150e-03,1.548051e-03,1.835742e-03,2.465922e-03,1.945339e-03,1.822043e-03,2.411124e-03,2.918008e-03,2.356326e-03,2.644017e-03,3.753682e-03,2.657716e-03,3.548188e-03,3.835879e-03,3.452291e-03,4.082471e-03,3.835879e-03,4.589355e-03,4.890746e-03,4.438660e-03,6.315501e-03,5.438729e-03,6.055209e-03,7.507364e-03,6.712789e-03,7.384067e-03,7.123776e-03,7.781355e-03,8.712926e-03,9.178711e-03,9.754093e-03,1.067196e-02,1.141174e-02,1.209672e-02,1.198712e-02,1.417905e-02,1.393246e-02,1.554901e-02,1.598740e-02,1.546681e-02,1.838482e-02,1.946709e-02,2.054935e-02,2.082334e-02,2.190561e-02,2.250839e-02,2.254949e-02,2.333037e-02,2.519351e-02,2.624837e-02,2.782382e-02,2.820741e-02,2.905678e-02,2.886499e-02,2.854990e-02,2.902939e-02,2.733064e-02,2.742654e-02,2.745394e-02,2.719364e-02,2.468662e-02,2.374135e-02,2.179601e-02,1.998767e-02,1.775464e-02,1.637098e-02,1.468594e-02,1.219262e-02,1.021988e-02,7.877252e-03,6.877183e-03,5.096239e-03,4.548257e-03,3.397493e-03,2.753613e-03,2.027536e-03,2.068635e-03,1.315159e-03,9.178711e-04,1.027468e-03,6.986780e-04,8.219741e-04,4.520858e-04,3.561888e-04,3.972875e-04,2.602918e-04,2.191931e-04,3.013905e-04,2.328927e-04,2.465922e-04,1.643948e-04,1.095965e-04,1.506953e-04,1.369957e-04,5.479827e-05,1.643948e-04,1.095965e-04,1.095965e-04,9.589698e-05,2.739914e-05,1.369957e-04,1.369957e-05,6.849784e-05,2.739914e-05,1.232961e-04,5.479827e-05,4.109871e-05,6.849784e-05,2.739914e-05,5.479827e-05,8.219741e-05,8.219741e-05,4.109871e-05,1.369957e-05,1.369957e-05,2.739914e-05,4.109871e-05,1.369957e-05,2.739914e-05,0.000000e+00,1.369957e-05,1.369957e-05,2.739914e-05,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,1.369957e-05,1.369957e-05,5.479827e-05,4.109871e-05,0.000000e+00,1.369957e-05,2.739914e-05,4.109871e-05,0.000000e+00,0.000000e+00,2.739914e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[3].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [1.091493e-06,0.000000e+00,5.457467e-07,0.000000e+00,0.000000e+00,9.274939e-06,0.000000e+00,0.000000e+00,0.000000e+00,9.274939e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,5.457467e-07,0.000000e+00,9.274939e-06,9.274939e-06,0.000000e+00,0.000000e+00,5.457467e-07,9.274939e-06,9.274939e-06,9.274939e-06,5.457467e-07,0.000000e+00,9.274939e-06,0.000000e+00,1.091493e-06,0.000000e+00,9.274939e-06,9.274939e-06,0.000000e+00,0.000000e+00,0.000000e+00,1.909563e-05,0.000000e+00,9.274939e-06,1.909563e-05,0.000000e+00,1.854988e-05,9.274939e-06,1.091493e-06,1.091218e-05,9.274939e-06,1.964137e-05,0.000000e+00,2.891631e-05,5.457467e-07,5.457467e-07,1.091493e-06,2.782482e-05,2.837056e-05,1.909563e-05,5.564964e-05,2.782482e-05,2.891631e-05,2.891631e-05,2.891631e-05,9.820686e-06,3.709976e-05,1.854988e-05,3.055355e-05,2.946206e-05,3.055355e-05,1.145793e-05,4.910343e-05,3.055355e-05,2.946206e-05,4.964918e-05,4.801194e-05,1.909563e-05,6.710756e-05,6.819905e-05,6.601607e-05,4.091998e-05,1.216657e-04,6.601607e-05,8.511169e-05,1.151195e-04,1.140280e-04,1.162110e-04,1.145738e-04,1.063903e-04,1.238487e-04,1.985940e-04,1.091190e-04,9.438663e-05,1.805898e-04,1.702234e-04,1.233029e-04,2.165981e-04,1.636772e-04,2.100519e-04,2.935263e-04,2.547893e-04,3.044385e-04,3.011640e-04,2.198726e-04,3.710003e-04,3.273516e-04,3.759093e-04,3.393553e-04,4.784794e-04,5.346747e-04,4.315589e-04,5.161249e-04,6.323359e-04,7.441781e-04,6.628867e-04,7.463611e-04,1.097720e-03,1.036067e-03,1.137000e-03,1.451802e-03,1.526002e-03,1.744783e-03,2.147968e-03,2.458953e-03,2.725198e-03,3.070553e-03,3.074374e-03,3.864378e-03,4.594918e-03,4.905903e-03,5.690452e-03,5.848672e-03,6.396442e-03,7.589089e-03,8.033743e-03,8.544410e-03,9.090000e-03,1.071912e-02,1.037486e-02,1.090026e-02,1.163572e-02,1.290203e-02,1.307172e-02,1.420163e-02,1.538993e-02,1.513133e-02,1.668735e-02,1.873440e-02,2.016440e-02,2.075581e-02,2.194083e-02,2.338882e-02,2.556080e-02,2.622752e-02,2.675565e-02,2.758277e-02,2.826203e-02,2.801652e-02,2.778467e-02,2.787745e-02,2.820536e-02,2.923327e-02,2.811596e-02,2.796267e-02,2.801127e-02,2.562434e-02,2.599483e-02,2.467945e-02,2.306837e-02,2.105625e-02,1.945061e-02,1.780733e-02,1.647554e-02,1.506031e-02,1.325169e-02,1.177862e-02,1.025479e-02,9.065946e-03,8.013498e-03,6.780460e-03,6.659858e-03,5.807093e-03,4.831554e-03,4.453966e-03,4.006010e-03,3.663342e-03,3.284133e-03,2.738508e-03,2.399130e-03,2.111040e-03,1.880235e-03,1.866573e-03,1.521200e-03,1.514640e-03,1.295843e-03,1.213446e-03,1.029030e-03,8.664419e-04,8.413376e-04,8.358746e-04,5.712673e-04,6.760149e-04,6.012641e-04,3.666591e-04,4.495851e-04,4.288495e-04,4.152113e-04,2.886284e-04,3.459180e-04,2.417052e-04,3.033580e-04,2.286100e-04,1.500445e-04,1.271287e-04,1.134878e-04,5.020043e-05,1.538620e-04,8.893468e-05,6.602158e-05,7.202204e-05,4.310573e-05,2.564459e-05,5.292366e-05,4.474021e-05,6.110710e-05,3.219079e-05,2.182436e-05,1.145793e-05,2.018712e-05,2.728734e-06,2.073287e-05,1.200367e-05,1.091493e-06,2.182987e-06,2.182987e-06,1.091493e-06,2.182987e-06,5.457467e-07,5.457467e-07,5.457467e-07,9.274939e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])


plt.savefig("/root/output/cytometry_plot_$1_S3_SrpR.png", bbox_inches='tight')
