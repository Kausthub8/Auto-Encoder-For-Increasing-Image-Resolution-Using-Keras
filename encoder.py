from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D
from tensorflow.keras import regularizers
from tensorflow.keras.models import Model
x_input = Input(shape=(256, 256, 3))
l1 = Conv2D(64, (3,3), padding='same', activation='relu', activity_regularizer = regularizers.l1(10e-10))(x_input)
l2 = Conv2D(64, (3,3), padding='same', activation='relu', activity_regularizer = regularizers.l1(10e-10))(l1)
l3 = MaxPooling2D(padding = 'same')(l2)
l4 = Conv2D(128, (3,3), padding='same', activation='relu', activity_regularizer = regularizers.l1(10e-10))(l3)
l5 = Conv2D(128, (3,3), padding='same', activation='relu', activity_regularizer = regularizers.l1(10e-10))(l4)
l6 = MaxPooling2D(padding = 'same')(l5)
l7 = Conv2D(256, (3,3), padding='same', activation='relu', activity_regularizer = regularizers.l1(10e-10))(l6)

encoder = Model(x_input, l7)

encoder.summary()
