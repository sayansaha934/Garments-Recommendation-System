import numpy as np
import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input
from numpy.linalg import norm


#loading pre-trained model
model = InceptionV3(include_top = False, weights='imagenet',input_shape=(224,224,3))

#adding a layer to the model
model = tensorflow.keras.Sequential([
    model,
    GlobalMaxPooling2D()
])


def extract_feature(image_path):
    '''
    Method: extract_feature
    Description: This method takes an image, expand its dimension,
                 preprocess the image, extract feature vector from the image,
                 and normalise it.
    Output: A list of feature vector

    '''

    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_expand = np.expand_dims(img_array,axis=0)
    processed_image = preprocess_input(img_expand)
    result = model.predict(processed_image).flatten()
    result_norm = result/norm(result)
    return result_norm