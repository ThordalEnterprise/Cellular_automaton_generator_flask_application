import matplotlib as mpl
import matplotlib.pyplot as plt

def plot_all_cmaps():
    N_ROWS, N_COLS = 8, 7 # 13, 13 <-- for all in one figure 
    HEIGHT, WIDTH = 7, 14

    cmap_ids = plt.colormaps()
    n_cmaps = len(cmap_ids)
    
    print(f'mpl version: {mpl.__version__},\nnumber of cmaps: {n_cmaps}')
    
    index = 0
    while index < n_cmaps:
        fig, axes = plt.subplots(N_ROWS, N_COLS, figsize=(WIDTH, HEIGHT))
        for row in range(N_ROWS):
            for col in range(N_COLS):
                ax = axes[row, col]
                cmap_id = cmap_ids[index]
                cmap = plt.get_cmap(cmap_id)
                mpl.colorbar.ColorbarBase(ax, cmap=cmap,
                                          orientation='horizontal')
                ax.set_title(f"'{cmap_id}', {index}", fontsize=8)
                ax.tick_params(left=False, right=False, labelleft=False,
                               labelbottom=False, bottom=False)
                
                last_iteration = index == n_cmaps-1
                if (row==N_ROWS-1 and col==N_COLS-1) or last_iteration:
                    plt.tight_layout()
                    #plt.savefig('colormaps'+str(index)+'.png')
                    plt.show()
                    if last_iteration: return
                index += 1

plot_all_cmaps()