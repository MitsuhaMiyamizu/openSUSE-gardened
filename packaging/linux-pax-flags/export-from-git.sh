#!/bin/sh -x

dir="$1"

if ! [ -d "$dir" ]; then
	echo "Usage: $0 <gitdir>"
	exit 1
fi

here=`pwd`
name=linux-pax-flags

cd $dir
git archive --format=tar --prefix=$name/ HEAD | bzip2 --best > $here/$name.tar.bz2
