#!/bin/sh

force=false

[ -z "$1" ] && {
	echo point me to the git repo
	exit 1
}

dir="$1"

set -e

pwd=`pwd`
cd "$dir"

# ...
PKG_VERSION=0.8
gitsha=$(git log --format='%h' -n 1)

out=elfix-${PKG_VERSION}_g${gitsha}.tar.bz2

[ -f "$pwd/$out" ] || force=true

if ! $force && head $pwd/elfix.changes | grep -q $gitsha; then
	echo "already there"
	exit 1
fi

( cd $pwd ; osc rm -f elfix-*.bz2 )

git archive --format=tar --prefix=elfix-$PKG_VERSION/ HEAD | bzip2 --best > $pwd/$out

cd $pwd
osc add $out

sed -i -e 's/^\(.*define.*git_version\s\+\).*/\1'$gitsha/ elfix.spec

ed elfix.changes <<EOF
0a
-------------------------------------------------------------------
`date` - $LOGNAME@suse.cz

- update to git $gitsha

.
w
EOF
