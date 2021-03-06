#!/usr/bin/env python2.7
from __future__ import absolute_import, division, print_function
#import os
#import sys
# hack
#sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
#sys.path.append(os.getcwd())
import utool as ut
import matplotlib as mpl
from matplotlib import pyplot as plt


def test_detect_then_show(ax, img_fpath):
    import pyhesaff
    kpts, vecs = pyhesaff.detect_feats(img_fpath)
    print('[test_detect_then_show]')
    print('img_fpath=%r' % img_fpath)
    print('kpts=%s' % (ut.truncate_str(repr(kpts)),))
    print('vecs=%s' % (ut.truncate_str(repr(vecs)),))
    assert len(kpts) == len(vecs)
    assert len(kpts) > 0, 'no keypoints were detected!'
    img = mpl.image.imread(img_fpath)
    plt.imshow(img)
    _xs, _ys = kpts.T[0:2]
    ax.plot(_xs, _ys, 'ro', alpha=.5)


def simple_iterative_test():
    r"""
    CommandLine:
        python -m pyhesaff.tests.test_pyhesaff_simple_iterative --test-simple_iterative_test
        python -m pyhesaff.tests.test_pyhesaff_simple_iterative --test-simple_iterative_test --show

    Example:
        >>> # GUI_DOCTEST
        >>> from pyhesaff.tests.test_pyhesaff_simple_iterative import *  # NOQA
        >>> result = simple_iterative_test()
        >>> print(result)
        >>> ut.show_if_requested()
    """
    lena_fpath  = ut.grab_test_imgpath('lena.png')
    carl_fpath  = ut.grab_test_imgpath('carl.jpg')
    grace_fpath = ut.grab_test_imgpath('grace.jpg')
    ada_fpath   = ut.grab_test_imgpath('ada.jpg')

    fig = plt.figure()
    ax = fig.add_subplot(2, 2, 1)
    test_detect_then_show(ax, lena_fpath)

    ax = fig.add_subplot(2, 2, 2)
    test_detect_then_show(ax, carl_fpath)

    ax = fig.add_subplot(2, 2, 3)
    test_detect_then_show(ax, grace_fpath)

    ax = fig.add_subplot(2, 2, 4)
    test_detect_then_show(ax, ada_fpath)


if __name__ == '__main__':
    """
    CommandLine:
        python -m pyhesaff.tests.test_pyhesaff_simple_iterative
        python -m pyhesaff.tests.test_pyhesaff_simple_iterative --allexamples
        python -m pyhesaff.tests.test_pyhesaff_simple_iterative --allexamples --noface --nosrc
    """
    import multiprocessing
    multiprocessing.freeze_support()  # for win32
    import utool as ut  # NOQA
    ut.doctest_funcs()
