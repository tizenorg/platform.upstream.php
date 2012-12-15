#

%define suhosin_version 0.9.33
%define suhosin_patch_version 0.9.10
%define with_suhosin_patch 0
%define pkg_name php
Name:           php
%global apiver      20090626
%global zendver     20090626

#BuildRequires:  autoconf213
BuildRequires:  bison
BuildRequires:  curl-devel
BuildRequires:  db4-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libjpeg8-devel
#BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  re2c
BuildRequires:  sqlite-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libpng12)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(xpm)

%define extension_dir     %{_libdir}/%{pkg_name}/extensions
%define peardir           %{_datadir}/%{pkg_name}/PEAR
%define php_sysconf       %{_sysconfdir}/%{pkg_name}
%define _x11prefix %(pkg-config --variable=prefix xft)
Version:        5.3.18
Release:        0
License:        PHP-3.01
Summary:        PHP5 Core Files
Url:            http://www.php.net
Group:          Development/Languages/Other
Source0:        php-%{version}.tar.bz2
Source5:        README.macros
Source6:        macros.php
Source7:        install-pear-nozlib.phar
Requires:       timezone
Provides:       php
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains the PHP5 core files, including PHP binary (CLI)
and PHP configuration (php.ini). This package must be installed in
order to use PHP. Additionally, extension modules and server modules
(e.g. for Apache) may be installed.

Additional documentation is available in package php-doc.

%package devel
Summary:        Include files of PHP5
Group:          Development/Languages/C and C++
#this is required by the installed  development headers
Requires:       %{name} = %{version}
#this is needed for "pecl" functionality
Requires:       autoconf
Requires:       automake
Requires:       glibc-devel
Requires:       libtool
Requires:       pkgconfig(libpcre)
Requires:       pkgconfig(libxml-2.0)
Provides:       pecl
Provides:       php-devel
Provides:       php-macros = 2.0
Obsoletes:      php-macros < 2.0
Conflicts:      php4-devel

%description devel
PHP is a server-side, cross-platform, HTML embedded scripting language.
If you are completely new to PHP and want to get some idea of how it
works, have a look at the Introductory Tutorial.  Once you get beyond
that have a look at the example archive sites and some of the other
resources available in the Links section. PHP5 is the latest version.

%package pear
Summary:        PHP Extension and Application Repository
Group:          Development/Libraries/PHP
Requires:       %{name}-zlib = %{version}
Provides:       php-pear
BuildArch:      noarch

%description pear
PEAR is a code repository for PHP extensions and PHP library code
similar to TeX's CTAN and Perl's CPAN. This package provides an access
to the repository.

See http://pear.php.net/manual/ for more details.

%package bcmath
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-bcmath

%description bcmath
Binary Calculator which supports numbers of any size and precision,
represented as strings.

%package bz2
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-bz2

%description bz2
PHP functions to read and write bzip2 (.bz2) compressed files.

%package calendar
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-calendar

%description calendar
PHP functions for converting between different calendar formats.

%package ctype
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-ctype

%description ctype
PHP functions for checking whether a character or string falls into a
certain character class according to the current locale.

%package curl
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-curl

%description curl
PHP interface to libcurl that allows you to connect to and communicate
with servers of many different types, using protocols of many different
types.

%package dba
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-dba

%description dba
This is a general abstraction layer for several file-based databases.
As such, functionality is limited to a common subset of features
supported by modern databases such as Sleepycat Software's DB2. (This
is not to be confused with IBM's DB2 software, which is supported
through the ODBC functions.)

%package dom
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-dom

%description dom
This module adds DOM support.

%package enchant
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-enchant

%description enchant
Enchant is the PHP binding for the Enchant library. Enchant steps in to provide uniformity and conformity on top of all spelling libraries, and implements certain features that may be lacking in any individual provider library. Everything should "just work" for any and every definition of "just working."

%package exif
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-mbstring = %{version}
Provides:       php-exif

%description exif
PHP functions for extracting EXIF (metadata from images) information
stored in headers of JPEG and TIFF images.

%package fileinfo
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-fileinfo

%description fileinfo
The functions in this module try to guess the content type and encoding of a file by looking for certain magic byte sequences at specific positions within the file. While this is not a bullet proof approach the heuristics used do a very good job.

%package ftp
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-openssl = %{version}
Provides:       php-ftp

%description ftp
PHP functions for access to file servers speaking the File Transfer
Protocol (FTP) as defined in rfc959.

%package gd
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-gd

