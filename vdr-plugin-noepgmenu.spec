
%define plugin	noepgmenu
%define name	vdr-plugin-%plugin
%define version	0.0.6
%define beta	beta4
%define rel	2

Summary:	VDR plugin: a menu for noEPG patch
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://winni.vdr-developer.org/noepgmenu/
%if %beta
Source:		http://winni.vdr-developer.org/noepgmenu/downloads/beta/vdr-%plugin-%version.%beta.tgz
%else
Source:		http://winni.vdr-developer.org/noepgmenu/downloads/vdr-%plugin-%version.tgz
%endif
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
A simple OSD to manage the channels for the noEPG patch.

%prep
%if %beta
%setup -q -n %plugin-%version.%beta
%else
%setup -q -n %plugin-%version
%endif
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.6-1mdv2010.0
+ Revision: 401088
- rebuild for new VDR
- new beta version

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.5-3mdv2009.1
+ Revision: 359342
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.5-2mdv2009.0
+ Revision: 197954
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.5-1mdv2009.0
+ Revision: 197696
- new version
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- update URL

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2-12mdv2008.1
+ Revision: 145152
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-11mdv2008.1
+ Revision: 103172
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-10mdv2008.0
+ Revision: 50022
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-9mdv2008.0
+ Revision: 42108
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-8mdv2008.0
+ Revision: 22760
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-7mdv2007.0
+ Revision: 90947
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-6mdv2007.1
+ Revision: 74056
- rebuild for new vdr
- Import vdr-plugin-noepgmenu

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-2mdv2007.0
- rebuild for new vdr

* Sun Jul 16 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-1mdv2007.0
- initial Mandriva release

