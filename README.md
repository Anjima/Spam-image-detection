



# Spam-image-detection-
Python Jupyter Notebook with Convolutional Neural Network spam image classifier implemented in Keras.
Requirements

## Requirements

  * Keras = 2.x (TensorFlow backend)
  * Numpy = 1.x

## Usage

First, collect training and validation data and deploy it like this
```
./data/
  training_set/
    spam/
      spam1.jpg
      spam2.jpg
      ...
    non_spam/
      ham1.jpg
      ham2.jpg
      ...
  
  validation/
     spam/
      spam1.jpg
      spam2.jpg
      ...
    non_spam/
      ham1.jpg
      ham2.jpg
      ...
```

and then run train script.

```
SPAM-CNN1_train.py
```

Train script makes model and weights file

To test another images, run

```
SPAM-CNN1_test.py
```
