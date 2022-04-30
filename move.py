import os
import shutil
from tqdm import tqdm

root_src = "/data/wudong/plane_data/ScanNet/scans"
root_dst = "/data/wudong/scannet/scans"

scene_lists = os.listdir(root_src)

for scene in tqdm(scene_lists):
    print(scene)
    src_path = os.path.join(root_src, scene, "annotation")
    dst_path = os.path.join(root_dst, scene, "annotation")
    #shutil.move(src_path, dst_path)