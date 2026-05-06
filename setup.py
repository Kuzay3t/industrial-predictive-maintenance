from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="industrial-predictive-maintenance",
    version="0.1.0",
    author="Kuzay3t",
    description="AI-powered predictive maintenance system for industrial rotating machinery",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kuzay3t/industrial-predictive-maintenance",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.10",
    install_requires=[
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "scikit-learn>=1.3.0",
        "xgboost>=2.0.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "shap>=0.42.0",
        "jupyter>=1.0.0",
        "ipython>=8.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "flake8>=6.0.0",
            "bandit>=1.7.0",
        ],
    },
)