%description gd
PHP functions to create and manipulate image files in a variety of
different image formats, including GIF, PNG, JPEG, WBMP, and XPM. Even
more convenient: PHP can output image streams directly to a browser.

%package gettext
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-gettext

%description gettext
PHP functions that implement an NLS (Native Language Support) API which
can be used to internationalize your PHP applications.

%package gmp
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-gmp

%description gmp
PHP functions for work with arbitrary-length integers using the GNU MP
library.

%package iconv
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-iconv

%description iconv
PHP interface to iconv character set conversion facility.

%package imap
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-imap

%description imap
PHP functions in this extension are not limited to the IMAP protocol,
despite their name. The underlying c-client library also supports NNTP,
POP3 and local mailbox access methods.

%package intl
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-intl

%description intl
Internationalization extension (further is referred as Intl) is a wrapper for ICU library, enabling PHP programmers to perform UCA-conformant collation and date/time/number/currency formatting in their scripts.

%package json
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-json

%description json
Support for JSON (JavaScript Object Notation) serialization.

%package ldap
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-openssl = %{version}
Provides:       php-ldap

%description ldap
PHP interface to Lightweight Directory Access Protocol (LDAP).

%package mbstring
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-mbstring

%description mbstring
This extension provides multi-byte character safe string functions and
other utility functions such as conversion functions.

%package mcrypt
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-mcrypt

%description mcrypt
PHP interface to the mcrypt library, which supports a wide variety of
block algorithms.

%package mssql
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Provides:       php-mssql
Provides:       php_any_db

%description mssql
PHP functions for access to MSSQL database servers.

%package mysql
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-pdo = %{version}
Provides:       php-mysql
Provides:       php5-mysqli = %{version}
Provides:       php5-pdo_mysql = %{version}
Provides:       php_any_db
Obsoletes:      php5-mysqli < %{version}
Obsoletes:      php5-pdo_mysql < %{version}

%description mysql
PHP functions for access to MySQL database servers.

%package odbc
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-pdo = %{version}
Provides:       php-odbc
Provides:       php-pdo_odbc

%description odbc
This module adds ODBC support.

%package openssl
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-openssl

%description openssl
This module adds OpenSSL support.

%package pcntl
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-pcntl

