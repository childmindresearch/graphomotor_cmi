import cv2

video_path = r"C:\Users\MoBI\Desktop\From Old Setup\sync_test\Diary_of_a_Wimpy_Kid_Trailer.mp4"
cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
while(1):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
        cap.release()
        cv2.destroyAllWindows()
        break
    cv2.imshow('frame',frame)