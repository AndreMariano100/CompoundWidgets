from setuptools import setup

setup(
    name='compoundwidgets',
    version='0.3.10',
    author='Andre Mariano',
    author_email='andremariano100@gmail.com',
    url='https://github.com/AndreMariano100/CompoundWidgets.git',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license="MIT",
    description='Compound TTK Widgets with ttkbootstrap',
    packages=['compoundwidgets', 'compoundwidgets.IMAGES'],
    install_requires=['ttkbootstrap', 'Pillow'],
    include_package_data=True,
    package_data={"IMAGES": ["*.png"]},
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
