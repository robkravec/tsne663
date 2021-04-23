from setuptools import setup, find_packages

setup(name='tsne663',
      version='0.3',
      description='Implentation of the t-SNE algorithm for dimension reduction',
      #long_description = Can add a long description if desired,
      url='https://github.com/robkravec/tsne663',
      author='Marc Brooks, Rob Kravec, Steven Winter',
      author_email='marc.brooks@duke.edu, robert.kravec@duke.edu, steven.winter@duke.edu',
      license='MIT',
      packages=find_packages(), 
      install_requires = ['matplotlib', 'numpy', 'numba', 'tqdm', 'scikit-learn', 'markdown', 'plotly', 'mpl_toolkits', 'textwrap']
     # ,py_modules = ['tsne', 'sim']
     )