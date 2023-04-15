# Create your JupyterLite website

This tutorial will walk you through the steps to create a JupyterLite website locally with the `jupyter-lite` CLI.

## Deploy on GitHub Pages

If you would like to deploy your JupyterLite website on GitHub Pages, you can follow the following quickstart guide:

https://jupyterlite.readthedocs.io/en/latest/quickstart/index.html

This is likely the easiest to get a JupyterLite up and running in just a couple of minutes, without setting up a development environment.

## Using the `jupyter-lite` CLI

### Create a new virtual environment

We recommend using mamba to create a new virtual environment:

If you don't have mamba installed, you can install it with for MacOS and Linux:

```bash
curl micro.mamba.pm/install.sh | bash
```

Or check the documentation for more details: https://mamba.readthedocs.io/en/latest/installation.html#micromamba

```bash
mamba create -n jupyterlite-tutorial -c conda-forge python=3.11 -y
mamba activate
```

For the rest of the tutorial, make sure you are in the `jupyterlite-tutorial` environment.

As an alternative you can also use the `venv` module from the standard library:

```bash
python -m venv jupyterlite-tutorial
source jupyterlite-tutorial/bin/activate
```

### Install the JupyterLite CLI

Then you can install the JupyterLite CLI with:

```bash
pip install "jupyterlite-core[lab]"
```

You can also use `mamba` to install the packages:

```bash
# the jupyterlab-server dependency will be needed later
mamba install -c conda-forge jupyterlite-core jupyterlab-server
```

The [lab] extra (or the `jupyterlab-server` dependency) installs additional dependencies for content and localization.

### Get an empty JupyterLite website

You can create an empty JupyterLite website with:

```bash
jupyter lite init
```

By default, this will create a new folder `_output` with the minimal content of the JupyterLite website. You can check the content with the following command:

```bash
ls _output
```

This should give something like the following:

```bash
bootstrap.js      index.html                  manifest.webmanifest
build             jupyter-lite.ipynb          package.json
config-utils.js   jupyter-lite.json           repl
doc               jupyterlite.schema.v0.json  retro
icon-120x120.png  kernelspecs                 service-worker-b2fb40a.js
icon-512x512.png  lab                         tree
```

### Serve the website locally

You can serve the website locally with:

```bash
jupyter lite serve
```

By default `jupyterlite-core` does not include any kernel.

As an alternative you can also start a Python server with:

```bash
python -m http.server 8000 --directory _output
```

### Add a kernel

To add a Python kernel to your JupyterLite website, you can install the `jupyterlite-xeus-python` package:

```bash
pip install jupyterlite-xeus-python
```

Then rebuild the website with:

```bash
jupyter lite build
```

It should now be possible to run a Python notebook in your JupyterLite website.

### Adding content

Then let's create a new folder to store the notebooks:

```bash
mkdir notebooks
```

Create a new notebook in the `notebooks` folder, and add other files you would like to include in your website.

Then rebuild the website with:

```bash
jupyter lite build --content notebooks
```

### Adding extensions

You can also add JupyterLab extensions to your JupyterLite website.

For example, you can install the `jupyterlab-execute-time` extension with:

```bash
pip install jupyterlab-execute-time
```

Or even a custom theme:

```bash
pip install jupyterlab-night
```

Then rebuild the website with:

```bash
jupyter lite build
```

### Localization and display languages

It's also possible to localize the JupyterLite website so it's available in different languages.

For example, you can install the `jupyterlab-language-pack-fr-FR` package with:

```bash
pip install jupyterlab-language-pack-fr-FR
```

Then rebuild the website with:

```bash
jupyter lite build
```

### The `jupyter_lite_config.json` file

The `jupyter_lite_config.json` file contains the configuration to build a JupyterLite website.

This file is picked up automatically when running the `jupyter lite build` command.

TODO

### Installing extra Python packages

TODO

## Voici: from Jupyter Notebook into a static web application

Install Voici with pip:

```bash
pip install voici
```

Then use the `voici` command to create a static website. In this case we also include the other JupyterLab and Notebook interfaces so they are still available:

```bash
voici build --contents notebooks --apps jupyterlab --apps retro
```

### Themes

TODO

### Templates

TODO

### Adding Voici options to the `jupyter_lite_config.json` file

You can also provide the Voici options in the `jupyter_lite_config.json` file instead of using the command line:

```json
{
  "VoilaConfiguration": {
    "theme": "dark",
    "template": "material"
  }
}
```

## Extras

### Using the Pyodide kernel

With the Pyodide kernel you can install extra Python packages:

https://jupyterlite.readthedocs.io/en/latest/howto/pyodide/packages.html

