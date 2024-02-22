import cv2
import os
import time
import uuid

IMAGES_PATH = 'Tensorflow/workspace/images/collectedimages'
labels = ['hello', 'thanks', 'yes', 'iloveyou']
number_imgs = 15

# Create directories for each label if they don't exist
for label in labels:
    label_path = os.path.join(IMAGES_PATH, label)
    if not os.path.exists(label_path):
        os.makedirs(label_path)

cap = cv2.VideoCapture(0)

for label in labels:
    print('Collecting images for {}'.format(label))
    time.sleep(5)  # Delay to prepare for image capture

    for img_num in range(number_imgs):
        ret, frame = cap.read()

        img_name = os.path.join(IMAGES_PATH, label, '{}_{}.jpg'.format(label, str(uuid.uuid4())))
        cv2.imwrite(img_name, frame)

        cv2.imshow("frame", frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()