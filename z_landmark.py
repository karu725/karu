# 랜드마크

import cv2
import dlib
import numpy as np

# 얼굴 검출기 초기화
detector = dlib.get_frontal_face_detector()
# 얼굴 특징점 검출기 초기화
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# 이미지 로드
image = cv2.imread('D:/data/2speaker/11/02/frame_0.jpg')

# 그레이스케일로 변환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 얼굴 검출
faces = detector(gray)

# 얼굴 바운딩 박스와 특징점 표시
for face in faces:
    # 얼굴 바운딩 박스 좌표
    x, y, w, h = face.left(), face.top(), face.width(), face.height()


    # 얼굴 특징점 검출
    landmarks = predictor(gray, face)

    # 왼쪽 눈 좌표 평균 계산
    x_left_eye = np.mean([landmarks.part(37).x, landmarks.part(38).x, landmarks.part(40).x, landmarks.part(41).x]).astype(int)
    y_left_eye = np.mean([landmarks.part(37).y, landmarks.part(38).y, landmarks.part(40).y, landmarks.part(41).y]).astype(int)

    # 오른쪽 눈 좌표 평균 계산
    x_right_eye = np.mean([landmarks.part(43).x, landmarks.part(44).x, landmarks.part(46).x, landmarks.part(47).x]).astype(int)
    y_right_eye = np.mean([landmarks.part(43).y, landmarks.part(44).y, landmarks.part(46).y, landmarks.part(47).y]).astype(int)

    # 왼쪽 눈 중앙에 점 표시
    cv2.circle(image, (x_left_eye, y_left_eye), 3, (0, 255, 0), -1)

    # 오른쪽 눈 중앙에 점 표시
    cv2.circle(image, (x_right_eye, y_right_eye), 3, (0, 255, 0), -1)
    

    # 코 좌표 표시
    x_nose = landmarks.part(30).x
    y_nose = landmarks.part(30).y
    cv2.circle(image, (x_nose, y_nose), 3, (0, 255, 0), -1)
    

    # 입 좌표 표시
    x_mouth_left = landmarks.part(48).x
    y_mouth_left = landmarks.part(48).y
    x_mouth_right = landmarks.part(54).x
    y_mouth_right = landmarks.part(54).y
    cv2.circle(image, (x_mouth_left, y_mouth_left), 3, (0, 255, 0), -1)
    cv2.circle(image, (x_mouth_right, y_mouth_right), 3, (0, 255, 0), -1)
    

# 결과 이미지 출력
cv2.imshow('Facial Landmarks with Bounding Box', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
