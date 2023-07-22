import cv2 

x=input("please enter 1 or 2")
 
if x=="1": 
    img=cv2.imread("images.png")
    cv2.imshow("dora",img) #圖片名稱
    cv2.waitKey(0) #秀出影像,0代表沒限時間,1000代表1毫秒
else:
    img=cv2.imread("Lenna.jpg")
    cv2.imshow("lenna",img) #圖片名稱
    cv2.waitKey(0) #秀出影像,0代表沒限時間,1000代表1毫秒






#x=imput("please enter 1 or 2")

#if x=="1": #如果1就印出1
   # print("1")

#elif x=="2": #如果2就印出2
   # print("2")

#else: #不是1不是2就印error
    #print("error")
