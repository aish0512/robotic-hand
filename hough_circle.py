

import sys
import cv2

window_title = "USB Camera"

def show_camera():
    camera_id = "/dev/video0"
    video_capture = cv2.VideoCapture(camera_id, cv2.CAP_V4L2)
   
    if video_capture.isOpened():
        try:
            window_handle = cv2.namedWindow(
                window_title, cv2.WINDOW_AUTOSIZE )
            # Window
            while True:
                ret_val, frame = video_capture.read()
                if cv2.getWindowProperty(window_title, cv2.WND_PROP_AUTOSIZE) >= 0:
                    #cv2.imshow(window_title, frame)
                    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                    # Apply GaussianBlur to reduce noise and improve circle detection
                    blurred_frame = cv2.GaussianBlur(gray_frame, (9, 9), 0)

                    # Detect circles using Hough Circle Transform
                    circles = cv2.HoughCircles(
                        blurred_frame,
                        cv2.HOUGH_GRADIENT,
                        dp=1,
                        minDist=50,
                        param1=50,
                        param2=30,
                        minRadius=20,
                        maxRadius=50,
                    )

                    if circles is not None:
                        circles = circles[0]  # Convert to 2D array if circles were detected
                        for circle in circles:
                            # Draw the detected circle
                            x, y, r = map(int, circle)
                            cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
                        print(circles);
                    # Display the output frame
                    cv2.imshow("Ball Detection", frame)
                else:
                    break
                keyCode = cv2.waitKey(10) & 0xFF
                # Stop the program on the ESC key or 'q'
                if keyCode == 27 or keyCode == ord('q'):
                    break

        finally:
            video_capture.release()
            cv2.destroyAllWindows()
    else:
        print("Unable to open camera")


if __name__ == "__main__":

    show_camera()
import sys
import cv2

window_title = "USB Camera"

def show_camera():
    camera_id = "/dev/video0"
    video_capture = cv2.VideoCapture(camera_id, cv2.CAP_V4L2)
   
    if video_capture.isOpened():
        try:
            window_handle = cv2.namedWindow(
                window_title, cv2.WINDOW_AUTOSIZE )
            # Window
            while True:
                ret_val, frame = video_capture.read()
                if cv2.getWindowProperty(window_title, cv2.WND_PROP_AUTOSIZE) >= 0:
                    #cv2.imshow(window_title, frame)
                    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                    # Apply GaussianBlur to reduce noise and improve circle detection
                    blurred_frame = cv2.GaussianBlur(gray_frame, (9, 9), 0)

                    # Detect circles using Hough Circle Transform
                    circles = cv2.HoughCircles(
                        blurred_frame,
                        cv2.HOUGH_GRADIENT,
                        dp=1,
                        minDist=50,
                        param1=50,
                        param2=30,
                        minRadius=20,
                        maxRadius=50,
                    )

                    if circles is not None:
                        circles = circles[0]  # Convert to 2D array if circles were detected
                        for circle in circles:
                            # Draw the detected circle
                            x, y, r = map(int, circle)
                            cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
                        print(circles);
                    # Display the output frame
                    cv2.imshow("Ball Detection", frame)
                else:
                    break
                keyCode = cv2.waitKey(10) & 0xFF
                # Stop the program on the ESC key or 'q'
                if keyCode == 27 or keyCode == ord('q'):
                    break

        finally:
            video_capture.release()
            cv2.destroyAllWindows()
    else:
        print("Unable to open camera")


if __name__ == "__main__":

    show_camera()
