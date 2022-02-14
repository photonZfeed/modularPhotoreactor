from distutils.core import setup

setup(
    name='mod_reactor_controller',
    version='1.1.0',
    url='',
    license='',
    author='Daniel Kowalczyk, Dirk Ziegenbalg',
    author_email='dirk.ziegenbalg@uni-ulm.de',
    description='Package to control the modular reactor.',
    packages=['mod_reactor_controller'],
    package_data={'mod_reactor_controller': ['conf/*.conf']},
    zip_safe=False,
    install_requires=['future',
                      'six',
                      'tinkerforge',
                      'simple_pid',
                      'configparser',
                      'future',
                      'pyserial']
)
