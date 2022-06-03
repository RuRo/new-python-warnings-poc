#!/bin/sh

docker run \
    --volume "$PWD:/long/path/to/code/that/may/end/up/wrapping/" \
    --workdir "/long/path/to/code/that/may/end/up/wrapping/" \
    -it python:3.11.0b1-slim \
    ./compare_warnings.sh
