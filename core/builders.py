#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""Model and loss construction functions."""

from core.config import cfg 
from core.net import SoftCrossEntropyLoss
from models.resnet import ResNet
from models.anynet import AnyNet
from models.effnet_v1 import EffNet_V1
from models.regnet import RegNet
from models.mobilenetv3_small import MobileNetV3_S
from models.mobilenetv3_large import MobileNetV3_L
from models.shufflenetv2 import ShuffleNet_V2
from models.effnet_v2 import EffNet_V2


# Supported models:
_models = {"anynet": AnyNet, "effnet_v1": EffNet_V1, "resnet": ResNet, "regnet": RegNet,
            "mobilenetv3_small":MobileNetV3_S,"mobilenetv3_large":MobileNetV3_L,
            "shufflenetv2":ShuffleNet_V2,"effnet_v2":EffNet_V2,}

# Supported loss functions   
_loss_funs={"cross_entropy": SoftCrossEntropyLoss}

def get_model():
    """Gets the model class specified in the config."""
    err_str="Model type '{}' not supported"
    assert cfg.MODEL.TYPE in _models.keys(), err_str.format(cfg.MODEL.TYPE)
    return _models[cfg.MODEL.TYPE]

def get_loss_fun():
    """Gets the loss function class specified in the config."""
    err_str = "Loss function type '{}' not supported"
    assert cfg.MODEL.LOSS_FUN in _loss_funs.keys(), err_str.format(cfg.TRAIN.LOSS)
    return _loss_funs[cfg.MODEL.LOSS_FUN]


def build_model():
    """Builds the model."""
    return get_model()()


def build_loss_fun():
    """Build the loss function."""
    return get_loss_fun()()


def register_model(name, ctor):
    """Registers a model dynamically."""
    _models[name] = ctor


def register_loss_fun(name, ctor):
    """Registers a loss function dynamically."""
    _loss_funs[name] = ctor

