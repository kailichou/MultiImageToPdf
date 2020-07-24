from PIL import Image
import os


def getImage(filepath, filename='/CombinedPDF.pdf'):
    
    images = []

    for f in filepath:
        x = Image.open(f)
        if x.mode == 'RGBA':
            x = x.convert('RGB')
            images.append(x)
        else:
            images.append(x)

    im1 = images.pop(0)
    imagelist = images
    if input(f"Would you like to save your file in {fileDirectory}? ====>\n").lower() == 'yes':
        savepath = fileDirectory + filename
    else:
        print("Please specify the directory, you'd like to save your file.")
        savepath = input("===>")
        if savepath.rsplit('/',1)[-1] == '':
            savepath = savepath.rsplit('/',1)[0]
        


    im1.save(savepath + filename, save_all=True, append_images=imagelist)
    print(f"Thank you for using this program. \nThe file {filename.split('/',1)[1]} is saved at folder {os.path.basename(savepath)}.")

            


fileDirectory = os.getcwd()

filepaths = input("Please add the pathname of images that you want to convert into a PDF file and seperate them with a comma ','===> \n").split(',')
getImage(filepaths,filename='/CombinedPDF.pdf')