import noise_Generators.noise_generators as noise
import pathlib
import utils.ultils as utils

rute_grey_images = "c:\\Users\Bell\\Documents\\GitHub\\Addin-noise-to-images\\gray_images"
#rute_up = "d:\\escuela\\tesis\\AniDif\\fastaniso-master\\ds_ini"
rute_salt_and_pepper="c:\\Users\Bell\\Documents\\GitHub\\Addin-noise-to-images\\diferent_noise\\salt_and_pepper"
rute_initials_color_images = "c:\\Users\Bell\\Documents\\GitHub\\Addin-noise-to-images\\test_images"
rute_wand_laplacian="c:\\Users\Bell\\Documents\\GitHub\\Addin-noise-to-images\\diferent_noise\\wand_laplacian"
print(str(pathlib.Path(__file__).parent.absolute()))




utils.image_retrieve(rute_initials_color_images,rute_grey_images,noise.escala_grises)                                                                
utils.image_retrieve(rute_grey_images,rute_salt_and_pepper,noise.sp_noise,0.01)    
utils.image_retrieve(rute_grey_images,rute_wand_laplacian,noise.wand_laplacian)                                                                                                                                                                                                           

print("all done")
                        