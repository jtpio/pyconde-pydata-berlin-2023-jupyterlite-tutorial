# Create your JupyterLite website

This tutorial will walk you through the steps to create a JupyterLite website locally with the `jupyter-lite` CLI.

![](https://raw.githubusercontent.com/jupyterlite/jupyterlite/main/docs/_static/icon.svg)

## Deploy on GitHub Pages

If you would like to deploy your JupyterLite website on GitHub Pages, you can follow the following quickstart guide:

https://jupyterlite.readthedocs.io/en/latest/quickstart/index.html

This is likely the easiest to get a JupyterLite up and running in just a couple of minutes, without setting up a development environment.

![Deploy your own](../deploy.gif)

## Using the `jupyter-lite` CLI

![jupyterlite-core CLI](https://user-images.githubusercontent.com/591645/232284263-7aa98589-a599-4f84-bc85-0c8fa799780b.png)

```{note}
Refer to the documentation for more details: https://jupyterlite.readthedocs.io/en/latest/quickstart/standalone.html
```

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

````{note}
As an alternative you can also use the `venv` module from the standard library:

```bash
python -m venv jupyterlite-tutorial
source jupyterlite-tutorial/bin/activate
```
````

### Install the JupyterLite CLI

Install the JupyterLite CLI with:

```bash
# the jupyterlab-server dependency will be needed later
mamba install -c conda-forge jupyterlite-core jupyterlab-server
```

You can also use `pip`:

```bash
pip install "jupyterlite-core[lab]"
```

The `[lab]` extra (or the `jupyterlab-server` dependency) installs additional dependencies for content and localization.

### Get an empty JupyterLite website

Create an empty JupyterLite website with:

```bash
jupyter lite init
```

By default, this will create a new folder `_output` with the minimal content of the JupyterLite website. You can check the content of the folder with the following command:

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

```{warning}
By default `jupyterlite-core` does not include any kernel.
We will see how to add one in the next section.
```

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

```{note}
Refer to the documentation for more details: https://jupyterlite.readthedocs.io/en/latest/howto/configure/kernels.html
```

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

```{note}
Refer to the documentation for more details: https://jupyterlite.readthedocs.io/en/latest/howto/index.html#contents
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

```{note}
Refer to the documentation for more details: https://jupyterlite.readthedocs.io/en/latest/howto/configure/simple_extensions.html
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

```{note}
As a reminder we have been using the `jupyterlite-xeus-python` package to add a Python kernel to our JupyterLite website.
This section is for installing extra Python packages for that particular kernel.
We will see below how to install extra Python packages for the Pyodide kernel.
```

TODO

```{note}
Refer to the documentation for more details: https://jupyterlite.readthedocs.io/en/latest/howto/xeus-python/preinstalled_packages.html
```

## Voici: from Jupyter Notebook into a static web application

![voila](https://raw.githubusercontent.com/voila-dashboards/voila/main/docs/source/voila-logo.svg)

Install Voici with `pip`:

```bash
pip install voici
```

Then use the `voici` command to create a static website. In this case we also include the other JupyterLab and Notebook interfaces so they are still available:

```bash
voici build --contents notebooks --apps jupyterlab --apps retro
```

### Templates

You can use different templates for your Voici application.

Templates can modify the layout and the appearance of your Voici application. Here are a few template examples:

- [Voila Material](https://github.com/voila-dashboards/voila-material): Material design template for Voilà
- [Voila GridStack](https://github.com/voila-dashboards/voila-gridstack): Dashboard template for Voilà based on GridStackJS

These templates were originally developed for Voilà, but they can also be used with Voici.

To install a template, you can use the `pip` command:

```bash
pip install voila-material
```

You can also add the template to your dependencies in the `environment.yml` file:

```yaml
dependencies:
  - voila-material
```

Once the template is installed, you can use it by specifying the `--template` option when building your Voici application:

```bash
voici build --template voila-material
```

Here is what a Voici dashboard looks like with the Material template:

![a screenshot showing a Voici dashboard with the Material template](https://user-images.githubusercontent.com/591645/231569683-7df59ff8-239e-4dee-ad15-3208e0b9c761.png)

### Themes

You can also use different themes for your Voici application.

To use the Dark theme, you can use the `--theme` option when building your Voici application:

```bash
voici build --theme dark
```

You can also the `?theme` query parameter to choose the theme while accessing the dashboard. For example:

```text
https://you-voici-deployment.example.com/voici/render/voici.html?theme=dark
```

## Additional Configuration

Voici supports additional configuration provided by JupyterLite, such as using custom extensions and settings.

You can refer to the [JupyterLite documentation](https://jupyterlite.readthedocs.io/en/latest/howto/index.html) for more information.

```{warning}
Some configuration options might not supported yet.
Please don't hesitate to open an issue on the [Voici repository](https://github.com/voila-dashboards/voici)
if you would like to use an option not supported by Voici yet.
```


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

