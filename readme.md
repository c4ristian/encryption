# encryption

## What is it?
This Python library provides experiments with quantum-resistant algorithms 
such as [AES-256](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) 
and [Kyber](https://pq-crystals.org/kyber/software.shtml). Key results are documented in this 
[article](https://towardsdatascience.com/post-quantum-cryptography-with-python-and-linux-17b1ca1b3e1).

## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/c4ristian/encryption

## Setup
```sh
conda env create -f environment.yml

conda activate encryption
```

## Jupyter
### Install Kernel 
```sh
python -m ipykernel install --user --name=encryption
```

### Run Notebooks
```sh
jupyter notebook --notebook-dir="./notebooks"
```

## License
[Apache 2.0](LICENSE.txt)

## Disclaimer
Code provided in this repository is prototypical and not intended for production use.
In accordance with the license, there is no warranty for the published content.

## Contact us
[christian.koch@th-nuernberg.de](mailto:christian.koch@th-nuernberg.de)
