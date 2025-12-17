import cv2
img = cv2.imread(
    r"C:\Users\ADHAVAN GNANASEKAR\OneDrive\Desktop\air_canvas\python\lab program\Screenshot 2025-12-17 122641.png"
)
if img is None:
    print("Error: Image not found")
    exit()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
cv2.imshow("Original Image", img)
cv2.imshow("Canny Edge Detection", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
