from setuptools import setup, find_packages

setup(
    name='compoundwidgets',
    version='0.1.7',
    author='Andre Mariano',
    license="MIT",
    url='https://github.com/AndreMariano100/CompoundWidgets.git',
    description='Compound TTK Widgets with ttkbootstrap',
    author_email='andremariano100@gmail.com',
    packages=['compoundwidgets', 'compoundwidgets.IMAGES'],
    install_requires=['ttkbootstrap', 'Pillow'],
    include_package_data=True,
    package_data={"IMAGES": ["*.png"]},
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
