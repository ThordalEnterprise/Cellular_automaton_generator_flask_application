# import libraries
import time, random, warnings, os, matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
warnings.filterwarnings("ignore")
from flask import Flask, render_template, request
import shutil

app = Flask(__name__)
matplotlib.pyplot.switch_backend('Agg')
img = os.path.join('static', 'images')
img_out = os.path.join('static', 'output')
img1 = os.path.join(img, '1.gif')
img2 = os.path.join(img, '2.gif')
img3 = os.path.join(img, '3.gif')
img4 = os.path.join(img, '4.gif')
img5 = os.path.join(img, '5.gif')
img6 = os.path.join(img, '6.gif')
img7 = os.path.join(img, '7.gif')
img8 = os.path.join(img, '8.gif')
img9 = os.path.join(img, '9.gif')
img10 = os.path.join(img, '10.gif')
img11 = os.path.join(img, '11.gif')
img12 = os.path.join(img, '12.gif')
img13 = os.path.join(img, '13.gif')
img14 = os.path.join(img, '14.gif')
img15 = os.path.join(img, '15.gif')
img16 = os.path.join(img, '16.gif')
out_file = os.path.join(img_out, 'output.gif')
img17 = os.path.join(img, 'Figure_1.png')
img18 = os.path.join(img, 'Figure_2.png')
img19 = os.path.join(img, 'Figure_3.png')


@app.route('/')
def index():
    filename = "output.gif"
    folder = "static/output"
    file_path = os.path.join(folder, filename)
    if os.path.exists(file_path):
        path = "static/output/output.gif"
    else:
        path = "static/output/placeholder-image.png"
    return render_template('index.html',img19=img19,img18=img18,img17=img17,img_output=path, img1=img1,img2=img2,img3=img3,img4=img4,img5=img5,img6=img6,img7=img7,img8=img8,img9=img9,img10=img10,img11=img11,img12=img12,img13=img13,img14=img14,img15=img15,img16=img16)

@app.route('/Generator', methods=['GET', 'POST'])
def Generator():
    id = request.args.get('ID')
    xy = id.split("*")
    user_rule = xy[0]
    user_Initcond_Phrase = xy[1]
    user_Impulse_Position = xy[2]
    user_selectedValue = xy[3]
    x_count = 0
    while x_count < 1:
        try:
            powers_of_two = np.array([[4], [2], [1]])  # shape (3, 1)
            x_count = 0
            def step(x, rule_binary):
                x_shift_right = np.roll(x,  1)  # circular shift to right <3 kan edits
                x_shift_left = np.roll(x, -1)  # circular shift to left <3 kan edits
                y = np.vstack((x_shift_right, x, x_shift_left)).astype(np.int8)  # stack row-wise, shape (3, cols)
                z = np.sum(powers_of_two * y, axis=0).astype(np.int8)  # LCR pattern as number
                return rule_binary[7 - z]

            def cellular_automaton(rule_number, size, steps, init_cond='random', impulse_pos='center'):
                assert 1 <= rule_number <= 256
                assert init_cond in ['random', 'impulse']
                assert impulse_pos in ['left', 'center', 'right']
                rule_binary_str = np.binary_repr(rule_number, width=8)
                rule_binary = np.array([int(ch) for ch in rule_binary_str], dtype=np.int8)
                x = np.zeros((steps, size), dtype=np.int8)
                if init_cond == 'random':  # random init of the first step
                    x[0, :] = np.array(np.random.rand(size) < 0.5, dtype=np.int8)
                if init_cond == 'impulse':  # starting with an initial impulse
                    if impulse_pos == 'left':
                        x[0, 0] = 1
                    elif impulse_pos == 'right':
                        x[0, size - 1] = 1
                    else:
                        x[0, size // 2] = 1
                for i in range(steps - 1):
                    x[i + 1, :] = step(x[i, :], rule_binary)
                return x


            rule_number = int(user_rule) # select the update rule <3
            size = 100  # number of cells in one row -- <3 Brede
            steps = 400 # number of time steps --  <3 Length
            init_cond=str(user_Initcond_Phrase)  # start with only one cell  <3  ['random', 'impulse']
            impulse_pos=str(user_Impulse_Position)  # start with the central cell <3 -- left - right - center
            x = cellular_automaton(rule_number, size, steps, init_cond, impulse_pos)
            steps_to_show = 100  # number of steps to show in the animation window <3 Skala
            iterations_per_frame = 3  # how many steps to show per frame - <3 Speed
            frames = int(steps // iterations_per_frame)  # number of frames in the animation
            interval=50  # interval in ms between consecutive frames -- <3 Speed
            collection = "Cellular Automata -"
            rand_x = random.randint(0,163)
            skinz = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']
            color_skinz=str(user_selectedValue)
            fig = plt.figure(figsize=(10, 10))
            plt.gcf().text(0.2, 0.05, 'From jtj.pythonanywhere.com'+' --- Rule #'+str(rule_number)+' - Color #'+str(color_skinz), fontsize=12, fontfamily='Verdana')
            ax = plt.axes()
            ax.set_axis_off()

            def animate(i):
                ax.clear()  # clear the plot
                ax.set_axis_off()
                Y = np.zeros((steps_to_show, size), dtype=np.int8)  # initialize with all zeros
                upper_boundary = (i + 1) * iterations_per_frame  # window upper boundary
                lower_boundary = 0 if upper_boundary <= steps_to_show else upper_boundary - steps_to_show  # window lower bound.
                print("Working #"+str(x_count))
                for t in range(lower_boundary, upper_boundary):  # assign the values
                    Y[t - lower_boundary, :] = x[t, :]
                #img = ax.imshow(Y, interpolation='none',cmap='RdPu')
                img = ax.imshow(Y, interpolation='none',cmap=color_skinz)
                #plt.gcf().text(0.15, 0.1, 'From Cellular-automation-generator.com', fontsize=14, fontfamily='Verdana')
                return [img]

            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            # call the animator
            file = open("REC.txt",'a')
            file.writelines(str(collection)+str(x_count)+' - Rule #'+str(rule_number)+' - Skin #'+str(color_skinz)+" - \n")
            file.close()
            #os.chdir("static/output")
            anim = animation.FuncAnimation(fig, animate, frames=frames, interval=interval, blit=True)
            anim.save("output.gif", writer='Pillow')
            original_folder = os.getcwd()
            destination_folder = 'static/output'
            file_name = 'output.gif'

            if os.path.isfile(original_folder + '/' + file_name):
                shutil.move(original_folder + '/' + file_name, destination_folder + '/' + file_name)
            else:
                print(file_name + ' not found in ' + original_folder)
        except Exception as EE:
            print(EE)
        x_count+=1
        if x_count == 1:
            break

    filename = "output.gif"
    folder = "static/output"
    file_path = os.path.join(folder, filename)
    if os.path.exists(file_path):
        path = "static/output/output.gif"
    else:
        path = "static/output/placeholder-image.png"
    img_out = os.path.join('static', 'output')
    out_file = os.path.join(img_out, 'output.gif')

    #return redirect('/')
    return render_template('index.html',img_output=path, img1=img1,img2=img2,img3=img3,img4=img4,img5=img5,img6=img6,img7=img7,img8=img8,img9=img9,img10=img10,img11=img11,img12=img12,img13=img13,img14=img14,img15=img15,img16=img16)

if __name__ == '__main__':
    app.run(debug=True)
