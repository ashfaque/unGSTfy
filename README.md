# Simple application to reverse calculate amount containing GST.

```sh
py -3.9 -m venv env
source env/Scripts/activate
python -m pip install --upgrade pip
python -m pip install "kivy[base]" kivy_examples
# python -m pip install "kivy[sdl2]"
```
[Logo URL](https://cdn.iconscout.com/icon/free/png-256/gst-1795334-1522598.png)

### Build:
```
# https://www.youtube.com/watch?app=desktop&v=cewc02KuHoo

pip install --no-cache-dir opencv-python, pyenchant

pyinstaller --noconfirm --onefile --windowed --icon "E:\\NO_BACKUP\\DjangoProjects\\unGSTfy\\bld\\gst_logo.ico" --name "unGSTfy" "E:\\NO_BACKUP\\DjangoProjects\\unGSTfy\\bld\\unGSTfy.py"

or,

pyinstaller --icon "E:\\NO_BACKUP\\DjangoProjects\\unGSTfy\\bld\\gst_logo.ico" --name "unGSTfy" "E:\\NO_BACKUP\\DjangoProjects\\unGSTfy\\bld\\unGSTfy.py" -w

# Update unGSTfy.spec file.
    from kivy_deps import sdl2, glew    # Add at the top of the file
    a.datas += [(r'Code\ungstfy.kv',r'E:\NO_BACKUP\DjangoProjects\unGSTfy\bld\ungstfy.kv','DATA')]    # Insert this between `pyz = ` and `exe = `.
    , Tree('E:\\NO_BACKUP\\DjangoProjects\\unGSTfy\\bld\\'),    # Add this beside `pyz` of `coll = COLLECT(`
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],    # Add this just after, `a.datas` of `coll = COLLECT(`

# Delete dirs named, build and dist.

pyinstaller unGSTfy.spec -y
```

Use [Inno Setup](https://jrsoftware.org/isdl.php) for one single standalone application, if using multiple images and fonts and files etc.
or, follow this [video](https://www.youtube.com/watch?v=p3tSLatmGvU)

NB: see `~/.kivy\logs` if your application crashes for more info
