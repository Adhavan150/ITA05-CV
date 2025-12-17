import cv2
img = cv2.imread(
    r"C:\Users\ADHAVAN GNANASEKAR\OneDrive\Desktop\air_canvas\python\lab program\Screenshot 2025-12-17 122641.png"
)
if img is None:
    print("Error: Image not found")
    exit()
blur = cv2.GaussianBlur(img, (15, 15), 0)
cv2.imshow("Original Image", img)
cv2.imshow("Gaussian Blurred Image", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
