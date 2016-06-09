docker build -t dev7 -f Dockerfile.prep-dev7 .
docker build -t prep7 -f Dockerfile.prep7 .
docker build -t el7 -f Dockerfile.el7 .
docker run -v ~/uproj/ruby/build:/build -it el7
