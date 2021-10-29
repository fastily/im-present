import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="im-present",
    version="0.0.1",
    author="Fastily",
    author_email="fastily@users.noreply.github.com",
    description="Peridoically shake the mouse pointer to prove you're present",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fastily/im-present",
    project_urls={
        "Bug Tracker": "https://github.com/fastily/im-present/issues",
    },
    include_package_data=True,
    packages=setuptools.find_packages(include=["present", "rich"]),
    install_requires=['pyautogui'],
    entry_points={
        'console_scripts': [
            'present = present.__main__:_main'
        ]
    },
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
