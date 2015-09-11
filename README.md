This is a collection of files to generate a server package for the
[sinopia](https://github.com/rlidwka/sinopia) node.js module.

Build the sinopia-server RPM with:

```
rpmbuild --define "_topdir `pwd`" -ba sinopia-server.spec
```

The sinopia-server RPM depends on the nodejs-sinopia RPM, which you will most
likely have to build yourself.

Currently this spec only supports sinopia `1.4.0`, you can easily build it with
[fpm](https://github.com/jordansissel/fpm):

```
fpm -s npm -t rpm --depends nodejs --npm-package-name-prefix nodejs sinopia@1.4.0
```
