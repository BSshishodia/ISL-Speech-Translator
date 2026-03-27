import cv2

def play_video(video_path):

    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("ISL Output", frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()