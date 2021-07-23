# Tutorials site for Kevrekidis Lab

Templates require python3.6+ to run. On Linux, and assuming you have `python3.7` in your `PATH`, you can use virtualenvwrapper to [make an environment](https://www.geeksforgeeks.org/using-mkvirtualenv-to-create-new-virtual-environment-python/) like this:


```bash
mkvirtualenv --python=`which python3.7` kevrekidislab.github.io
```

this should make and activate the environment. You can then install requirements to build the site like this:

```bash
pip install -r requirements.txt
```

You can now generate the site with 
```bash
bash generate_html.sh
```

and now open `index.html` in a browser to see the updated site locally.

If you're the site maintainer, you can configure the (public) site repo as an upstream remote like this (done only once for your local clone):
```bash
git remote add upstream git@github.com:kevrekidislab/kevrekidislab.github.io.git
```

Then, every time you're ready to push changes to the live site, you do
```bash
git push upstream
```
(Compare this to how you push to your own (private) fork, with just `git push`, or maybe `git push origin` or `git push origin master`.)