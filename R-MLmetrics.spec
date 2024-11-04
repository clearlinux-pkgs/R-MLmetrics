#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v10
# autospec commit: 5905be9
#
Name     : R-MLmetrics
Version  : 1.1.3
Release  : 42
URL      : https://cran.r-project.org/src/contrib/MLmetrics_1.1.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/MLmetrics_1.1.3.tar.gz
Summary  : Machine Learning Evaluation Metrics
Group    : Development/Tools
License  : GPL-2.0
Requires: R-ROCR
BuildRequires : R-ROCR
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
utility functions, that measure regression, classification and ranking performance.

%prep
%setup -q -n MLmetrics
pushd ..
cp -a MLmetrics buildavx2
popd
pushd ..
cp -a MLmetrics buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713136681

%install
export SOURCE_DATE_EPOCH=1713136681
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/MLmetrics/DESCRIPTION
/usr/lib64/R/library/MLmetrics/INDEX
/usr/lib64/R/library/MLmetrics/Meta/Rd.rds
/usr/lib64/R/library/MLmetrics/Meta/features.rds
/usr/lib64/R/library/MLmetrics/Meta/hsearch.rds
/usr/lib64/R/library/MLmetrics/Meta/links.rds
/usr/lib64/R/library/MLmetrics/Meta/nsInfo.rds
/usr/lib64/R/library/MLmetrics/Meta/package.rds
/usr/lib64/R/library/MLmetrics/NAMESPACE
/usr/lib64/R/library/MLmetrics/R/MLmetrics
/usr/lib64/R/library/MLmetrics/R/MLmetrics.rdb
/usr/lib64/R/library/MLmetrics/R/MLmetrics.rdx
/usr/lib64/R/library/MLmetrics/help/AnIndex
/usr/lib64/R/library/MLmetrics/help/MLmetrics.rdb
/usr/lib64/R/library/MLmetrics/help/MLmetrics.rdx
/usr/lib64/R/library/MLmetrics/help/aliases.rds
/usr/lib64/R/library/MLmetrics/help/paths.rds
/usr/lib64/R/library/MLmetrics/html/00Index.html
/usr/lib64/R/library/MLmetrics/html/R.css
