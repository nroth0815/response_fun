from setuptools import setup

setup(name='test_pack',
      version='0.1',
      description='Some random tests',
      url='http://github.com/nroth0815/response_fun',
      author='Nina Roth',
      author_email='nrmailfwd@gmail.com',
      license='MIT',
      packages=['test_pack'],
      #dependency_links=['http://github.com/pynbody/pynbody.git'], #requires the lastest version, not sure about syntax
      install_requires=['pynbody', 'numpy'], #any package known to pip
      zip_safe=False)
