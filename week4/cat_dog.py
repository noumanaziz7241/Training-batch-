import json
import os
import cv2
from PIL import Image
import glob
# specify the paths for the JSON file and the images directory
json_path = "cat_dog_annotations.json"
images_dir = "augmentented"

# load the JSON file
with open(json_path, 'r') as f:
    data = json.load(f)

# create the class dictionary from the JSON file
class_dict = {}
class_counter = 0

for path in ((glob.glob('augmentented/*.jpeg'))):

    for img_id, img_data in data['_via_img_metadata'].items():
        for region in img_data['regions']:
            class_name = region['region_attributes']['class']
            if class_name not in class_dict.values():
                class_dict[class_counter] = class_name
                class_counter += 1

    # loop over each image in the JSON file
    for img_id, img_data in data['_via_img_metadata'].items():

        filename = os.path.splitext(img_data['filename'])[0]
        img_path = os.path.join(images_dir, img_data['filename'])
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # loop over each region in the image
        with open(f'{path}.txt', 'w') as f:
            for region in img_data['regions']:
                # extract the bounding box coordinates
                x = region['shape_attributes']['x']
                y = region['shape_attributes']['y']
                w = region['shape_attributes']['width']
                h = region['shape_attributes']['height']

                # get the class name and ID for the region
                class_name = region['region_attributes']['class']
                class_id = list(class_dict.keys())[list(class_dict.values()).index(class_name)]

                # write the class ID and bounding box coordinates to the output file
                f.write(f"{class_id} {((x + w / 2) / img.shape[1]):.6f} {((y + h / 2) / img.shape[0]):.6f} {(w / img.shape[1]):.6f} {(h / img.shape[0]):.6f}\n")

                cv2.rectangle(img, (x, y), (x+w, y+h), (255,0, 0), 3)

      display(Image.fromarray(img))