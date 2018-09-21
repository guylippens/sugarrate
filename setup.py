from distutils.core import setup

setup(
    name='SugarRate',
    version='0.1dev',
    packages=['sugarrate', ],
    license='GNU Lesser General Public License version 3',
    long_description=open('README.md').read(),
    install_requires=['numpy', ]
)
