docker build -t dev6 -f Dockerfile.prep-dev6 .
docker build -t prep6 -f Dockerfile.prep6 .
docker build -t el6 -f Dockerfile.el6 .
mkdir -p build/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
cp ruby-el6.spec build/SPECS
wget https://cache.ruby-lang.org/pub/ruby/2.3/ruby-2.3.1.tar.gz -O ./build/SOURCES/ruby-2.3.1.tar.gz
docker run -v ~/uproj/ruby/build:/build -it el6
