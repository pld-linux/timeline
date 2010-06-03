Summary:	An application for displaying and navigating events on a timeline
Summary(pl.UTF-8):	-
Name:		timeline
Version:	0.10.1
Release:	0.2
License:	GPL v3
Group:		Applications
Source0:	http://downloads.sourceforge.net/project/thetimelineproj/thetimelineproj/%{version}/%{name}-%{version}.zip
# Source0-md5:	d47860752d22e77976c8506e8fda54b5
Patch0:		env-python.patch
URL:		http://thetimelineproj.sourceforge.net/
BuildRequires:	gettext-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	scons
BuildRequires:	unzip
Requires:	python-Markdown
Requires:	python-wxPython
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An application for displaying and navigating events on a timeline.

%prep
%setup -q
sed -i "s,\.agw,," timelinelib/gui/components/cattree.py
%patch0 -p1

%build
# generate translations
scons mo

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{py_scriptdir}
cp -rf timelinelib $RPM_BUILD_ROOT%{py_scriptdir}

install -d $RPM_BUILD_ROOT%{_bindir}
install %{name}.py $RPM_BUILD_ROOT%{_bindir}/timeline

install -d $RPM_BUILD_ROOT%{_datadir}/locale
rm po/*.po
cp -rf po/* $RPM_BUILD_ROOT%{_datadir}/locale

install -d $RPM_BUILD_ROOT%{py_scriptdir}/icons
install icons/*.png $RPM_BUILD_ROOT%{py_scriptdir}/icons

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README
%attr(755,root,root) %{_bindir}/%{name}
%{py_scriptdir}/%{name}lib
%{py_scriptdir}/icons
%lang(pt)%{_datadir}/locale/pt/LC_MESSAGES/timeline.mo
