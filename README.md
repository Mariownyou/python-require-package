# python-require: Provides one-time installation of Python package
python-require allows for one-time installation of a Python package. It is particularly useful for prototyping, where you need to quickly install a package and use it in your code but you don't want to bloat your environment. Inspired by npx and pipx

It's worth noting that packages installed by python-require are automatically deleted after the script finishes running. This means that the package will not persist in your development environment, and will need to be re-installed the next time you run your script. This behavior is intentional, as it helps prevent conflicts between different versions of packages that may be installed in your environment.


## Installation
```bash
pip install require-package
```


## Usage
```python
from require_package import require

# Install a package
requests = require("requests")
r = requests.get("https://google.com")
print(r.status_code)
```


## Caveats
python-require is not a package manager. It is a tool for prototyping. It is not meant to be used in production.
Additionally, Python-Require may not work properly in all environments. In particular, it may have trouble installing packages in virtual environments with non-standard configurations. Use at your own risk!


## License

[MIT License](./LICENSE.txt)
