from setuptools import setup

setup(
    name='compoundwidgets',
    version='0.1.6',
    author='Andre Mariano',
    license="MIT",
    url='https://github.com/AndreMariano100/CompoundWidgets.git',
    description='Compound TTK Widgets with ttkbootstrap',
    author_email='andremariano100@gmail.com',
    packages=['compoundwidgets'],
    install_requires=['ttkbootstrap', 'Pillow'],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)