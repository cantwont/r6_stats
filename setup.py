from setuptools import setup

setup(
    name="r6_stats",
    version="1.0.2",
    packages=["r6_stats"],
    install_requires=["requests", "beautifulsoup4", "lxml"],
    description="Python package to retreive player stats from the game Rainbow 6: Siege",
    long_description="Python package to retreive player stats from the game Rainbow 6: Siege"
)
