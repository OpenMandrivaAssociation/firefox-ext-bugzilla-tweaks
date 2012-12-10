Summary: Bugzilla extension for firefox
Name: firefox-ext-bugzilla-tweaks
Version: 1.8
Release: 2
License: MPL
Group:	Networking/WWW
URL:	https://addons.mozilla.org/en-US/firefox/addon/187588/
Source: http://releases.mozilla.org/pub/mozilla.org/addons/187588/bugzilla_tweaks-%{version}-fn+tb+fx.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Obsoletes: %{name} < %{version}
Requires: firefox >= %{firefox_version}
BuildArch: noarch
BuildRequires: firefox-devel

%description
This extension modifies the pages loaded from bugzilla.mozilla.org and adds features including:
- Interleaving the bug's change history with the comments on the same page
- Showing the last time that a bug or attachment flag was changed
- Proving user name autocompletion support
- And many more...

%prep
%setup -q -c -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{firefox_extdir}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{firefox_extdir}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%files
%defattr(0644,root,root,0755)
%{firefox_extdir}


%changelog
* Sat Mar 19 2011 Funda Wang <fwang@mandriva.org> 1.8-1mdv2011.0
+ Revision: 646529
- new version 1.8

* Fri Jan 28 2011 Funda Wang <fwang@mandriva.org> 1.6-3
+ Revision: 633584
- build for new ff ext dir

* Wed Jan 05 2011 Thierry Vignaud <tv@mandriva.org> 1.6-2mdv2011.0
+ Revision: 628870
- rebuild for new firefox

* Mon Nov 15 2010 Thierry Vignaud <tv@mandriva.org> 1.6-1mdv2011.0
+ Revision: 597639
- import firefox-ext-bugzilla-tweaks

