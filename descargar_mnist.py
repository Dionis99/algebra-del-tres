#!/usr/bin/env python3
"""
Descarga MNIST desde la fuente oficial y guarda los arrays en .npz
"""

import os
import gzip
import urllib.request
import numpy as np

# URLs de MNIST (formato IDX)
BASE_URL = "http://yann.lecun.com/exdb/mnist/"
FILES = [
    ("train-images-idx3-ubyte.gz", "train_images.npy"),
    ("train-labels-idx1-ubyte.gz", "train_labels.npy"),
    ("t10k-images-idx3-ubyte.gz", "test_images.npy"),
    ("t10k-labels-idx1-ubyte.gz", "test_labels.npy"),
]

def descargar(url, destino):
    if not os.path.exists(destino):
        print(f"Descargando {url} ...")
        urllib.request.urlretrieve(url, destino)
        print("Descargado.")
    else:
        print(f"Ya existe {destino}, omitiendo descarga.")

def leer_imagenes(ruta_gz):
    with gzip.open(ruta_gz, 'rb') as f:
        data = f.read()
    # El header son 16 bytes: magic(4), num_images(4), rows(4), cols(4)
    magic, num, rows, cols = np.frombuffer(data[:16], dtype='>i4')
    imgs = np.frombuffer(data[16:], dtype=np.uint8).reshape(num, rows, cols)
    return imgs

def leer_etiquetas(ruta_gz):
    with gzip.open(ruta_gz, 'rb') as f:
        data = f.read()
    magic, num = np.frombuffer(data[:8], dtype='>i4')
    labs = np.frombuffer(data[8:], dtype=np.uint8)
    return labs

def main():
    # Descargar archivos si no están
    for url_suffix, _ in FILES:
        url = BASE_URL + url_suffix
        descargar(url, url_suffix)

    print("Convirtiendo imágenes y etiquetas...")
    train_imgs = leer_imagenes(FILES[0][0])
    train_labs = leer_etiquetas(FILES[1][0])
    test_imgs  = leer_imagenes(FILES[2][0])
    test_labs  = leer_etiquetas(FILES[3][0])

    print(f"Train: {train_imgs.shape[0]} imágenes, {train_imgs.shape[1]}x{train_imgs.shape[2]}")
    print(f"Test:  {test_imgs.shape[0]} imágenes, {test_imgs.shape[1]}x{test_imgs.shape[2]}")

    # Guardar como .npz comprimido
    np.savez_compressed(
        "mnist_data.npz",
        x_train=train_imgs, y_train=train_labs,
        x_test=test_imgs,   y_test=test_labs
    )
    print("Datos guardados en mnist_data.npz")

if __name__ == "__main__":
    main()
