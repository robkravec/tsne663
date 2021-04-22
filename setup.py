from setuptools import setup, find_packages

setup(name='tsne663',
      version='0.2',
      description='Implentation of the t-SNE algorithm for dimension reduction',
      url='https://github.com/robkravec/tsne663',
      author='Marc Brooks, Rob Kravec, Steven Winter',
      author_email='marc.brooks@duke.edu, robert.kravec@duke.edu, steven.winter@duke.edu',
      license='MIT',
      packages=find_packages(), 
      install_requires = ['matplotlib', 'numpy', 'numba', 'tqdm', 'scikit-learn'],
      py_modules = ['tsne', 'sim'])