#task3
import json
import os
from PIL import Image
import glob

images_dir = "/home/nouman/Downloads/training_batch/week4/test"
with open('/home/nouman/Downloads/training_batch/week4/conversion_test/conversion_test.json') as f:
    data = json.load(f)
for path in ((glob.glob('/home/nouman/Downloads/training_batch/week4/test/*.jpeg'))):
    
    # Define the class labels
    classes = list(set([list(region['region_attributes']['class'].keys())[0] for img_data in data['_via_img_metadata'].values() for region in img_data['regions']]))
    class_labels = {classes[i]: i for i in range(len(classes))}

    # Get the filename, x, y, width, height and class label for each annotation
    annotations = []
    for filename, img_data in data['_via_img_metadata'].items():
        # Extract the image filename without extension and path
        image_name = os.path.splitext(os.path.basename(img_data['filename']))[0]
        img_path = os.path.join(images_dir, img_data['filename'])
        if path.split('/')[-1].split('.')[0][:len(image_name)]==image_name:

            for region in img_data['regions']:
                shape_attributes = region['shape_attributes']
                labels = list(region['region_attributes']['class'].keys())
                for label in labels:
                    annotations.append((img_path, shape_attributes['x'], shape_attributes['y'], shape_attributes['width'], shape_attributes['height'], label))

        # Process each image and save the annotations to a txt file
        for image_id in set([a[0] for a in annotations]):
            processed_annotations = []
            for ann in annotations:
                if ann[0] == image_id:
                    processed_annotations.append(ann)

                txt_path = os.path.splitext(path)[0] + ".txt"
                with open(txt_path, "w") as f:
                    for ann in processed_annotations:
                        x, y, w, h = ann[1:5]
                        # Normalize the bounding box coordinates
                        img_width, img_height = Image.open(ann[0]).size
                        x_center = (x + w/2) / img_width
                        y_center = (y + h/2) / img_height
                        width = w / img_width
                        height = h / img_height
                        # Get the class ID
                        class_id = class_labels[ann[5]]
                        # Write the annotation to the txt file
                        f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")