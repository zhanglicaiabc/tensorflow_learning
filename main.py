from build_model import *
from cifar10_cnn_cap_attack import *
from mnist_cnn_cap_process import *
from mnist_fnn_cap_attack import *
import tensorflow as tf
from cifar10_cnn_cap_defend import *
from cifar10_cnn_cap_attack_enhance import *
import os
from mnist_fnn_linear_attack import *
from mnist_cnn_linear_attack import *
from cifar10_cnn import *

# os.environ["CUDA_VISIBLE_DEVICES"] = "0"

if __name__ == '__main__':

    # tf.random.set_seed(124)
    gpu_options = tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.85)
    config = tf.compat.v1.ConfigProto(gpu_options=gpu_options)
    session = tf.compat.v1.Session(config=config)
    # mnist训练


    # mnist fnn 线性权重惩罚项攻击
    model, optimizer = build_mnist_fnn_model()
    mnist_linear_attack_train(model, optimizer)

    # mnist cnn 线性权重惩罚项攻击
    # model, optimizer = build_mnist_cnn_model()
    # mnist_cap_cnn_train(model, optimizer)

    # 黑盒CAP攻击
    # mnist_cap_fnn_train(model, optimizer)

    # cifar10训练
    # train_db, test_db = load('cifar10')

    # conv_net, fc_net, optimizer2 = build_vgg13_model(0.0001)

    # train_cifar10(conv_net, fc_net, optimizer2)
    # cifar10_cnn_cap_enhance_attack(conv_net, fc_net, optimizer2)
