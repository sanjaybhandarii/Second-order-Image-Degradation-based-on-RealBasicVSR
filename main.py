"""
Credit for this project : https://basicsr.readthedocs.io/en/latest/_modules/basicsr/data/degradations.html
                         and 
                         RealESRGAN paper https://arxiv.org/abs/2107.10833
"""

from degrade import *

#path to your High resolution image here
path = "a.jpg"

#path to save degraded image here
save_loc ="b.jpg"

def process_all_image():

    for img in os.listdir(path):
    
        src = cv2.imread(path + "/" + img, cv2.IMREAD_UNCHANGED)

        frame = degrade_img(src)
        
        resize_dim = (512,512)
        src = cv2.resize(src, resize_dim, interpolation=cv2.INTER_AREA)
        
        cv2.imshow("Src image", src)
        cv2.waitKey(0)
        
        cv2.imshow("Degraded image", frame)
        cv2.waitKey(0)
        
        cv2.destroyAllWindows()
        
        frame = 255 * frame

        cv2.imwrite(save_loc + "/" + img, frame)

def main():
    process_all_image()
    
if __name__ == "__main__":
    main()
