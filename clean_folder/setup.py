import setuptools

setuptools.setup(name='clean_folder',
                 
      description='clean folder',
      author='pavlov nikita',
      packages= setuptools.find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder=clean_folder.clean:main']})
