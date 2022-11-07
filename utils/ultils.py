import matplotlib.pyplot as plt
from skimage import io
import os
#import generateDS.my_globals as globals
import pathlib

def image_retrieve(rute_up,rute_down,image_funtion, *args):
    rootDir = rute_up
    rootFinal = rute_down
    i = 0
    for dirName, subdirList, fileList in os.walk(rootDir):

        for fname in fileList:
            # creamos la carpeta asociada a la foto
            if not (os.path.isdir(str(rootFinal)+"\\"+str(fname)[:len(str(fname))-4] + str('_') + str(i))):
                os.mkdir(str(rootFinal)+"\\"+str(fname)
                        [:len(str(fname))-4] + str('_') + str(i))
            # aca cuando metamos concurrencia
            # concurrency_handler()
            print(dirName)
            print("-----------------------")
            print(subdirList)
            print("-----------------------")
            print(fileList)
            print("-----------------------")
            print(fname)
            print("-----------------------")
            result_list = []
            img_PIL = io.imread(str(dirName)+'\\'+str(fname))

            j = 0
            os.chdir(rute_down+'\\'+str(fname)
                    [:len(str(fname))-4] + str('_') + str(i))
            io.imsave(str(i)+'_ite_'+str(0)+'.jpg', img_PIL)
            io.imshow(img_PIL)

            print(str(pathlib.Path(__file__).parent.absolute()))

            #fastaniso.anisodiff(img_PIL, number_of_iterations,result_list)
            gray_image = image_funtion(img_PIL, args)
            io.imsave(str(i)+'_ite_'+str(j)+'.jpg', gray_image)

            # for item in result_list:
            #    j+=1
            #    io.imsave(str(i)+'_ite_'+str(j)+'.jpg', result_list[j-1])
            #
            i += 1