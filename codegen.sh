#!/usr/bin/env bash
#
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i https://raw.githubusercontent.com/FootprintAI/restcol/refs/heads/main/api/openapiv2/restcol.swagger.json \
    -g python \
    -o /local
