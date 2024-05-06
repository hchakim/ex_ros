import os # launch 파일 추가를 위해
from glob import glob # launch 파일 추가를 위해

from setuptools import setup

package_name = 'py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        #여기에 런치 파일에 대한 설명을 추가함
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hk',
    maintainer_email='hk@todo.todo',
    description='My Package description',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = py_pubsub.publisher_member_function:main',    #실행 위치
            'listener = py_pubsub.subscriber_member_function:main', #실행 위치
        ],
    },
)
