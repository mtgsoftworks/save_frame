import cv2
import os

def frame_rate(video_path):
    video = cv2.VideoCapture(video_path)

    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    total_seconds = int(video.get(cv2.CAP_PROP_FRAME_COUNT) / video.get(cv2.CAP_PROP_FPS))

    fps = total_frames / total_seconds

    return fps


def save_frames(video_path, fps):
    video = cv2.VideoCapture(video_path)

    total_seconds = int(video.get(cv2.CAP_PROP_FRAME_COUNT) / video.get(cv2.CAP_PROP_FPS))

    video_name = os.path.basename(video_path).split(".")[0]
    os.mkdir(video_name)

    for i in range(total_seconds):
        ret, frame = video.read()
        resized_frame = cv2.resize(frame, (1920, 1080))

        filename = "{}/frame_{}.png".format(video_name, i)
        cv2.imwrite(filename, resized_frame, params=[cv2.IMWRITE_PNG_COMPRESSION, 9])
        # cv2.imwrite(filename, frame, params=[cv2.IMWRITE_PNG_COMPRESSION, 9])


if __name__ == "__main__":
    video_path = input("Enter Video Path: ")

    fps = frame_rate(video_path)

    save_frames(video_path, fps)

    print("Process Successfully Completed")