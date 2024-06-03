import glob
from PIL import Image
import os
import shutil

def remove(path):
    """ param <path> could either be relative or absolute. """
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)  # remove the file
    elif os.path.isdir(path):
        shutil.rmtree(path)  # remove dir and all contains
    else:
        raise ValueError("file {} is not a file or dir.".format(path))

def get_order(name):
    frag = name[name.find("frame")+5:]
    frag = frag.replace(".png","")
    return int(frag)

def make_gif(frame_folder, number):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*")]
    frames_selected = []
    frames_selected.append(frames[1])
    for x in range(1,len(frames)):
        if x%5 == 0:
            frames_selected.append(frames[x])
    frames_selected.append(frames[len(frames)-1])
    frames = frames_selected
    frames.sort(key=lambda x: get_order(x.filename), reverse=False)
    frame_one = frames[0]
    frame_one.save("MicroRTS/LLM/mapBloodBath/EnemyLR/"+number+"_code.gif", format="GIF", append_images=frames,
               save_all=True, duration=0, optimize=True, loop=1)
    
if __name__=="__main__":
    print("inside main")
    for i in range(0,20):
        path = "MicroRTS/LLM/mapBloodBath/EnemyLR/"+str(i)+"_folderLog"
        make_gif(path, str(i))
        remove(path=path)