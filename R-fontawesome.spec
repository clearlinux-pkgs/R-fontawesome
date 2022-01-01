#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fontawesome
Version  : 0.2.2
Release  : 2
URL      : https://cran.r-project.org/src/contrib/fontawesome_0.2.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fontawesome_0.2.2.tar.gz
Summary  : Easily Work with 'Font Awesome' Icons
Group    : Development/Tools
License  : MIT
Requires: R-htmltools
Requires: R-rlang
BuildRequires : R-htmltools
BuildRequires : R-rlang
BuildRequires : buildreq-R

%description
documents and 'Shiny' apps. These icons can be inserted into HTML content
    through inline 'SVG' tags or 'i' tags. There is also a utility function for
    exporting 'Font Awesome' icons as 'PNG' images for those situations where
    raster graphics are needed.

%prep
%setup -q -c -n fontawesome
cd %{_builddir}/fontawesome

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641018556

%install
export SOURCE_DATE_EPOCH=1641018556
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fontawesome
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fontawesome
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fontawesome
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc fontawesome || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fontawesome/DESCRIPTION
/usr/lib64/R/library/fontawesome/INDEX
/usr/lib64/R/library/fontawesome/LICENSE
/usr/lib64/R/library/fontawesome/Meta/Rd.rds
/usr/lib64/R/library/fontawesome/Meta/features.rds
/usr/lib64/R/library/fontawesome/Meta/hsearch.rds
/usr/lib64/R/library/fontawesome/Meta/links.rds
/usr/lib64/R/library/fontawesome/Meta/nsInfo.rds
/usr/lib64/R/library/fontawesome/Meta/package.rds
/usr/lib64/R/library/fontawesome/NAMESPACE
/usr/lib64/R/library/fontawesome/NEWS.md
/usr/lib64/R/library/fontawesome/R/fontawesome
/usr/lib64/R/library/fontawesome/R/fontawesome.rdb
/usr/lib64/R/library/fontawesome/R/fontawesome.rdx
/usr/lib64/R/library/fontawesome/apps/138-icon-fontawesome/app.R
/usr/lib64/R/library/fontawesome/fontawesome/css/all.css
/usr/lib64/R/library/fontawesome/fontawesome/css/all.min.css
/usr/lib64/R/library/fontawesome/fontawesome/css/v4-shims.css
/usr/lib64/R/library/fontawesome/fontawesome/css/v4-shims.min.css
/usr/lib64/R/library/fontawesome/fontawesome/webfonts/fa-brands-400.ttf
/usr/lib64/R/library/fontawesome/fontawesome/webfonts/fa-brands-400.woff
/usr/lib64/R/library/fontawesome/fontawesome/webfonts/fa-regular-400.ttf
/usr/lib64/R/library/fontawesome/fontawesome/webfonts/fa-regular-400.woff
/usr/lib64/R/library/fontawesome/fontawesome/webfonts/fa-solid-900.ttf
/usr/lib64/R/library/fontawesome/fontawesome/webfonts/fa-solid-900.woff
/usr/lib64/R/library/fontawesome/help/AnIndex
/usr/lib64/R/library/fontawesome/help/aliases.rds
/usr/lib64/R/library/fontawesome/help/figures/fontawesome_rmd.png
/usr/lib64/R/library/fontawesome/help/figures/fontawesome_shiny_app.png
/usr/lib64/R/library/fontawesome/help/figures/logo.svg
/usr/lib64/R/library/fontawesome/help/fontawesome.rdb
/usr/lib64/R/library/fontawesome/help/fontawesome.rdx
/usr/lib64/R/library/fontawesome/help/paths.rds
/usr/lib64/R/library/fontawesome/html/00Index.html
/usr/lib64/R/library/fontawesome/html/R.css
/usr/lib64/R/library/fontawesome/tests/testthat.R
/usr/lib64/R/library/fontawesome/tests/testthat/test-fa_icon.R
