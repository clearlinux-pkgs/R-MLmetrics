#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-MLmetrics
Version  : 1.1.1
Release  : 39
URL      : https://cran.r-project.org/src/contrib/MLmetrics_1.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/MLmetrics_1.1.1.tar.gz
Summary  : Machine Learning Evaluation Metrics
Group    : Development/Tools
License  : GPL-2.0
Requires: R-ROCR
BuildRequires : R-ROCR
BuildRequires : buildreq-R

%description
utility functions, that measure regression, classification and ranking performance.

%prep
%setup -q -c -n MLmetrics
cd %{_builddir}/MLmetrics

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641060949

%install
export SOURCE_DATE_EPOCH=1641060949
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library MLmetrics
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library MLmetrics
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library MLmetrics
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc MLmetrics || :


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
