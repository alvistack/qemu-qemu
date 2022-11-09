# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects

Name: qemu
Epoch: 100
Version: 7.1.0
Release: 1%{?dist}
Summary: QEMU full system emulation
License: MIT
URL: https://github.com/qemu/qemu/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: alsa-lib-devel
BuildRequires: brlapi-devel
BuildRequires: bzip2-devel
BuildRequires: capstone-devel >= 3.0.5
BuildRequires: cyrus-sasl-devel
BuildRequires: daxctl-devel >= 57
BuildRequires: device-mapper-multipath-devel
BuildRequires: fdupes
BuildRequires: fuse3-devel >= 3.1
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: glib2-devel >= 2.56
BuildRequires: glibc-devel
BuildRequires: gmp-devel
BuildRequires: gnutls-devel
BuildRequires: gtk3-devel >= 3.22.0
BuildRequires: libaio-devel
BuildRequires: libattr-devel
BuildRequires: libbpf-devel
BuildRequires: libcacard-devel >= 2.5.1
BuildRequires: libcap-ng-devel
BuildRequires: libcurl-devel >= 7.29.0
BuildRequires: libdrm-devel
BuildRequires: libepoxy-devel
BuildRequires: libfdt-devel >= 1.4.2
BuildRequires: libgbm-devel
BuildRequires: libiscsi-devel >= 1.9.0
BuildRequires: libjpeg-devel
BuildRequires: libpmem-devel
BuildRequires: libpng-devel >= 1.6.34
BuildRequires: libseccomp-devel >= 2.3.0
BuildRequires: libselinux-devel
BuildRequires: libslirp-devel >= 4.1.0
BuildRequires: libssh-devel >= 0.8.7
BuildRequires: libudev-devel
BuildRequires: libusbx-devel >= 1.0.13
BuildRequires: libuuid-devel
BuildRequires: libva-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libzstd-devel >= 1.4.0
BuildRequires: lzo-devel
BuildRequires: make
BuildRequires: meson >= 0.59.3
BuildRequires: ncurses-devel
BuildRequires: ninja-build >= 1.7
BuildRequires: numactl-devel
BuildRequires: pam-devel
BuildRequires: pixman-devel >= 0.21.8
BuildRequires: pkgconfig
BuildRequires: pulseaudio-libs-devel
BuildRequires: python3-devel
BuildRequires: rdma-core-devel
BuildRequires: SDL2-devel
BuildRequires: snappy-devel
BuildRequires: systemd-devel
BuildRequires: usbredir-devel >= 0.6
BuildRequires: vte291-devel
BuildRequires: zlib-devel

%description
QEMU provides full machine emulation and cross architecture usage. It
closely integrates with KVM and Xen virtualization, allowing for
excellent performance. Many options are available for defining the
emulated environment, including traditional devices, direct host device
access, and interfaces specific to virtualization.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
set -ex && \
    mkdir -p build && \
    pushd build && \
    ../configure \
        --extra-cflags="%{optflags}" \
        --prefix=%{_prefix} \
        --libdir=%{_libdir} \
        --libexecdir=%{_libexecdir} \
        --localstatedir=%{_localstatedir} \
        --mandir=%{_mandir} \
        --sysconfdir=%{_sysconfdir} \
        --target-list=x86_64-softmmu \
        --with-git-submodules=ignore \
        --with-default-devices \
        --audio-drv-list=pa,alsa,oss,sdl \
        --firmwarepath=%{_datadir}/qemu:%{_datadir}/qemu-firmware:%{_datadir}/ipxe/qemu:%{_datadir}/seavgabios:%{_datadir}/seabios:%{_datadir}/sgabios \
        --disable-install-blobs \
        --disable-strip \
        --enable-alsa \
        --enable-attr \
        --enable-auth-pam \
        --enable-avx2 \
        --enable-bochs \
        --enable-bpf \
        --enable-brlapi \
        --enable-bzip2 \
        --enable-cap-ng \
        --enable-capstone \
        --enable-cloop \
        --enable-coroutine-pool \
        --enable-curl \
        --enable-curses \
        --enable-dmg \
        --enable-fuse \
        --enable-gettext \
        --enable-gio \
        --enable-gnutls \
        --enable-gtk \
        --enable-guest-agent \
        --enable-iconv \
        --enable-kvm \
        --enable-l2tpv3 \
        --enable-libdaxctl \
        --enable-libiscsi \
        --enable-libpmem \
        --enable-libssh \
        --enable-libudev \
        --enable-libusb \
        --enable-linux-aio \
        --enable-linux-user \
        --enable-live-block-migration \
        --enable-lzo \
        --enable-malloc-trim \
        --enable-modules \
        --enable-mpath \
        --enable-multiprocess \
        --enable-numa \
        --enable-opengl \
        --enable-oss \
        --enable-pa \
        --enable-parallels \
        --enable-pie \
        --enable-png \
        --enable-pvrdma \
        --enable-qcow1 \
        --enable-qed \
        --enable-qom-cast-debug \
        --enable-rdma \
        --enable-replication \
        --enable-sdl \
        --enable-seccomp \
        --enable-selinux \
        --enable-slirp-smbd \
        --enable-slirp=system \
        --enable-smartcard \
        --enable-snappy \
        --enable-system \
        --enable-tcg \
        --enable-tools \
        --enable-tpm \
        --enable-usb-redir \
        --enable-vdi \
        --enable-vhost-crypto \
        --enable-vhost-kernel \
        --enable-vhost-net \
        --enable-vhost-user \
        --enable-vhost-user-blk-server \
        --enable-vhost-vdpa \
        --enable-virtfs \
        --enable-virtiofsd \
        --enable-vnc \
        --enable-vnc-jpeg \
        --enable-vnc-sasl \
        --enable-vte \
        --enable-vvfat \
        --enable-xkbcommon \
        --enable-zstd && \
    popd
