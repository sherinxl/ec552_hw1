import matplotlib.pyplot as plt
import numpy as np

num_plots = 4

fig, ax = plt.subplots(num_plots, 1, sharex=True, sharey=True)
fig.set_size_inches(4, 1*num_plots)

fig.suptitle("$1 / P3_PhlF")

for a in ax:
    a.set_xscale('log')
    a.set_yscale('log')
    a.set_xlim(1.000000e-03, 1.000000e+02)

ax[0].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [3.699484e-04,3.255546e-04,2.663628e-04,2.071711e-04,3.255546e-04,4.735339e-04,1.923731e-04,6.215132e-04,2.663628e-04,4.735339e-04,7.103008e-04,4.587360e-04,3.995442e-04,5.179277e-04,4.291401e-04,4.143422e-04,6.067153e-04,4.587360e-04,4.883318e-04,5.327256e-04,4.735339e-04,4.883318e-04,5.179277e-04,5.475236e-04,5.623215e-04,9.618657e-04,8.434822e-04,1.154239e-03,1.405804e-03,1.479793e-03,1.361410e-03,1.435400e-03,1.065451e-03,7.250988e-04,8.138864e-04,1.346612e-03,1.598177e-03,1.953327e-03,2.116105e-03,2.397265e-03,1.642571e-03,1.894136e-03,1.923731e-03,2.175296e-03,3.151960e-03,2.811607e-03,2.397265e-03,2.130903e-03,3.018779e-03,3.921453e-03,3.344333e-03,2.959587e-03,3.877059e-03,4.661349e-03,3.240748e-03,4.528168e-03,5.356852e-03,3.921453e-03,5.682407e-03,5.312458e-03,5.859982e-03,6.895837e-03,6.141143e-03,7.295382e-03,7.680128e-03,7.946491e-03,9.293103e-03,7.265786e-03,8.923154e-03,1.040295e-02,1.058052e-02,1.043254e-02,1.137961e-02,1.220830e-02,1.263744e-02,1.340693e-02,1.420602e-02,1.530106e-02,1.604096e-02,1.612975e-02,1.666247e-02,1.945928e-02,1.820146e-02,1.932610e-02,2.166418e-02,2.139781e-02,2.272963e-02,2.312917e-02,2.496412e-02,2.426861e-02,2.460896e-02,2.687305e-02,2.638472e-02,2.740577e-02,2.838244e-02,2.697663e-02,2.725779e-02,2.835284e-02,2.537846e-02,2.583719e-02,2.407624e-02,2.380988e-02,2.240407e-02,2.025837e-02,1.866020e-02,1.581899e-02,1.376208e-02,1.203072e-02,1.099487e-02,8.819569e-03,7.472957e-03,6.081951e-03,4.720541e-03,3.729079e-03,2.856001e-03,2.086509e-03,1.583379e-03,1.361410e-03,9.766637e-04,9.322699e-04,9.766637e-04,9.322699e-04,5.327256e-04,5.771194e-04,5.919174e-04,3.847463e-04,3.403525e-04,3.699484e-04,3.107566e-04,3.551504e-04,2.515649e-04,1.775752e-04,1.923731e-04,1.923731e-04,1.775752e-04,1.035855e-04,2.219690e-04,1.923731e-04,8.878761e-05,7.398967e-05,1.183835e-04,1.331814e-04,1.183835e-04,1.035855e-04,1.331814e-04,7.398967e-05,1.479793e-05,5.919174e-05,4.439380e-05,2.959587e-05,5.919174e-05,4.439380e-05,0.000000e+00,2.959587e-05,5.919174e-05,4.439380e-05,4.439380e-05,7.398967e-05,2.959587e-05,1.479793e-05,0.000000e+00,2.959587e-05,1.479793e-05,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,4.439380e-05,0.000000e+00,0.000000e+00,4.439380e-05,1.479793e-05,0.000000e+00,1.479793e-05,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[1].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [3.699484e-04,3.255546e-04,2.663628e-04,2.071711e-04,3.255546e-04,4.735339e-04,1.923731e-04,6.215132e-04,2.663628e-04,4.735339e-04,7.103008e-04,4.587360e-04,3.995442e-04,5.179277e-04,4.291401e-04,4.143422e-04,6.067153e-04,4.587360e-04,4.883318e-04,5.327256e-04,4.735339e-04,4.883318e-04,5.179277e-04,5.475236e-04,5.623215e-04,9.618657e-04,8.434822e-04,1.154239e-03,1.405804e-03,1.479793e-03,1.361410e-03,1.435400e-03,1.065451e-03,7.250988e-04,8.138864e-04,1.346612e-03,1.598177e-03,1.953327e-03,2.116105e-03,2.397265e-03,1.642571e-03,1.894136e-03,1.923731e-03,2.175296e-03,3.151960e-03,2.811607e-03,2.397265e-03,2.130903e-03,3.018779e-03,3.921453e-03,3.344333e-03,2.959587e-03,3.877059e-03,4.661349e-03,3.240748e-03,4.528168e-03,5.356852e-03,3.921453e-03,5.682407e-03,5.312458e-03,5.859982e-03,6.895837e-03,6.141143e-03,7.295382e-03,7.680128e-03,7.946491e-03,9.293103e-03,7.265786e-03,8.923154e-03,1.040295e-02,1.058052e-02,1.043254e-02,1.137961e-02,1.220830e-02,1.263744e-02,1.340693e-02,1.420602e-02,1.530106e-02,1.604096e-02,1.612975e-02,1.666247e-02,1.945928e-02,1.820146e-02,1.932610e-02,2.166418e-02,2.139781e-02,2.272963e-02,2.312917e-02,2.496412e-02,2.426861e-02,2.460896e-02,2.687305e-02,2.638472e-02,2.740577e-02,2.838244e-02,2.697663e-02,2.725779e-02,2.835284e-02,2.537846e-02,2.583719e-02,2.407624e-02,2.380988e-02,2.240407e-02,2.025837e-02,1.866020e-02,1.581899e-02,1.376208e-02,1.203072e-02,1.099487e-02,8.819569e-03,7.472957e-03,6.081951e-03,4.720541e-03,3.729079e-03,2.856001e-03,2.086509e-03,1.583379e-03,1.361410e-03,9.766637e-04,9.322699e-04,9.766637e-04,9.322699e-04,5.327256e-04,5.771194e-04,5.919174e-04,3.847463e-04,3.403525e-04,3.699484e-04,3.107566e-04,3.551504e-04,2.515649e-04,1.775752e-04,1.923731e-04,1.923731e-04,1.775752e-04,1.035855e-04,2.219690e-04,1.923731e-04,8.878761e-05,7.398967e-05,1.183835e-04,1.331814e-04,1.183835e-04,1.035855e-04,1.331814e-04,7.398967e-05,1.479793e-05,5.919174e-05,4.439380e-05,2.959587e-05,5.919174e-05,4.439380e-05,0.000000e+00,2.959587e-05,5.919174e-05,4.439380e-05,4.439380e-05,7.398967e-05,2.959587e-05,1.479793e-05,0.000000e+00,2.959587e-05,1.479793e-05,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,4.439380e-05,0.000000e+00,0.000000e+00,4.439380e-05,1.479793e-05,0.000000e+00,1.479793e-05,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[2].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [3.699484e-04,3.255546e-04,2.663628e-04,2.071711e-04,3.255546e-04,4.735339e-04,1.923731e-04,6.215132e-04,2.663628e-04,4.735339e-04,7.103008e-04,4.587360e-04,3.995442e-04,5.179277e-04,4.291401e-04,4.143422e-04,6.067153e-04,4.587360e-04,4.883318e-04,5.327256e-04,4.735339e-04,4.883318e-04,5.179277e-04,5.475236e-04,5.623215e-04,9.618657e-04,8.434822e-04,1.154239e-03,1.405804e-03,1.479793e-03,1.361410e-03,1.435400e-03,1.065451e-03,7.250988e-04,8.138864e-04,1.346612e-03,1.598177e-03,1.953327e-03,2.116105e-03,2.397265e-03,1.642571e-03,1.894136e-03,1.923731e-03,2.175296e-03,3.151960e-03,2.811607e-03,2.397265e-03,2.130903e-03,3.018779e-03,3.921453e-03,3.344333e-03,2.959587e-03,3.877059e-03,4.661349e-03,3.240748e-03,4.528168e-03,5.356852e-03,3.921453e-03,5.682407e-03,5.312458e-03,5.859982e-03,6.895837e-03,6.141143e-03,7.295382e-03,7.680128e-03,7.946491e-03,9.293103e-03,7.265786e-03,8.923154e-03,1.040295e-02,1.058052e-02,1.043254e-02,1.137961e-02,1.220830e-02,1.263744e-02,1.340693e-02,1.420602e-02,1.530106e-02,1.604096e-02,1.612975e-02,1.666247e-02,1.945928e-02,1.820146e-02,1.932610e-02,2.166418e-02,2.139781e-02,2.272963e-02,2.312917e-02,2.496412e-02,2.426861e-02,2.460896e-02,2.687305e-02,2.638472e-02,2.740577e-02,2.838244e-02,2.697663e-02,2.725779e-02,2.835284e-02,2.537846e-02,2.583719e-02,2.407624e-02,2.380988e-02,2.240407e-02,2.025837e-02,1.866020e-02,1.581899e-02,1.376208e-02,1.203072e-02,1.099487e-02,8.819569e-03,7.472957e-03,6.081951e-03,4.720541e-03,3.729079e-03,2.856001e-03,2.086509e-03,1.583379e-03,1.361410e-03,9.766637e-04,9.322699e-04,9.766637e-04,9.322699e-04,5.327256e-04,5.771194e-04,5.919174e-04,3.847463e-04,3.403525e-04,3.699484e-04,3.107566e-04,3.551504e-04,2.515649e-04,1.775752e-04,1.923731e-04,1.923731e-04,1.775752e-04,1.035855e-04,2.219690e-04,1.923731e-04,8.878761e-05,7.398967e-05,1.183835e-04,1.331814e-04,1.183835e-04,1.035855e-04,1.331814e-04,7.398967e-05,1.479793e-05,5.919174e-05,4.439380e-05,2.959587e-05,5.919174e-05,4.439380e-05,0.000000e+00,2.959587e-05,5.919174e-05,4.439380e-05,4.439380e-05,7.398967e-05,2.959587e-05,1.479793e-05,0.000000e+00,2.959587e-05,1.479793e-05,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,4.439380e-05,0.000000e+00,0.000000e+00,4.439380e-05,1.479793e-05,0.000000e+00,1.479793e-05,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[3].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,6.895063e-06,0.000000e+00,0.000000e+00,0.000000e+00,6.895063e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.822269e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,6.895063e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,6.895063e-06,6.895063e-06,0.000000e+00,2.927206e-06,0.000000e+00,0.000000e+00,2.927206e-06,0.000000e+00,6.895063e-06,0.000000e+00,1.379013e-05,6.895063e-06,2.927206e-06,1.964454e-05,5.854412e-06,0.000000e+00,2.927206e-06,9.822269e-06,8.781618e-06,2.927206e-06,5.854412e-06,2.653960e-05,2.361239e-05,2.068519e-05,0.000000e+00,1.379013e-05,1.379013e-05,9.822269e-06,2.068519e-05,2.653960e-05,1.671733e-05,1.170882e-05,2.653960e-05,2.549895e-05,1.860389e-05,5.854412e-06,3.740252e-05,3.928907e-05,2.653960e-05,3.928907e-05,4.117563e-05,2.549895e-05,3.239401e-05,5.997426e-05,5.203855e-05,4.911134e-05,4.514349e-05,3.824842e-05,2.445830e-05,4.117563e-05,2.549895e-05,2.361239e-05,4.911134e-05,4.703004e-05,8.358666e-05,1.042718e-04,6.270672e-05,1.120128e-04,6.875588e-05,3.928907e-05,8.254601e-05,6.875588e-05,9.737678e-05,1.138994e-04,7.753750e-05,9.236827e-05,1.256082e-04,6.979653e-05,8.944107e-05,5.600641e-05,1.130535e-04,5.496576e-05,1.011499e-04,7.857815e-05,4.911134e-05,2.842616e-05,8.651386e-05,1.180620e-04,4.032972e-05,4.032972e-05,3.239401e-05,5.997426e-05,4.722479e-05,2.946681e-05,1.671733e-05,9.822269e-06,4.514349e-05,3.636187e-05,2.927206e-06,2.927206e-06,2.068519e-05,2.068519e-05,5.854412e-06,1.671733e-05,0.000000e+00,3.636187e-05,2.653960e-05,1.860389e-05,1.567668e-05,1.567668e-05,2.549895e-05,5.600641e-05,4.410284e-05,1.860389e-05,3.909433e-05,3.428057e-05,3.909433e-05,8.508372e-05,5.769822e-05,1.034929e-04,1.661996e-04,2.082211e-04,1.816815e-04,2.138808e-04,2.577889e-04,4.100036e-04,4.873464e-04,5.929205e-04,6.698738e-04,8.550668e-04,1.104007e-03,1.146680e-03,1.623486e-03,1.890835e-03,2.296153e-03,2.777055e-03,3.274935e-03,4.044133e-03,4.480737e-03,5.965397e-03,6.850381e-03,8.321129e-03,9.858941e-03,1.111691e-02,1.368736e-02,1.541355e-02,1.807481e-02,2.105747e-02,2.352728e-02,2.727542e-02,3.112881e-02,3.431935e-02,3.723440e-02,4.035839e-02,4.326602e-02,4.645726e-02,4.804720e-02,4.885118e-02,4.910184e-02,4.722208e-02,4.533007e-02,4.193683e-02,3.913163e-02,3.554285e-02,3.120974e-02,2.781450e-02,2.395039e-02,2.098206e-02,1.748339e-02,1.469023e-02,1.242084e-02,9.813262e-03,8.637980e-03,7.532421e-03,6.252604e-03,5.349479e-03,4.785185e-03,3.562416e-03,3.624405e-03,2.840254e-03,2.640425e-03,2.159007e-03,1.791420e-03,1.784330e-03,1.270712e-03,1.134046e-03,1.014098e-03,8.465347e-04,8.810100e-04,7.431088e-04,6.785155e-04,5.888797e-04,5.792522e-04,5.184320e-04,3.776036e-04,2.942116e-04,3.245244e-04,2.852353e-04,1.751090e-04,1.682140e-04,1.138994e-04,1.042718e-04,1.191026e-04,1.151348e-04,1.042718e-04,9.340892e-05,8.065945e-05,5.411985e-05,2.361239e-05,2.068519e-05,2.758025e-05,0.000000e+00,0.000000e+00,1.671733e-05,9.822269e-06,0.000000e+00,2.068519e-05,2.927206e-06,6.895063e-06,0.000000e+00,0.000000e+00,6.895063e-06,0.000000e+00,0.000000e+00,6.895063e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])


plt.savefig("/root/output/cytometry_plot_$1_P3_PhlF.png", bbox_inches='tight')