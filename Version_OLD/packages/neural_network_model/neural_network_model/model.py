# for the convolutional network
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
from keras.optimizers import Adam
from keras.callbacks import ReduceLROnPlateau, ModelCheckpoint
from keras.wrappers.scikit_learn import KerasClassifier

from neural_network_model.config import config


def cnn_model(kernel_size=(3, 3),
              pool_size=(2, 2),
              first_filters=32,
              second_filters=64,
              third_filters=128,
              dropout_conv=0.3,
              dropout_dense=0.3,
              image_size=50):

    model = Sequential()
    model.add(Conv2D(
      first_filters,
      kernel_size,
      activation='relu',
      input_shape=(image_size, image_size, 3)))
    model.add(Conv2D(first_filters, kernel_size, activation = 'relu'))
    model.add(MaxPooling2D(pool_size=pool_size))
    model.add(Dropout(dropout_conv))

    model.add(Conv2D(second_filters, kernel_size, activation='relu'))
    model.add(Conv2D(second_filters, kernel_size, activation ='relu'))
    model.add(MaxPooling2D(pool_size=pool_size))
    model.add(Dropout(dropout_conv))

    model.add(Conv2D(third_filters, kernel_size, activation='relu'))
    model.add(Conv2D(third_filters, kernel_size, activation ='relu'))
    model.add(MaxPooling2D(pool_size=pool_size))
    model.add(Dropout(dropout_conv))

    model.add(Flatten())
    model.add(Dense(256, activation="relu"))
    model.add(Dropout(dropout_dense))
    model.add(Dense(12, activation="softmax"))

    model.compile(Adam(lr=0.0001),
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    return model


checkpoint = ModelCheckpoint(config.MODEL_PATH,
                             monitor='acc',
                             verbose=1,
                             save_best_only=True,
                             mode='max')

reduce_lr = ReduceLROnPlateau(monitor='acc',
                              factor=0.5,
                              patience=2,
                              verbose=1,
                              mode='max',
                              min_lr=0.00001)

callbacks_list = [checkpoint, reduce_lr]

cnn_clf = KerasClassifier(build_fn=cnn_model,
                          batch_size=config.BATCH_SIZE,
                          validation_split=10,
                          epochs=config.EPOCHS,
                          verbose=1,  # progress bar - required for CI job
                          callbacks=callbacks_list,
                          image_size=config.IMAGE_SIZE
                          )


if __name__ == '__main__':
    model = cnn_model()
    model.summary()