%make_build -C build

%install
%make_build -C build install DESTDIR=%{buildroot}
install -Dpm755 -d %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir} && \
    ln -fs qemu-system-x86_64 qemu-kvm && \
    popd
install -Dpm755 -d %{buildroot}%{_sysconfdir}/qemu
install -Dpm755 -d %{buildroot}%{_unitdir}
install -Dpm755 -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -Dpm755 -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -Dpm644 -t %{buildroot}%{_sysconfdir}/qemu scripts/qemu-guest-agent/fsfreeze-hook
install -Dpm644 -t %{buildroot}%{_unitdir} contrib/systemd/qemu-guest-agent.service
install -Dpm644 -t %{buildroot}%{_datadir}/icons/hicolor/32x32/apps ui/icons/qemu_32x32.png
install -Dpm644 -t %{buildroot}%{_datadir}/icons/hicolor/scalable/apps ui/icons/qemu.svg

%check

%package -n qemu-system
Summary: QEMU full system emulation binaries
Requires: qemu-system-x86 = %{epoch}:%{version}-%{release}

%description -n qemu-system
This metapackage provides the full system emulation binaries for all supported
targets, by depending on all per-architecture system emulation packages which
QEMU supports.

%package -n qemu-system-common
Summary: QEMU full system emulation binaries (common files)

%description -n qemu-system-common
This package provides common files needed for target-specific
full system emulation (qemu-system-*) packages.

%package -n qemu-system-x86
Summary: QEMU full system emulation binaries (x86)
Requires: qemu-system-common = %{epoch}:%{version}-%{release}

%description -n qemu-system-x86
On x86 host hardware this package also enables KVM kernel virtual
machine usage on systems which supports it.

%package -n qemu-utils
Summary: QEMU utilities
Requires: qemu-system-common = %{epoch}:%{version}-%{release}

%description -n qemu-utils
This package provides QEMU related utilities:
  - qemu-img: QEMU disk image utility
  - qemu-io: QEMU disk exerciser
  - qemu-nbd: QEMU disk network block device server

%package -n qemu-guest-agent
Summary: Guest-side qemu-system agent

%description -n qemu-guest-agent
Install this package on a system which is running as guest inside qemu
virtual machine. It is not used on the host.

%files -n qemu-system
%license LICENSE

%files -n qemu-system-common
%exclude %{_unitdir}/qemu-guest-agent.service
%{_bindir}/qemu-pr-helper
%{_bindir}/qemu-storage-daemon
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/locale/*
%{_datadir}/qemu
%{_includedir}/*
%{_libdir}/*
%{_libexecdir}/*

%files -n qemu-system-x86
%{_bindir}/qemu-kvm
%{_bindir}/qemu-system-x86_64

%files -n qemu-utils
%{_bindir}/elf2dmp
%{_bindir}/qemu-edid
%{_bindir}/qemu-img
%{_bindir}/qemu-io
%{_bindir}/qemu-keymap
%{_bindir}/qemu-nbd

%files -n qemu-guest-agent
%{_bindir}/qemu-ga
%{_sysconfdir}/qemu
%{_unitdir}/qemu-guest-agent.service

%changelog
