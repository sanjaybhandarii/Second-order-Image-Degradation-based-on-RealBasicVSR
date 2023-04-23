# Second-order-Image-Degradation-based-on-RealBasicVSR
based on [RealESRGAN](https://arxiv.org/abs/2107.10833) by Xintao Wang, Liangbin Xie, Chao Dong, Ying Shan

## Description


This project is aimed at simulating second-order image degradation and converting high-quality images to low-quality noisy images using algorithm stated by RealBasicVSR paper. The motivation behind this project is to better understand the process of image degradation and the factors that affect image quality.

This project is built as a learning exercise to gain a deeper understanding of image processing and computer vision techniques. By working on this project, I was able to explore and experiment with different algorithms and techniques for image degradation and restoration.

The problem that this project solves is the simulation of second-order image degradation, which is a common problem in image processing. By converting high-quality images to low-quality noisy images, this project provides a realistic simulation of image degradation in real life, which can be useful for testing and validating Image/Video Super-Resolution/Upsampling algorithms.



## Installation


1. Clone the repository:

   ```shell
   git clone https://github.com/sanjaybhandarii/Second-order-Image-Degradation-based-on-RealBasicVSR
   ```
2. Requirement:

    The requirements are listed in requirements.txt.
    To install the requirements:

    ```shell
    pip install requirements.txt
    ```

## Usage

    High Resolution Image:

    <p align="center"><img src="./assets/hr/a.jpg" width="400"/></p>

    Low Resolution Image:

    <p align="center"><img src="./assets/to/a.jpg" width="400"/></p>

    Give the locations of HR(High Resolution) images and locations to save your degraded image in main.py.
    Then,To run the project code:

    ```shell
    python main.py
    ```

## Credits

1. [BasicSR](https://basicsr.readthedocs.io/en/latest/_modules/basicsr/data/degradations.html)
2. [RealESRGAN](https://arxiv.org/abs/2107.10833)
