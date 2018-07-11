import cv2
import os

'''This is the command to read in the GIF. You need Videocapture which makes a cv2 Video Object.
Add your GIF file name in the parameter of this function.
'''

def convert_gif_to_frames(gif):

    # Initialize the frame number and create empty frame list
    frame_num = 0
    frame_list = []

    # Loop until there are frames left
    while True:
        try:
            # Try to read a frame. Okay is a BOOL if there are frames or not
            okay, frame = gif.read()
            # Append to empty frame list
            frame_list.append(frame)
            # Break if there are no other frames to read
            if not okay:
                break
            # Increment value of the frame number by 1
            frame_num += 1
        except KeyboardInterrupt:  # press ^C to quit
            break

    return frame_list


def output_frames_as_pics(frame_list, path):

    # Reduce the list of frames by half to make the list more managable
    frame_list_reduce = frame_list[0::2]

    for frames_idx in range(len(frame_list_reduce)):
        cv2.imwrite(os.path.join(path + '-' + str(frames_idx+1) + '.png'), frame_list_reduce[frames_idx])

    pass

if __name__ == '__main__':

    image_path = "./downloads/"
    for folder in os.listdir(image_path):
        if os.path.isdir(image_path + folder):
            for f in os.listdir(image_path + folder):
                file_path = image_path + folder + '/' + f
                path, file_extension = os.path.splitext(file_path)
                if file_extension == '.gif':
                    gif = cv2.VideoCapture(file_path)
                    frames = convert_gif_to_frames(gif)
                    output_frames_as_pics(frames, path)