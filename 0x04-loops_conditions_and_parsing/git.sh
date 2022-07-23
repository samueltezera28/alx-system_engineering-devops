#!/bin/bash
chmod u+x *
git add --chmod+=x *
echo "commit message"
read msg
git commit -m $msg
git push
