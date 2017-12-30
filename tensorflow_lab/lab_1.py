import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Create TensorFlow object called hello_constant
hello_constant = tf.constant('Hello World!')
x = tf.placeholder(tf.string)
y = tf.placeholder(tf.int32)
z = tf.placeholder(tf.float32)

with tf.Session() as sess:
    # Run the tf.constant operation in the session
    # output = sess.run(hello_constant)
    output = sess.run(x, feed_dict={x: 'Test String', y: 123, z: 45.67})
    print(output)

# A is a 0-dimensional int32 tensor
A = tf.constant(1234)

# B is a 1-dimensional int32 tensor
B = tf.constant([123, 456, 789])

# C is a 2-dimensional int32 tensor
C = tf.constant([[123, 456, 789], [222, 333, 444]])

add = tf.add(5, 2)
print(add)

sub = tf.subtract(10, 4)
print(sub)

mul = tf.multiply(2, 5)
print(mul)

cast_value = tf.subtract(tf.cast(tf.constant(2.0), tf.int32), tf.constant(1))
print(cast_value)
