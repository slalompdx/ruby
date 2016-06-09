docker build -t dev6 -f Dockerfile.prep-dev6 .
docker build -t prep6 -f Dockerfile.prep6 .
docker build -t el6 -f Dockerfile.el6 .
docker run -v ~/uproj/ruby/build:/build -it el6
