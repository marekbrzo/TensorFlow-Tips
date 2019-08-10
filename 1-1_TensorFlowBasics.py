# The simplest Tensorflow application.
# In this application we will set up two variables which contain a single value
# and determine the sum of the two variables.

#%%
import tensorflow as tf

#%%
# Declaration of two single value variables.
a = tf.Variable(1 , name = 'a')
b = tf.Variable(2 , name ='b')

#%%
# The function 'f' seen below is the creation of a new graph that adds the two tensors above.
# The graph does not actually perform the addition yet.
f = a + b

#%%
# We neect to intialize any global variables before we run the graph.
init = tf.global_variables_initializer()

#%%
# Finally we CREATE a Tensorflow Session object, 
#               RUN our variable intializer, 
#       and EXECUTE the graph with eval()
with tf.Session() as s:
    init.run()
    print(f.eval())
