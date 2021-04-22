from setuptools import setup

setup(name='tsne663',
      version='0.1',
      description='Implentation of the t-SNE algorithm for dimension reduction',
      url='https://github.com/robkravec/tsne663',
      author='Marc Brooks, Rob Kravec, Steven Winter',
      author_email='marc.brooks@duke.edu, robert.kravec@duke.edu, steven.winter@duke.edu',
      license='MIT',
      packages=setuptools.find_packages(), 
      install_requires = ['<matplotlib>', '<numpy>', '<numba>', '<tqdm>', '<sklearn>'],
      py_modules = ['tsne', 'sim'])