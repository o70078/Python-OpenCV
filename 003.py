#coding=utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

print cv2.useOptimized();
cv2.setUseOptimized(onoff=True);
print cv2.useOptimized();

if __name__ == "__main__":

    #关于载入与建立
    img = cv2.imread('009.jpg')
    img = cv2.resize(img, (800, 600))
    #patch = img[0:100, 0:100]#剪切
    img3=img.copy()
    img2 = np.array([
        [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
        [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
        [[255, 255, 255], [128, 128, 128], [0, 0, 0]],
    ], dtype=np.uint8)

    #关于存储
    #用matplotlib存储
    #plt.imsave('img_pyplot.jpg', img)
    #用cv存储
    #cv2.IMWRITE_JPEG_QUALITY指定jpg质量，范围0到100，默认95，越高画质越好，文件越大
    #cv2.IMWRITE_PNG_COMPRESSION指定png质量，范围0到9，默认3，越高文件越小，画质越差
    #cv2.imwrite('img_cv2.jpg', img2,(cv2.IMWRITE_JPEG_QUALITY, 100))

    # 不直接指定缩放后大小，通过fx和fy指定缩放比例，0.5则长宽都为原来一半
    # 等效于img_200x300 = cv2.resize(img, (300, 200))，注意指定大小的格式是(宽度,高度)
    # 插值方法默认是cv2.INTER_LINEAR，这里指定为最近邻插值
    img3 = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #0:色调（Hue）1:饱和度（Saturation） 2:明度（Value）
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hsv[:,:,1]=hsv[:,:,1]*1.1
    hsvimg3 = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
    
    #分裂通道与合并通道
    r,g,b=cv2.split(hsvimg3)
    b[:]=b[:]*0.1
    hsvimg3=cv2.merge((r,g,b))

    #设置与读取单个像素
    print img.item(10,10,2)
    img.itemset((10,10,2),0)
    '''
    borderType 要添加那种类型的边界，类型如下
    – cv2.BORDER_CONSTANT 添加有颜色的常数值边界，还需要 下一个参数（value）。
    – cv2.BORDER_REFLECT边界元素的镜像。比如:fedcba|abcdefgh|hgfedcb
    – cv2.BORDER_REFLECT_101orcv2.BORDER_DEFAULT 跟上面一样，但稍作改动。例如: gfedcb|abcdefgh|gfedcba
    – cv2.BORDER_REPLICATE重复最后一个元素。例如: aaaaaa| abcdefgh|hhhhhhh
    – cv2.BORDER_WRAP 不知道怎么说了, 就像这样: cdefgh| abcdefgh|abcdefg
    '''
    hsvimg3=cv2.copyMakeBorder(hsvimg3,10,10,10,10,cv2.BORDER_CONSTANT,value=(0,128,128))

    cv2.imshow('A TestImage',hsvimg3)
    cv2.waitKey()
    cv2.destroyAllWindows()

    plt.subplot(131),plt.imshow(hsvimg3,'gray'),plt.title('1')
    plt.subplot(132),plt.imshow(img,'gray'),plt.title('2')
    plt.subplot(133),plt.imshow(img2,'gray'),plt.title('3')
    plt.show()
