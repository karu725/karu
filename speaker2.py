import cv2
import time
import timeit

# 영상 검출기
def videoDetector(cam, cascade, is_paused):
    video_start_time = timeit.default_timer()  # 비디오 시작 시간 기록
    prev_timestamp = None  # 이전 타임스탬프 변수 초기화
    fps = cam.get(cv2.CAP_PROP_FPS)  # Get the frames per second of the video
    while True:
        if not is_paused:
            # Algorithm operations

            ret, img = cam.read()
            if not ret:
                break  # Break the loop if there are no more frames

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            results = cascade.detectMultiScale(gray,
                                               scaleFactor=1.1,
                                               minNeighbors=5,
                                               minSize=(20, 20))

            for box in results:
                x, y, w, h = box
                # Output timestamp based on video time
                frame_number = cam.get(cv2.CAP_PROP_POS_FRAMES) - 1
                elapsed_time = frame_number / fps
                timestamp = time.strftime('%H:%M:%S', time.gmtime(elapsed_time))
                if timestamp != prev_timestamp:  # Check if timestamp is different from previous timestamp
                    prev_timestamp = timestamp
                    print("Face recognized at:", timestamp)

            # Algorithm operations

        key = cv2.waitKey(1)
        if key == 32:  # Spacebar key
            is_paused = not is_paused  # Toggle the pause state
        elif key > 0:
            break

# 가중치 파일 경로
cascade_filename = 'haarcascade_frontalface_alt.xml'
# 모델 불러오기
cascade = cv2.CascadeClassifier(cascade_filename)

# 영상 파일 
video_file = 'D:/데이터작업/1.편성표분할작업/11/01/E20201101_00009_video_10800_10984.mp4'
cam = cv2.VideoCapture(video_file)

is_paused = False  # Flag to indicate if the video is paused
videoDetector(cam, cascade, is_paused)

cam.release()


