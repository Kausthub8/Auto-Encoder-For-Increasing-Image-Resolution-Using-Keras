from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D
from tensorflow.keras import regularizers
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Conv2DTranspose, UpSampling2D, add

l8 = UpSampling2D()(l7)
l9 = Conv2D(128, (3,3), padding='same', activation='relu', activity_regularizer = regularizers.l1(10e-10))(l8)
l10 = Conv2D(128, (3,3), padding='same', activation='relu', activity_regularizer = regularizers.l1(10e-10))(l9)
l11 = add([l5, l10])
l12 = UpSampling2D()(l11)
l13 = Conv2D(64, (3,3), padding='same', activation='relu', activity_regularizer = regularizers.l1(10e-10))(l12)
l14 = Conv2D(64, (3,3), padding='same', activation='relu', activity_regularizer = regularizers.l1(10e-10))(l13)
l15 = add([l14, l2])
Decoded = Conv2D(3, (3,3), padding='same', activation='relu', activity_regularizer = regularizers.l1(10e-10))(l15)

autoencoder = Model(x_input, Decoded)


autoencoder.summary()
