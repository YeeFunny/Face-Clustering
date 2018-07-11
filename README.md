# Face-Clustering

This is a Chinese Whispers implementation of the face clustering based on FaceNet ["FaceNet: A Unified Embedding for Face Recognition and Clustering"](http://arxiv.org/abs/1503.03832).

## Compatibility
The code is tested with Python 3.5. The test results can be found in data/cluster_result.

##Pre-trained models
| Model name      | LFW accuracy | Training dataset | Architecture |
|-----------------|--------------|------------------|-------------|
| [20180408-102900](https://drive.google.com/open?id=1R77HmFADxe87GmoLwzfgMu_HY0IhcyBz) | 0.9905        | CASIA-WebFace    | [Inception ResNet v1](https://github.com/davidsandberg/facenet/blob/master/src/models/inception_resnet_v1.py) |
| [20180402-114759](https://drive.google.com/open?id=1EXPBSXwTaqrSC0OhUdXNmKSh9qJUQ55-) | 0.9965        | VGGFace2      | [Inception ResNet v1](https://github.com/davidsandberg/facenet/blob/master/src/models/inception_resnet_v1.py) |
| [20170511-185253](https://drive.google.com/open?id=1b0_w4Z7F7UONWWF69MHXjM9x4it1hJp_) | 0.9920        | MS-Celeb-1M      | [Inception ResNet v1](https://github.com/davidsandberg/facenet/blob/master/src/models/inception_resnet_v1.py) |

##Usage

Clone the FaceNet [repo](https://github.com/davidsandberg/facenet).
	Using CLI
	$ git clone https://github.com/davidsandberg/facenet.git

Set the python paths
	Set the environment variable PYTHONPATH to point to the src directory of the cloned repo. [...] should be replaced with the directory where the cloned facenet repo resides.
	
	$ export PYTHONPATH=[...]/facenet/src
	
