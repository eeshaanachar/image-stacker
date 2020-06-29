try:
    import numpy as np
    from concurrent.futures import ThreadPoolExecutor
    from cv2 import imread, imwrite
    from os import listdir

    files = ['exposures/' + file for file in listdir('exposures')]

    with ThreadPoolExecutor() as executor:
        images = list(executor.map(imread, files))

    image_mean = np.mean(np.array(images), axis=0)

    vfunc = np.vectorize(lambda x: int(round(x)))
    result = vfunc(image_mean)

    imwrite(files[0].split('/')[1], result)

except Exception as message:
    input(message)
