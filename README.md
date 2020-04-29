# Auto-Encoder-for-Increasing-Image-Resolution-Using-Keras
1. This is an example of auto-encoder for perfoming image transformation tasks like Denoising, Super-Resolution and
Colorization

2. In order to train this autoencoder, you can take dataset from:

<https://ai.stanford.edu/~jkrause/cars/car_dataset.html>

3. An Auto-encoder is a type of Neural Network that tries to learn a representation of its input data, but in a space with much smaller dimensionality. This smaller representation is able to learn important features of the input data that can be used to later reconstruct the data. An auto encoder is principally composed of 3 elements: an encoder, a decoder and a loss function.
4. Both the encoder and decoder are usually Convolutional Neural Networks.

5. In order to teach an auto-encoder how to reconstruct an image, we need to show it pairs of low quality and high quality images. This way, then network will try to find the patterns and important encoded visual features needed to be able to reconstruct it from the low quality version.
