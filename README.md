# QGIS GMF Admin Plugin

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE.md)

## Development / testing

Plugin source code is in folder `gmf_admin`.

Recommended development environment is Linux.
You can also use Windows but you'll not have the help of `make` targets.

### Test the plugin with QGIS desktop

#### Linux

```
make link
```

This will create a symbolic link to the plugin source code folder in your home QGIS Python plugins folder.

#### Windows

In QGIS settings, in tab *System* add an environment variable named `QGIS_PLUGINPATH` with as value the path to this folder (git repository root folder).

#### All operating systems

In QGIS desktop extensions manager:

- load plugin `GMF Admin`;
- install QGIS Plugin `Plugin Reloader`.

Now you can easily make changes in source code, reload plugin `gmf_admin` and see changes in QGIS desktop.

### Packaging

```
make package
```

This will create an archive of the plugin in `dist/gmf_admin.zip`

### Test the package archive

```
make deploy
```

This will update the Zip archive (package) and extract files in your home QGIS Python plugins folder.
With this you can test the packaged Zip archive contains all required files.

### List all available make targets

```
make help
```
