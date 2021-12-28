# %%
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt

def plot_distances(z_array, rz_array, trz_array, DLz_array, DAz_array):
        
        width = st.slider("plot width", 1, 25, 10)
        height = st.slider("plot height", 1, 25, 5)
        
        fig, ax = plt.subplots(figsize=(width, height))
        a
        colors = {
         'orange' : '#ffc345',
         'gray' : '#333333',
         'white' : '#FFFFFF',
        }
        
        ax.spines['bottom'].set_color(colors['orange'])
        ax.spines['top'].set_color(colors['orange']) 
        ax.spines['right'].set_color(colors['orange'])
        ax.spines['left'].set_color(colors['orange'])

        ax.tick_params(axis='x', colors=colors['orange'])
        ax.tick_params(axis='y', colors=colors['orange'])

        ax.yaxis.label.set_color(colors['orange'])
        ax.xaxis.label.set_color(colors['orange'])
        
        for axis in ['top','bottom','left','right']:
            ax.spines[axis].set_linewidth(3)

        ax.tick_params(width=3)
        ax.tick_params(axis='both', labelsize=12)

        ax.set_facecolor(colors['white'])
        fig.patch.set_facecolor(colors['white'])
   
        if plot_rz:
            ax.plot(z_array, rz_array, label='Comoving Distance', color=colors['gray'], ls='-', lw=3)
        if plot_trz:
            ax.plot(z_array, trz_array, label='Transverse Comoving Distance', color=colors['gray'], ls='-.', lw=3)
        if plot_DLz:
            ax.plot(z_array, DLz_array, label='Luminosity Distance', color=colors['gray'], ls='--', lw=3)
        if plot_DAz:
            ax.plot(z_array, DAz_array, label='Angular Diameter Distance', color=colors['gray'], ls=':', lw=3)
        

        legend = plt.legend(frameon = 1)
        plt.setp(legend.get_texts(), color=colors['gray'])
        frame = legend.get_frame()
        frame.set_facecolor(colors['white'])
        frame.set_edgecolor(colors['white'])

        ax.set_xlabel('Redshift', size=15)
        ax.set_ylabel('Distance [Mpc]', size=15)

        myplot = st.pyplot(fig)
        
        return myplot
        