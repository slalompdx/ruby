docker build -t dev7 -f Dockerfile.prep-dev7 .
docker build -t prep7 -f Dockerfile.prep7 .
docker build -t el7 -f Dockerfile.el7 .
mkdir -p build/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
cp ruby-el7.spec build/SPECS
wget https://cache.ruby-lang.org/pub/ruby/2.3/ruby-2.3.1.tar.gz -O ./build/SOURCES/ruby-2.3.1.tar.gz
docker run -v ~/uproj/ruby/build:/build -it el7
