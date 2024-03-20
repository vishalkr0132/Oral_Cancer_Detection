import numpy as np
import keras 
from keras.preprocessing.image import ImageDataGenerator
from PIL import Image 
import PIL.Image

# from keras.preprocessing.image import load_img
from tensorflow.keras.utils import load_img
# from keras.preprocessing.image import img_to_array
from tensorflow.keras.utils import img_to_array

from keras.models import load_model

# model_path =("OralCancel.h5")

def pred_Cancer_NonCancer(Cancer_or_NonCancer):
  model = keras.models.load_model('D:\Django\Cancer\Home\OralCancel.h5') 
  test_image = PIL.Image.open(Cancer_or_NonCancer)
  test_image = test_image.resize((150, 150))
  test_image = np.asarray(test_image) / 255.0
  test_image = np.expand_dims(test_image, axis=0)

  result = model.predict(test_image).round(3)
  pred = np.argmax(result)

  if pred == 0:
    return'Cancer'
  else:
    return'NonCancer'

# Cancer_or_NonCancer = "./nonthird.jpg"
# print(pred_Cancer_NonCancer(Cancer_or_NonCancer))
