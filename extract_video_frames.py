import cv2
import os

def extract_frames(video_path, output_folder):
    """
    Extracts frames from a video and saves them as images in a specified folder.

    Args:
        video_path (str): The path to the input video file.
        output_folder (str): The path to the directory where frames will be saved.
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    frame_count = 0
    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # If 'ret' is False, it means there are no more frames or an error occurred
        if not ret:
            break

        # Construct the output filename
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.png")

        # Save the current frame as an image
        cv2.imwrite(frame_filename, frame)

        frame_count += 1

    # Release the video capture object
    cap.release()
    print(f"Extracted {frame_count} frames to {output_folder}")

# Example usage:
video_file = "vid3.mp4"  # Replace with the actual path to your video
output_directory = "vid3/"

extract_frames(video_file, output_directory)
