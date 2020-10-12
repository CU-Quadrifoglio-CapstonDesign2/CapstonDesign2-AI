import tensorflow as tf
import numpy as np
import random as random
import matplotlib.pyplot as plt
tf.set_random_seed(777)

xy = np.loadtxt('training_valu_remo.csv', delimiter = ',', skiprows=1, dtype = np.float32)

x_training_set = xy[:,:] 
y_training_set = xy[:,[-1]]

X = tf.placeholder(tf.float32, [None, 12])
Y = tf.placeholder(tf.float32, [None, 1])


W1 = tf.get_variable("W1",shape = [12,10],initializer = tf.contrib.layers.xavier_initializer())

b1 = tf.Variable(tf.random_normal([10]), name='bias')

X1 = tf.matmul(X, W1)+b1


W2 = tf.get_variable("W2",shape = [10,5],initializer = tf.contrib.layers.xavier_initializer())

b2 = tf.Variable(tf.random_normal([5]), name='bias')

X2 = tf.nn.relu(tf.matmul(X1,W2)+b2)


W3 = tf.get_variable("W3",shape = [5,1],initializer = tf.contrib.layers.xavier_initializer())

b3 = tf.Variable(tf.random_normal([1]), name='bias')

X3 = tf.matmul(X2,W3)+b3



W4 = tf.get_variable("W4",shape = [1,1],initializer = tf.contrib.layers.xavier_initializer())

b4 = tf.Variable(tf.random_normal([1]), name='bias')

X4 = tf.sigmoid(tf.matmul(X3,W4)+b4)



W5 = tf.get_variable("W5",shape = [1,1],initializer = tf.contrib.layers.xavier_initializer())

b5 = tf.Variable(tf.random_normal([1]), name='bias')

X5 = tf.matmul(X4, W5) + b5



W6 = tf.get_variable("W6",shape = [1,1],initializer = tf.contrib.layers.xavier_initializer())

b6 = tf.Variable(tf.random_normal([1]), name='bias')

X6 = tf.sigmoid(tf.matmul(X5,W6)+b6)


W7 = tf.get_variable("W7",shape = [1,1],initializer = tf.contrib.layers.xavier_initializer())

b7 = tf.Variable(tf.random_normal([1]), name='bias')



logits = tf.matmul(X6, W7) + b7

hypothesis = logits

cost = tf.reduce_mean(tf.square(hypothesis - Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)


predicted = tf.round(hypothesis) 

accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32)) 

saver = tf.train.Saver()

min_loss = 100000000

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(100000): 
        idx = random.randint(0, x_training_set.size-1)
        _ =sess.run(optimizer, feed_dict={X: x_training_set[idx:idx+1,:], Y: y_training_set[idx:idx+1, :]}) 
        
        if step % 10000 == 0:
            loss_train,acc_train = sess.run([cost, accuracy], feed_dict = {X: x_training_set,Y: y_training_set})
            print("Step: {:5}\ttrain_Loss: {:.3f}\t train_Acc: {:.2%}\n".format(step,loss_train, acc_train))
            if min_loss > loss_train:
                min_loss = loss_train
                save_path = saver.save(sess, r"D:\과제들\4학년\CAPSTONE2\Project")
                print("save complite: %s"%save_path)
            
    saver.restore(sess, r"D:\과제들\4학년\CAPSTONE2\Project")
    check_val_cost, check_val_acc = sess.run([cost,accuracy], feed_dict = {X: x_training_set,Y: y_training_set})
    print("\t \t ch_val_Loss: {:.3f}\t ch_val_Acc: {:.2%}".format(check_val_cost,check_val_acc))
    
    print("Learning finished")


