from feature_extractor import extract_feature
from sklearn.neighbors import NearestNeighbors
import pickle

#loading the images and it's corresponding feature vectors
images_features = pickle.load(open('features.pkl', 'rb'))
images_list = list(images_features.keys())
features_list = list(images_features.values())


def recommend(image_path):
    '''
    Method: recommend
    Description: This method takes feature vectors as input,
                and gives the 10 most similar images from database.
    Output: A list of images

    '''

    image_feature = extract_feature(image_path)
    recommended_images = []
    neighbor = NearestNeighbors(n_neighbors=10, algorithm='brute', metric='cosine')
    neighbor.fit(features_list)
    distance, indexes = neighbor.kneighbors([image_feature])

    for index in indexes[0]:
        recommended_images.append(images_list[index])

    return recommended_images