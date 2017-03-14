# Download Tagoos

~~~
git clone url_with_tagoos_repository /path/to/the/tagoos/source
~~~

# Installation

## Install Tagoos

Finally create a tagoos environment variable to the tagoos folder. In the __.bashrc__, add

~~~
export TAGOOS=/path/to/the/tagoos/source # path to folder with tagoos
~~~

## Install Python packages

~~~
NAME=tagoos
conda create --yes --name $NAME python=3
source activate $NAME
~~~

Install/update packages in conda environment

~~~
cd /path/to/the/tagoos/source
conda install --yes --name $NAME --file spec-file.txt
pip install -r requirements.txt
~~~

