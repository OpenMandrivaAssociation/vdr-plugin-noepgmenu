%define plugin	noepgmenu
%define beta	beta4

Summary:	VDR plugin: a menu for noEPG patch
Name:		vdr-plugin-%plugin
Version:	0.0.6
%if %beta
Release:	3.%beta.1
%else
Release:	4
%endif
Group:		Video
License:	GPL
URL:		http://winni.vdr-developer.org/noepgmenu/
%if %beta
Source:		http://winni.vdr-developer.org/noepgmenu/downloads/beta/vdr-%plugin-%{version}.%beta.tgz
%else
Source:		http://winni.vdr-developer.org/noepgmenu/downloads/vdr-%plugin-%{version}.tgz
%endif
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
A simple OSD to manage the channels for the noEPG patch.

%prep
%if %beta
%setup -q -n %plugin-%{version}.%beta
%else
%setup -q -n %plugin-%{version}
%endif
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%doc README HISTORY




