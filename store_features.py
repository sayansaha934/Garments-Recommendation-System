from feature_extractor import extract_feature
import os
import pickle

images_folder = 'static/database/'
images = os.listdir(images_folder)

features_data={}

print('Started extracting features')
for img in images:
    try:
        image_path = images_folder+img
        img_feature = extract_feature(image_path)
        features_data[img]=img_feature
    except Exception:
        pass

print('Feature extraction done')


pickle.dump(features_data, open('features.pkl', 'wb'))
print('All features stored into features.pkl file')