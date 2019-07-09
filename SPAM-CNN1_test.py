import numpy as np
import cv2
from keras.preprocessing import image
from keras.models import load_model

model = load_model('my_model2.h5')

from tkinter.filedialog import askopenfilename
img_path = askopenfilename()

test_image = image.load_img(img_path, target_size = (64, 64))
test_image1 = image.img_to_array(test_image)
test_image2 = np.expand_dims(test_image1, axis = 0)
result = model.predict(test_image2)
if result[0][0] >=0.5:
  prediction = 'SPAM'
else:
  prediction = 'Non SPAM'
  

img = cv2.imread(img_path)  
cv2.imshow("Input",img)
cv2.waitKey(100)  
  
print(prediction)

