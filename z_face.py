import cv2
import os

# DNN 모델 로드
net = cv2.dnn.readNetFromCaffe("deploy.prototxt.txt", "res10_300x300_ssd_iter_140000_fp16.caffemodel")


def save_frames(video_path, output_directory, face_directory, video_index):
    # 동영상 파일 열기
    video = cv2.VideoCapture(video_path)

    # 프레임 카운터 초기화
    frame_count = 0

    # 동영상의 전체 프레임 수 구하기
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # 동영상의 FPS(Frames Per Second) 구하기
    fps = video.get(cv2.CAP_PROP_FPS)

    # 이미지 저장 폴더 생성
    output_directory = os.path.join(output_directory, f"{video_index}_image")
    os.makedirs(output_directory, exist_ok=True)

    # 얼굴 이미지 저장 폴더 생성
    face_directory = os.path.join(face_directory, f"{video_index}_face")
    os.makedirs(face_directory, exist_ok=True)

    # 동영상 프레임 순회
    while frame_count < total_frames:
        # 프레임 읽기
        ret, frame = video.read()

        # 프레임을 모두 읽었으면 종료
        if not ret:
            break

        # 60프레임마다만 작업 수행
        if frame_count % 60 == 0:
            # 이미지 파일 이름 생성
            image_name = f"{video_index}_{frame_count}.jpg"

            # 이미지 파일 경로 생성
            image_path = os.path.join(output_directory, image_name)

            # 얼굴 검출을 위해 이미지 사이즈 변경
            blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))

            # DNN 모델을 통해 얼굴 검출
            net.setInput(blob)
            detections = net.forward()

            # 검출된 얼굴의 신뢰도가 일정 값 이상인 경우
            confidence = detections[0, 0, 0, 2]
            if confidence > 0.6:
                # 얼굴 이미지 파일 이름 생성
                face_image_name = f"{video_index}_{frame_count}_face.jpg"

                # 얼굴 이미지 파일 경로 생성
                face_image_path = os.path.join(face_directory, face_image_name)

                # 얼굴 이미지 파일 저장
                cv2.imwrite(face_image_path, frame)
            else:
                # 전체 이미지 파일 저장
                cv2.imwrite(image_path, frame)

        # 60프레임마다 프레임의 진행 상태 출력
        if frame_count % 60 == 0:
            print(f"Processing frame {frame_count}/{total_frames} in video {video_index}")

        # 프레임 카운터 증가
        frame_count += 1

    # 동영상 파일 닫기
    video.release()

    print(f"Frame extraction complete for video {video_index}")


def process_videos(folder_path):
    # 폴더 경로에서 폴더 이름 추출
    folder_name = os.path.basename(folder_path)

    # 작업 폴더와 같은 위치에 이미지 파일을 저장할 디렉토리 경로 생성
    output_directory = os.path.join(os.path.dirname(folder_path), f"{folder_name}_image")
    os.makedirs(output_directory, exist_ok=True)

    # 작업 폴더와 같은 위치에 얼굴 이미지를 저장할 디렉토리 경로 생성
    face_directory = os.path.join(os.path.dirname(folder_path), f"{folder_name}_face")
    os.makedirs(face_directory, exist_ok=True)

    # 폴더 내의 모든 파일 확인
    for video_index, file_name in enumerate(os.listdir(folder_path), start=1):
        # 파일 경로 생성
        file_path = os.path.join(folder_path, file_name)

        # 파일인 경우에만 작업 수행
        if os.path.isfile(file_path):
            # 동영상 파일인지 확인
            if file_name.endswith(('.mp4', '.avi', '.mov')):
                print(f"Processing video {video_index}: {file_name}")
                save_frames(file_path, output_directory, face_directory, video_index)


if __name__ == "__main__":
    # 폴더 경로 입력
    folder_path = input("작업 폴더: ")

    # 함수 호출
    process_videos(folder_path)
