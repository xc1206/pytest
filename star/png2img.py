import os
def transform(dir):
    for pngName in os.listdir(dir):
        with open(dir+"/"+pngName,"rb") as png:
            with open(dir+"/"+pngName.split(".")[0]+".jpg","wb") as img:
                img.write(png.read())
if __name__=="__main__":
    dir="E:/py/files/img"
    transform(dir)