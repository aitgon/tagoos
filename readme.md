# Install

Create environment conda

~~~
NAME=tagoos
conda create --yes --name $NAME python=3
source activate $NAME
~~~

Install/update packages in conda environment

~~~
conda install --yes --name $NAME --file spec-file.txt
pip install -r requirements.txt
~~~

Finally create a tagoos environment variable to the tagoos folder. In the bashrc, add

~~~
export TAGOOS=$HOME/Software/repositories/tagoos
~~~

# Build the documentation

Run this command and open __$PWD/docs/manual.html__ in a browser

~~~
pandoc -s -S --toc -c buttondown.css $PWD/docs/*.md >$PWD/docs/manual.html
~~~

## Bug

For this error message:

~~~
python: /lib64/libc.so.6: version `GLIBC_2.14' not found
~~~

Fix it like this:

~~~
cd $HOME/Software/miniconda3/envs/tagoos/lib
rm libstdc++.so.6
ln -s $HOME/Software/prefix/lib64/libstdc++.so.6
cd $OLDPWD
~~~

