from PIL import Image
import tensorflow as tf

def imageprepare():
    file_name = 'number28_28/5_270_270.png'
    myimage = Image.open(file_name)
    myimage = myimage.resize((28, 28), Image.ANTIALIAS).convert('L')  #变换成28*28像素，并转换成灰度图
    tv = list(myimage.getdata())  # 获取像素值
    tva = [(255-x)*1.0/255.0 for x in tv]  # 转换像素范围到[0 1], 0是纯白 1是纯黑
    return tva

result = imageprepare()
init = tf.global_variables_initializer()
saver = tf.train.Saver

with tf.Session() as sess:
    sess.run(init)
    saver = tf.train.import_meta_graph('minst_cnn_model.ckpt.meta')  # 载入模型结构
    saver.restore(sess,  'minst_cnn_model.ckpt')  # 载入模型参数

    graph = tf.get_default_graph()  # 加载计算图
    x = graph.get_tensor_by_name("x:0")  # 从模型中读取占位符张量
    keep_prob = graph.get_tensor_by_name("keep_prob:0")
    y_conv = graph.get_tensor_by_name("y_conv:0")  # 关键的一句  从模型中读取占位符变量

    prediction = tf.argmax(y_conv, 1)
    predint = prediction.eval(feed_dict={x: [result], keep_prob: 1.0}, session=sess)  # feed_dict输入数据给placeholder占位符
    print(predint[0]) # 打印预测结果
