import os
import pandas as pd
import matplotlib.pyplot as plt

paths = ['denoising', 'deblurring_1_6', 'deblurring_0_4', 'deblurring_0_4_high_noise']
titles = ['Denoising ($\sigma_{noise}=0.05$)', 'Deblurring ($\sigma_{blur}=1.6$, $\sigma_{noise}=0.0078$)', 'Deblurring ($\sigma_{blur}=0.4$, $\sigma_{noise}=0.0078$)', 'Deblurring ($\sigma_{blur}=0.4$, $\sigma_{noise}=0.0314$)']
ylims = [(None, None), (15., None), (17.5, None), (22.5, None)]

def load_psnrs(path, filepath):
    psnrs = pd.read_csv(os.path.join(path, filepath))
    return psnrs['Step'].to_numpy(), psnrs['Value'].to_numpy()

fig, axs = plt.subplots(2, 2, figsize=(16, 8), gridspec_kw={'wspace': 0.1})

for i, (ax, path, title, ylim) in enumerate(zip(axs.T.flat, paths, titles, ylims)):
    dip_steps, dip_psnrs = load_psnrs(path, 'dip.csv')
    dip_sure_steps, dip_sure_psnrs = load_psnrs(path, 'dip_sure.csv')

    ax.plot(dip_steps, dip_psnrs, label='DIP', color='blue')
    ax.plot(dip_sure_steps, dip_sure_psnrs, label='SURE DIP', color='orange')
    if i in [0, 2]:
        ax.get_xaxis().set_ticklabels([])
    if i in [1, 3]:
        ax.set_xlabel('Iteration')
    if i in [0, 1]:
        ax.set_ylabel('PSNR [dB]')
    ax.set_title(title)
    ax.set_ylim(ylim)
    ax.grid(ls='--')

axs.flatten()[0].legend()

fig.savefig('plot_sure_vs_dip.png', bbox_inches='tight', pad_inches=0.)
