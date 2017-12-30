import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# TODO: Convert the following to TensorFlow:
x = tf.constant(10)
y = tf.constant(2)
z = tf.subtract(tf.divide(x, y), tf.cast(tf.constant(1), tf.float64))

# TODO: Print z from a session
with tf.Session() as sess:
    # Run the tf.constant operation in the session
    # output = sess.run(hello_constant)
    output = sess.run(z)
    print(output)
