from setuptools import setup

package_name = 'my_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nsy',
    maintainer_email='sktpdud819@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simplepub = my_pkg.simplepublisher:main',
            'simplesub = my_pkg.simplepusubscriber:main',
            'simpletimepub = my_pkg.simpletimepublisher:main',
            'simpletimesub = my_pkg.simpletimesubscriber:main',
            'messagepub = my_pkg.messagepublisher:main',
            'messagesub1 = my_pkg.messagesubscriber1:main',
            'messagesub2 = my_pkg.messagesubscriber2:main',
            'messagetimesub = my_pkg.messageTimeSubscriber:main'
        ],
    },
)