%description pcntl
This module will attempt to implement all features related to process
spawning and control (fork(), waitpid(), signal(), WIF's, etc). This is
extremley experimental, with hope to become stable on most UNIX's. I
greatly appreciate any feedback, fixes, and or suggestions on how to
improve/better implement this functionality.

%package phar
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-phar

%description phar
The phar extension provides a way to put entire PHP applications into a
single file called a "phar" (PHP Archive) for easy distribution and installation.

%package pdo
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-pdo

%description pdo
PHP Data Objects - Data Access Abstraction

- light-weight

- provides common API for common database operations

- keeps majority of PHP specific stuff in the PDO core (such as
persistent resource management); drivers should only have to worry
about getting the data and not about PHP internals.

%package pgsql
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-pdo = %{version}
Provides:       php-pgsql
Provides:       php5-pdo_pgsql = %{version}
Provides:       php_any_db
Obsoletes:      php5-pdo_pgsql < %{version}

%description pgsql
PHP functions for access to PostgreSQL database servers. It includes
both traditional pgsql and pdo_pgsql drivers.

%package posix
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-posix

%description posix
This module allows to use POSIX-like functions in PHP.

%package readline
Summary:        PHP5 readline extension
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-readline

%description readline
PHP interface to libedit, which provides editable command line as well
as PHP interactive mode (php -a)

%package shmop
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-shmop

%description shmop
PHP functions to read, write, create and delete UNIX shared memory
segments.

%package snmp
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-snmp

%description snmp
PHP functions for SNMP.

%package soap
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-soap

%description soap
This module provides SOAP support.

SOAP extension can be used to write SOAP Servers and Clients. It
supports subsets of SOAP 1.1, SOAP 1.2 and WSDL 1.1 specifications.

%package sockets
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-sockets

%description sockets
A low-level interface to the socket communication functions based on
the popular BSD sockets, providing the possibility to act as a socket
server as well as a client. This extension is experimental!

%package sqlite
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-pdo = %{version}
Provides:       php-sqlite = %{version}
Provides:       php-sqlite3 = %{version}
Provides:       php5-pdo_sqlite = %{version}
Obsoletes:      php5-pdo_sqlite < %{version}

%description sqlite
This is an extension for the SQLite Embeddable SQL Database Engine.
http://www.sqlite.org/

SQLite is a C library that implements an embeddable SQL database
engine. Programs that link with the SQLite library can have SQL
database access without running a separate RDBMS process.

SQLite is not a client library used to connect to a big database
server. SQLite is the server. The SQLite library reads and writes
directly to and from the database files on disk.

This package includes sqlite and pdo_sqlite modules for sqlite version
2 and 3 respectively.

%package sysvmsg
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-sysvmsg

%description sysvmsg
This module provides System V IPC support.

%package sysvsem
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-sysvsem

%description sysvsem
PHP interface for System V semaphores.

%package sysvshm
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-sysvshm

%description sysvshm
PHP interface for System V shared memory.

%package tidy
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-tidy

%description tidy
Tidy is an extension based on Libtidy (http://tidy.sf.net/) and allows
a PHP developer to clean, repair, and traverse HTML, XHTML, and XML
documents -- including ones with embedded scripting languages such as
PHP or ASP within them using OO constructs.

%package tokenizer
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-tokenizer

%description tokenizer
The tokenizer functions provide an interface to the PHP tokenizer
embedded in the Zend Engine. Using these functions you may write your
own PHP source analyzing or modification tools without having to deal
with the language specification at the lexical level.

%package wddx
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-wddx

%description wddx
PHP functions for Web Distributed Data Exchange.

%package xmlrpc
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-xmlrpc

%description xmlrpc
This module adds XMLRPC-EPI support.

%package xsl
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-dom = %{version}
Provides:       php-xsl

%description xsl
This module adds new XSL support to PHP.

%package xmlreader
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-dom = %{version}
Provides:       php-xmlreader

%description xmlreader
XMLReader represents a reader that provides non-cached, forward-only
access to XML data. It is based upon the xmlTextReader API from libxml.

%package xmlwriter
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-xmlwriter

%description xmlwriter
XMLWriter wraps the libxml xmlWriter API. Represents a writer that
provides a non-cached, forward-only means of generating streams or
files containing XML data.

%package zip
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-zip

%description zip
Zip is an extension to create, modify and read zip files.

%package zlib
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       php-zlib

%description zlib
PHP functions to read and write gzip (.gz) compressed files.

%prep
%setup -q -n php-%{version}
cp %{SOURCE5} .
cp %{SOURCE7} pear/
# Safety check for API version change.
vapi=`sed -n '/#define PHP_API_VERSION/{s/.* //;p}' main/php.h`
if test "x${vapi}" != "x%{apiver}"; then
   : Error: Upstream API version is now ${vapi}, expecting %{apiver}.
   : Update the apiver macro and rebuild.
   exit 1
fi
vzend=`sed -n '/#define ZEND_MODULE_API_NO/{s/^[^0-9]*//;p;}' Zend/zend_modules.h`
if test "x${vzend}" != "x%{zendver}"; then
   : Error: Upstream Zend ABI version is now ${vzend}, expecting %{zendver}.
   : Update the zendver macro and rebuild.
   exit 1
fi

%build
CFLAGS=`echo %{optflags} |sed -e 's/-ffast-math//g'`
# Regenerate configure scripts (patches change config.m4's)
touch configure.in
# we build three SAPI
mkdir -p build-cli/ext/sqlite/libsqlite/src/

for parser in `find -name "*.re"`;do
    re2c --no-generation-date -gi "$parser" > ${parser%.*}.c
done

rm -rf ext/pcre/pcrelib ext/pdo_sqlite/sqlite

# regenerate configure etc.
# workaround: suhosin-patch updates timestamp of configure, confusing buildconf
#rm -f configure
#./buildconf --force
# export flags
CFLAGS="%{optflags} -O3 -fPIC -DPIC -D_GNU_SOURCE -fno-strict-aliasing"
CXXFLAGS="%{optflags} -O3 -fPIC -DPIC -D_GNU_SOURCE -fno-strict-aliasing"
export CFLAGS
export CXXFLAGS
export NO_INTERACTION=true
# where to install extensions
EXTENSION_DIR=%{extension_dir}
export EXTENSION_DIR

# build function
Build()
{
    sapi=$1
    pushd build-$1
    shift
    ../configure \
        --prefix=%{_prefix} \
        --datadir=%{_datadir}/%{pkg_name} \
        --mandir=%{_mandir} \
        --bindir=%{_bindir} \
        --with-libdir=%{_lib} \
        --includedir=%{_includedir} \
        --sysconfdir=%{php_sysconf}/$sapi \
        --with-config-file-path=%{php_sysconf}/$sapi \
        --with-config-file-scan-dir=%{php_sysconf}/conf.d \
        --enable-libxml \
        --enable-session \
        --with-pcre-regex=%{_prefix} \
        --enable-xml \
        --enable-simplexml \
        --enable-spl \
        --enable-filter \
        --disable-debug \
        --enable-inline-optimization \
        --disable-rpath \
		--disable-static \
		--enable-shared \
		--with-pic \
		--with-gnu-ld \
		--enable-re2c-cgoto \
		--with-system-tzdata=/usr/share/zoneinfo \
        --enable-hash \
        --with-mhash \
        "$@"
# Some modules are builtin, reasons:
#  - libxml can not be shared (and is needed by PEAR)
#  - spl doesn't build shared
#  - simplexml is needed by spl
#  - session need to be builtin, otherwise sqlite and other session engines fail
#  - pcre is needed for PEAR
#  - filter is builtin due security reasons
#We have still have harcoded RPATH in some modules
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=LIBTOOL_IS_BROKED|g' libtool
    make %{?jobs:-j%jobs PHP_PEAR_PHP_BIN=%{_bindir}/php}
    popd
}

# cli sapi with all shared modules
# Hack the built configure to also link ncurses together with libedit.
# this is reported upstream bug http://bugs.php.net/bug.php?id=21153
sed -i "s/-ledit/-ledit -lncurses/g" configure
Build cli \
    --enable-cli \
    --with-pear=%{peardir} \
    --enable-bcmath=shared \
    --enable-calendar=shared \
    --enable-ctype=shared \
    --enable-dom=shared \
    --enable-exif=shared \
    --enable-ftp=shared \
    --enable-mbstring=shared \
    --enable-mbregex \
    --enable-pcntl=shared \
    --enable-posix=shared \
    --enable-shmop=shared \
    --enable-soap=shared \
    --enable-sockets=shared \
    --enable-sysvmsg=shared \
    --enable-sysvsem=shared \
    --enable-sysvshm=shared \
    --enable-tokenizer=shared \
    --enable-wddx=shared \
    --enable-fileinfo=shared \
    --with-zlib=shared \
    --with-bz2=shared \
    --with-curl=shared \
    --with-gd=shared \
        --enable-gd-native-ttf \
        --with-xpm-dir=%{_x11prefix} \
        --with-freetype-dir=%{_prefix} \
        --with-png-dir=%{_prefix} \
        --with-jpeg-dir=%{_prefix} \
        --with-zlib-dir=%{_prefix} \
    --with-gettext=shared \
    --with-gmp=shared \
    --with-iconv=shared \
    --enable-json=shared \
	--with-libedit=shared,%{_prefix} \
    --with-openssl=shared \
    --enable-phar=shared \
    --with-xmlrpc=shared \
    --enable-xmlreader=shared \
    --enable-xmlwriter=shared \
    --with-xsl=shared \
    --enable-dba=shared \
	   --with-db4=%{_prefix} \
       --without-gdbm \
       --with-cdb \
       --with-inifile \
       --with-flatfile \
    --enable-zip=shared \
    --enable-intl=shared,%{_prefix} \
    --disable-cgi
# things that currently do not compile:
# extensions:
#    --with-recode=shared \ error: recode extension can not be configured together with: imap mysql yaz
#disabled extensions
#    --enable-embedded-mysqli \

%check
cd build-cli
# Run tests, using the CLI SAPI
export NO_INTERACTION=1 REPORT_EXIT_STATUS=1 LANG=POSIX LC_ALL=POSIX
unset TZ
#make test
set +x
for f in `find .. -name "*.diff" -type f -print`; do
	echo "TEST FAILURE: $f --"
	cat "$f"
	echo "-- $f result ends."
done
set -x
unset NO_INTERACTION REPORT_EXIT_STATUS

%install
# install function
Install()
{
    pushd build-$1
    make install INSTALL_ROOT=%{buildroot} PHP_PEAR_PHP_BIN=%{_bindir}/php
    popd
}
Install cli
# generate php.ini from php.ini-production:
install -d -m 755 %{buildroot}/%{php_sysconf}/conf.d
install -d -m 755 %{buildroot}/%{php_sysconf}/cli
install -d -m 755 %{buildroot}/%{php_sysconf}/fpm
sed "s=@extdir@=%{extension_dir}=" php.ini-production \
    | sed -r 's/^(html_errors|implicit_flush|max_execution_time|register_argc_argv)/;\1/' \
    > %{buildroot}/%{php_sysconf}/cli/php.ini
# prepare configuration files for each extension
extern_modules=""
for f in %{buildroot}%{extension_dir}/*; do
    if test ${f##*.} = a; then
        rm $f
        continue
    fi
    if test ${f##*.} = so; then
        f=${f%.so}
    fi
    ext=${f##*/}
    extern_modules="$extern_modules $ext"
    echo "; comment out next line to disable $ext extension in php" > %{buildroot}/%{php_sysconf}/conf.d/$ext.ini
    echo "extension=$ext.so" >> %{buildroot}/%{php_sysconf}/conf.d/$ext.ini
done
# list of builtin modules
builtin_modules=`./build-cli/sapi/cli/php -m | egrep -v '^(\[.*)?$' | sort | tr '\n' ' '`
# directory for sessions
install -d %{buildroot}%{_localstatedir}/lib/%{pkg_name}
# documentation
mv sapi/cli/README README.CLI
mv sapi/cgi/README.FastCGI README.FastCGI
rm -rf %{buildroot}/{.channels,.depdb*,.filemap,.lock,usr/bin/peardev}
install -d -m 0755 %{buildroot}/%{peardir}/test
# for pear XML files
install -d -m 0755 %{buildroot}%{_localstatedir}/lib/pear
#fix symlink
sed -i -e "s@$RPM_BUILD_DIR/php-%{version}/build-cli/sapi/cli/php@php@g" %{buildroot}%{_bindir}/phar.phar
rm %{buildroot}%{_bindir}/phar
ln -s -f %{_bindir}/phar.phar %{buildroot}%{_bindir}/phar
# Install the macros file:
install -d %{buildroot}%{_sysconfdir}/rpm
sed -e "s/@PHP_APIVER@/%{apiver}/;s/@PHP_ZENDVER@/%{zendver}/" \
    < $RPM_SOURCE_DIR/macros.php > macros.php
install -m 644 -c macros.php \
           %{buildroot}%{_sysconfdir}/rpm/macros.php



%files
%defattr(-, root, root)
%doc LICENSE
%doc %{_mandir}/man1/*
%dir %{php_sysconf}
%dir %{php_sysconf}/conf.d
%dir %{php_sysconf}/cli
%config(noreplace) %{php_sysconf}/cli/php.ini
%{_bindir}/php
%dir %{_libdir}/%{pkg_name}
%dir %{extension_dir}
%dir %{_datadir}/%{pkg_name}
%attr(0755, wwwrun, root) %dir %{_localstatedir}/lib/%{pkg_name}

%files devel
%defattr(-, root, root)
%{_includedir}/%{pkg_name}
%{_bindir}/phpize
%{_bindir}/php-config
%{_bindir}/pecl
%{_prefix}/lib/php/build
%config %{_sysconfdir}/rpm/macros.php

%files pear
%defattr(-, root, root)
%{_bindir}/pear
%config(noreplace) %{php_sysconf}/cli/pear.conf
%{peardir}
%dir %{_localstatedir}/lib/pear



%files bcmath
%defattr(644,root,root,755)
%{extension_dir}/bcmath.so
%config(noreplace) %{php_sysconf}/conf.d/bcmath.ini

%files bz2
%defattr(644,root,root,755)
%{extension_dir}/bz2.so
%config(noreplace) %{php_sysconf}/conf.d/bz2.ini

%files calendar
%defattr(644,root,root,755)
%{extension_dir}/calendar.so
%config(noreplace) %{php_sysconf}/conf.d/calendar.ini

%files ctype
%defattr(644,root,root,755)
%{extension_dir}/ctype.so
%config(noreplace) %{php_sysconf}/conf.d/ctype.ini

%files curl
%defattr(644,root,root,755)
%{extension_dir}/curl.so
%config(noreplace) %{php_sysconf}/conf.d/curl.ini

%files dba
%defattr(644,root,root,755)
%{extension_dir}/dba.so
%config(noreplace) %{php_sysconf}/conf.d/dba.ini

%files dom
%defattr(644,root,root,755)
%{extension_dir}/dom.so
%config(noreplace) %{php_sysconf}/conf.d/dom.ini


%files exif
%defattr(644,root,root,755)
%{extension_dir}/exif.so
%config(noreplace) %{php_sysconf}/conf.d/exif.ini

%files fileinfo
%defattr(644,root,root,755)
%{extension_dir}/fileinfo.so
%config(noreplace) %{php_sysconf}/conf.d/fileinfo.ini

%files ftp
%defattr(644,root,root,755)
%{extension_dir}/ftp.so
%config(noreplace) %{php_sysconf}/conf.d/ftp.ini

%files gd
%defattr(644,root,root,755)
%{extension_dir}/gd.so
%config(noreplace) %{php_sysconf}/conf.d/gd.ini

%files gettext
%defattr(644,root,root,755)
%{extension_dir}/gettext.so
%config(noreplace) %{php_sysconf}/conf.d/gettext.ini

%files gmp
%defattr(644,root,root,755)
%{extension_dir}/gmp.so
%config(noreplace) %{php_sysconf}/conf.d/gmp.ini

%files iconv
%defattr(644,root,root,755)
%{extension_dir}/iconv.so
%config(noreplace) %{php_sysconf}/conf.d/iconv.ini


%files intl
%defattr(644,root,root,755)
%{extension_dir}/intl.so
%config(noreplace) %{php_sysconf}/conf.d/intl.ini

%files json
%defattr(644,root,root,755)
%{extension_dir}/json.so
%config(noreplace) %{php_sysconf}/conf.d/json.ini

%files mbstring
%defattr(644,root,root,755)
%{extension_dir}/mbstring.so
%config(noreplace) %{php_sysconf}/conf.d/mbstring.ini


%files openssl
%defattr(644,root,root,755)
%{extension_dir}/openssl.so
%config(noreplace) %{php_sysconf}/conf.d/openssl.ini

%files phar
%defattr(644,root,root,755)
%{extension_dir}/phar.so
%config(noreplace) %{php_sysconf}/conf.d/phar.ini
%{_bindir}/phar
%{_bindir}/phar.phar

%files pcntl
%defattr(644,root,root,755)
%{extension_dir}/pcntl.so
%config(noreplace) %{php_sysconf}/conf.d/pcntl.ini



%files posix
%defattr(644,root,root,755)
%{extension_dir}/posix.so
%config(noreplace) %{php_sysconf}/conf.d/posix.ini


%files readline
%defattr(644,root,root,755)
%{extension_dir}/readline.so
%config(noreplace) %{php_sysconf}/conf.d/readline.ini

%files shmop
%defattr(644,root,root,755)
%{extension_dir}/shmop.so
%config(noreplace) %{php_sysconf}/conf.d/shmop.ini


%files soap
%defattr(644,root,root,755)
%{extension_dir}/soap.so
%config(noreplace) %{php_sysconf}/conf.d/soap.ini

%files sockets
%defattr(644,root,root,755)
%{extension_dir}/sockets.so
%config(noreplace) %{php_sysconf}/conf.d/sockets.ini



%files sysvmsg
%defattr(644,root,root,755)
%{extension_dir}/sysvmsg.so
%config(noreplace) %{php_sysconf}/conf.d/sysvmsg.ini

%files sysvsem
%defattr(644,root,root,755)
%{extension_dir}/sysvsem.so
%config(noreplace) %{php_sysconf}/conf.d/sysvsem.ini

%files sysvshm
%defattr(644,root,root,755)
%{extension_dir}/sysvshm.so
%config(noreplace) %{php_sysconf}/conf.d/sysvshm.ini

%files tokenizer
%defattr(644,root,root,755)
%{extension_dir}/tokenizer.so
%config(noreplace) %{php_sysconf}/conf.d/tokenizer.ini

%files wddx
%defattr(644,root,root,755)
%{extension_dir}/wddx.so
%config(noreplace) %{php_sysconf}/conf.d/wddx.ini

%files xmlrpc
%defattr(644,root,root,755)
%{extension_dir}/xmlrpc.so
%config(noreplace) %{php_sysconf}/conf.d/xmlrpc.ini

%files xmlreader
%defattr(644,root,root,755)
%{extension_dir}/xmlreader.so
%config(noreplace) %{php_sysconf}/conf.d/xmlreader.ini

%files xmlwriter
%defattr(644,root,root,755)
%{extension_dir}/xmlwriter.so
%config(noreplace) %{php_sysconf}/conf.d/xmlwriter.ini

%files xsl
%defattr(644,root,root,755)
%{extension_dir}/xsl.so
%config(noreplace) %{php_sysconf}/conf.d/xsl.ini

%files zip
%defattr(644,root,root,755)
%{extension_dir}/zip.so
%config(noreplace) %{php_sysconf}/conf.d/zip.ini

%files zlib
%defattr(644,root,root,755)
%{extension_dir}/zlib.so
%config(noreplace) %{php_sysconf}/conf.d/zlib.ini

%changelog
