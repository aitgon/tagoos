# Build the documentation

Run this command and open __$PWD/docs/manual.html__ in a browser

~~~
pandoc -s -S --toc -c buttondown.css $PWD/docs/*.md >$PWD/docs/manual.html
~~~

