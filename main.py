import cv2
import numpy as np
import glob
from src.add_image import add_transparent_image

paths = glob.glob("./input/*jpeg")


x1,x2,y1,y2=None,None,None,None


def main(path):

    global frame
    frame = cv2.imread(path)
    frame_path = path.split("/")[-1].split("\\")[-1].split(".")[0]
    #---------------EKLENECEK GÖRSELLERİN ŞEFFAF HALLERİ-------------#
    uai_transparent = cv2.imread('./img/uai.png', cv2.IMREAD_UNCHANGED)  
    uap_transparent = cv2.imread('./img/uap.png', cv2.IMREAD_UNCHANGED)  
    image_height, image_weight, c = frame.shape

    def mouse(event,x,y,flags,params): 

        global frame,x1,x2,y1,y2,add_image,class_id,f

        #------UAP İÇİN MOUSE TAKİBİ-----#
        #-------------SOL TIK -----------# 
        if event == cv2.EVENT_LBUTTONDOWN:
            try: 
                x1,y1 = x,y
                #------KULLANILACAK İMAGE VE İDSİ-------#
                add_image,class_id = uap_transparent,2
            except: pass
            
        elif event == cv2.EVENT_LBUTTONUP:
            try: 
                x2,y2 = x,y
            except: pass

        #------UAİ İÇİN MOUSE TAKİBİ-----# 
        #-------------SAĞ TIK -----------#
        elif event == cv2.EVENT_RBUTTONDOWN:
            try: 
                x1,y1 = x,y
                #------KULLANILACAK İMAGE VE İDSİ-------#
                add_image, class_id = uai_transparent, 3
            except: pass
            
        elif event == cv2.EVENT_RBUTTONUP:
            try: 
                x2,y2 = x,y
            except: pass
            
        #-----TÜM MOUSE HAREKETLERİ-----#
        elif event == cv2.EVENT_MOUSEMOVE:
    
            if x2 != None and x1 != None and y1 != None and y2 != None:

                frame_copy = frame.copy()
                f = open(f'./output/{frame_path}.txt', "a")
                cv2.rectangle(frame_copy,(x1,y1),(x2,y2),(0,255,0),2)
                #-----------------ORJİNAL RESİM ÜZERİNE EKLEME YAPILMASI-------------------------#
                new_image = add_transparent_image(frame, cv2.resize(add_image, (abs(2*x2-2*x1),abs(2*y2-2*y1))), 2*x1, 2*y1)
                frame = new_image  # OLUŞTURULAN GÖRSELİ ORJİNAL HALİNE EŞİTLİYORUZ

                txt_final = txt_create(x1,y1,x2,y2,image_weight,image_height,class_id)
                f.write(txt_final)

                x1,x2,y1,y2 = None,None,None,None 
                # YENİ GELEN DEĞERLER İLE ESKİLERİ ÇAKIŞMAMASI İÇİN SÜREKLİ DEĞİŞKENLERİ TEMİZLİYORUZ

            cv2.imshow("frame",cv2.resize(frame,(image_weight//2,image_height//2)))
            cv2.waitKey(1)
 
    cv2.namedWindow("frame") 
    cv2.setMouseCallback("frame",mouse) 
    cv2.imshow("frame", cv2.resize(frame,(image_weight//2,image_height//2)))
    cv2.waitKey(0)
    cv2.imwrite(f'./output/{frame_path}.jpeg',frame,  [cv2.IMWRITE_JPEG_QUALITY, 100])
    f.close()



def txt_create(xmin,ymin,xmax,ymax,image_weight,image_height,class_id):

    basamak = 6
    # GÖRSELİ İMSHOW EDERKEN KÜÇÜLTÜĞÜMÜZ İÇİN GELEN DEĞERLERİ AYNI ORANDA ÇARPIYORUZ
    xmin = xmin*2
    ymin = ymin*2
    xmax = xmax*2
    ymax = ymax*2

    box_weight = abs(xmax-xmin)
    box_height = abs(ymax-ymin)

    x_x = box_weight / 2
    y_y = box_height / 2 
    x_center = xmin + x_x
    y_center = ymin + y_y

    x_center_yolo = x_center / image_weight
    y_center_yolo = y_center / image_height 
    yolo_weight = box_weight / image_weight
    yolo_height = box_height / image_height

    x_center_yolo = str(round(x_center_yolo,basamak))
    y_center_yolo = str(round(y_center_yolo,basamak))
    yolo_weight = str(round(yolo_weight,basamak))
    yolo_height = str(round(yolo_height,basamak))

    txt_final  = str(class_id) +" "+ x_center_yolo +" "+ y_center_yolo +" "+ yolo_weight +" "+ yolo_height +"\n"

    return txt_final


for path in paths:
    main(path)
