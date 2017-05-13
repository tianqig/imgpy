from tempfile import TemporaryFile

import pytest
from PIL import ImageFilter

from imgpy import Img


@pytest.mark.parametrize('image', ({
    'sub': 'anima/bordered.gif',
    'mode': 'RGBA',
    'res': 38
}, {
    'sub': 'anima/clear.gif',
    'mode': 'RGBA',
    'res': 12
}, {
    'sub': 'fixed/bordered.jpg',
    'res': 1
}, {
    'sub': 'fixed/clear.jpg',
    'res': 1
}, ))
def test_filter(path, image):
    with Img(fp=path(image['sub'])) as src, TemporaryFile() as tf:
        if 'mode' in image:
            src.convert(image['mode'])

        src.filter(ImageFilter.BLUR)
        src.save(fp=tf)
        with Img(fp=tf) as dest:
            assert dest.n_frames == image['res']
