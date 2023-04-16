---
marp: true
---


# Create interactive Jupyter websites with JupyterLite 💡

![bg fit right:33%](https://raw.githubusercontent.com/jupyterlite/jupyterlite/main/docs/_static/icon.svg)

## 🐍 PyConDE & PyData Berlin 2023 🐍

### 2023-04-19

#### Jeremy Tuloup


---

# How is JupyterLite different compared to normal Jupyter? 🤔

---

# Boots in seconds

![height:600px](https://user-images.githubusercontent.com/591645/120649478-18258400-c47d-11eb-80e5-185e52ff2702.gif)

---

# The `jupyter-lite` CLI is a **Static Site Generator** (SSG)

```shell
pip install jupyterlite-core
```

---


# Lightweight Jupyter Frontend running in the browser

![width:512](https://raw.githubusercontent.com/jupyterlite/jupyterlite/main/docs/_static/badge-launch.svg)

- ✅ no server
- ✅ no command line
- ✅ no need to install Python and other packages locally


---

# Easy to deploy

- Documentation: https://jupyterlite.readthedocs.io/en/latest/deploying.html
- Served via well-cacheable, static HTTP(S), locally or on most static web hosts

---

# Examples

- https://jupyterlite.rtfd.io/en/latest/try/lab (Read The Docs)
- https://jupyterlite.github.io/demo (GitHub Pages)
- ![width:128](https://user-images.githubusercontent.com/591645/120675034-00f29080-c495-11eb-928c-26bb94e8eb68.png)
- ![width:128](https://user-images.githubusercontent.com/591645/120676545-6dba5a80-c496-11eb-9b2b-604e92c3429b.png)
- ![width:128](https://user-images.githubusercontent.com/591645/120675516-6f375300-c495-11eb-819c-d6f1fb3cb0f1.png)
- ![width:128](https://user-images.githubusercontent.com/591645/120676108-03a1b580-c496-11eb-8990-ed30c7861376.png)
- ![width:128](https://user-images.githubusercontent.com/591645/120676313-2df37300-c496-11eb-8639-25e2fc606850.png)
- And more: Netlify, nginx, Heroku...

---

# Standing on the shoulders of giants 💁‍♂️

-  Built from the ground-up using JupyterLab components and extensions
- The frontend communicates to the in-browser kernels via the Jupyter Protocol

![height:400px](https://user-images.githubusercontent.com/591645/162748538-e44fea00-f727-4055-b795-8f5fc5c6b133.png)

---

#  Wasm powered Jupyter running in the browser 💡

- https://developer.mozilla.org/en-US/docs/WebAssembly

![height:400px](https://user-images.githubusercontent.com/591645/162831191-16956085-783a-435e-b810-0d25da1379b3.png)

---

# Interactive Computing in the browser

- Python kernels:
  - Pyodide
  - Xeus Python
- Visualizations:
   - matplotlib
   - ipywidgets
   - plotly

---

# Embed a live Python console on your website 🚀

![height:300px](https://user-images.githubusercontent.com/591645/162619390-ecab994a-3f39-4e26-af78-ca2569aee9b2.png)

Embed with:

```html
<iframe
  src="https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1"
  width="100%"
  height="500px"
>
</iframe>
```

---

# [numpy.org](https://numpy.org)

![image](https://user-images.githubusercontent.com/591645/162569443-40e841ad-f42d-44eb-966f-c1c810c1ab10.png)

---

# [sympy.org](https://sympy.org)

![height:500px](https://user-images.githubusercontent.com/591645/167361691-da1252e7-17f4-4bbf-8eee-ba3bfaff8c2e.png)

---

# [try.jupyter.org](https://try.jupyter.org)

-️ Help reduce the load on [mybinder.org](https://mybinder.org)
-️ Huge savings: trade compute resources (1 GB / 1 CPU) for static assets

![height:500px](https://user-images.githubusercontent.com/591645/162569510-56287b4b-acf2-47f9-90af-7b0605c5b112.png)

---

# [jupyterlite-sphinx](https://jupyterlite-sphinx.readthedocs.io/en/latest/)

![height:500px](https://user-images.githubusercontent.com/591645/162838828-d6407725-15d9-4640-8aa6-c8c8979a9a3f.png)

---

# Strengths

- Easy to deploy
- Simpler for users (no need to install Python and other packages locally)
- Educational use cases
- Reproducibility time capsule

---

# Limitations

- Suited for lighter workloads
- Not all packages are available (or ever will be)
- Subset of Python running in the browser
- Initial asset download can be big (~30MB), then cached by the browser

---

# In this tutorial

- Quickstart with the demo repository
- Adding content: notebooks, files and static assets
- Adding extensions to the user interface
- Adding packages to the Python runtime
- Customization and custom settings
