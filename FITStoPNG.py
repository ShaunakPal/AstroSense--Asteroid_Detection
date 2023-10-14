import os
from astropy.visualization import ZScaleInterval
from astropy.io import fits
import matplotlib.pyplot as plt

input_folder = "/path/to/folder"
output_folder = "/path/to/folder"

#Get the list of FITS files in the input folder
fits_files = [f for f in os.listdir(input_folder) if f.endswith('.fits')]


for fits_file in fits_files:
    #Load the FITS data
    fits_path = os.path.join(input_folder, fits_file)
    data = fits.getdata(fits_path)

    #Create a new figure without axes
    fig = plt.figure(frameon=False)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)

    #Plot the image data
    zscale = ZScaleInterval()
    plt.imshow(zscale(data), cmap="gray")

    #Save the image without graph markings
    output_filename = os.path.splitext(fits_file)[0] + ".png"
    output_path = os.path.join(output_folder, output_filename)
    print(f"Saving {fits_file} as {output_filename}")
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0)

    plt.close(fig)

print("All FITS files converted and saved in the output folder.")