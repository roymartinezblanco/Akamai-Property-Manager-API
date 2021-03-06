from setuptools import setup

setup(
    name='Akamai OPEN API',
    version='0.1',
    packages=['lib.python3.7.site-packages.ndg', 'lib.python3.7.site-packages.ndg.httpsclient',
              'lib.python3.7.site-packages.ndg.httpsclient.test', 'lib.python3.7.site-packages.cffi',
              'lib.python3.7.site-packages.idna', 'lib.python3.7.site-packages.akamai.edgegrid',
              'lib.python3.7.site-packages.akamai.edgegrid.test', 'lib.python3.7.site-packages.pyasn1',
              'lib.python3.7.site-packages.pyasn1.type', 'lib.python3.7.site-packages.pyasn1.codec',
              'lib.python3.7.site-packages.pyasn1.codec.ber', 'lib.python3.7.site-packages.pyasn1.codec.cer',
              'lib.python3.7.site-packages.pyasn1.codec.der',
              'lib.python3.7.site-packages.pyasn1.codec.native', 'lib.python3.7.site-packages.pyasn1.compat',
              'lib.python3.7.site-packages.certifi', 'lib.python3.7.site-packages.chardet',
              'lib.python3.7.site-packages.chardet.cli', 'lib.python3.7.site-packages.OpenSSL',
              'lib.python3.7.site-packages.urllib3', 'lib.python3.7.site-packages.urllib3.util',
              'lib.python3.7.site-packages.urllib3.contrib',
              'lib.python3.7.site-packages.urllib3.contrib._securetransport',
              'lib.python3.7.site-packages.urllib3.packages',
              'lib.python3.7.site-packages.urllib3.packages.backports',
              'lib.python3.7.site-packages.urllib3.packages.ssl_match_hostname',
              'lib.python3.7.site-packages.requests', 'lib.python3.7.site-packages.pycparser',
              'lib.python3.7.site-packages.pycparser.ply', 'lib.python3.7.site-packages.asn1crypto',
              'lib.python3.7.site-packages.asn1crypto._perf', 'lib.python3.7.site-packages.cryptography',
              'lib.python3.7.site-packages.cryptography.x509',
              'lib.python3.7.site-packages.cryptography.hazmat',
              'lib.python3.7.site-packages.cryptography.hazmat.backends',
              'lib.python3.7.site-packages.cryptography.hazmat.backends.openssl',
              'lib.python3.7.site-packages.cryptography.hazmat.bindings',
              'lib.python3.7.site-packages.cryptography.hazmat.bindings.openssl',
              'lib.python3.7.site-packages.cryptography.hazmat.primitives',
              'lib.python3.7.site-packages.cryptography.hazmat.primitives.kdf',
              'lib.python3.7.site-packages.cryptography.hazmat.primitives.ciphers',
              'lib.python3.7.site-packages.cryptography.hazmat.primitives.twofactor',
              'lib.python3.7.site-packages.cryptography.hazmat.primitives.asymmetric',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.idna',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.pytoml',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.certifi',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.chardet',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.chardet.cli',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.distlib',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.distlib._backport',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.msgpack',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.util',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.contrib',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.contrib._securetransport',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.packages',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.packages.backports',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.packages.ssl_match_hostname',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.colorama',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib._trie',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.filters',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.treewalkers',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.treeadapters',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.treebuilders',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.lockfile',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.progress',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.requests',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.packaging',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.cachecontrol',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.cachecontrol.caches',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.webencodings',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.pkg_resources',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._internal',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._internal.req',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._internal.vcs',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._internal.utils',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._internal.models',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._internal.commands',
              'lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._internal.operations'],
    url='',
    license='',
    author='Roy Martinez',
    author_email='roymartinezblanco@gmail.com',
    description='Akamai OPEN Sample Script for Property Manager'
)
