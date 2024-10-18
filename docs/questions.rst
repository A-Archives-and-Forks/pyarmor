=====
 FAQ
=====

.. highlight:: none

Pyarmor provides rich options for different cases, the default option only works for common case. When something is wrong, it may be not bug, but need the right options. Users need spend time learning Pyarmor by documentation or `pyarmor man`, and find the right options for their project. Generally pyarmor team won't learn user's project and tell user which options should be used.

Pyarmor is well document, you needn't read all of them at first, but it's necessary to read :doc:`tutorial/getting-started` which includes essentials concepts. If you spend 10 minutes reading full of it, it may save your several hours to solve the wrong usage problems.

If using :command:`pyarmor-7` or Pyarmor < 8.0, please check `Pyarmor 7.x Doc`_

.. important::

   Pyarmor team handles too many wrong usage issues, so one document :doc:`reference/solutions` has been arranged to solve this kind of issue quickly. If you aren't sure this issue is wrong usage or not, please check this doc at first.

   Pyarmor team will mark this kind of issue as `invalid` or `documented` and close it immediately.

.. _asking questions:

Asking questions in GitHub
==========================

Before ask question, please try the following common solutions in order to avoid duplicated issues:

- If need some feature, first check :ref:`the detailed table of contents <mastertoc>`

- If there is error message, check :doc:`reference/errors`

- If obfuscated scripts don't work as expected, make sure you have read :doc:`topic/obfuscated-script`

- If you have trouble in pack, check :doc:`topic/repack`

- If you have trouble in :term:`RFT Mode`, check :ref:`using rftmode`

- If you have trouble in :term:`BCC Mode`, check :ref:`using bccmode`

- If you have trouble with third-party libraries, check :doc:`how-to/third-party`

- If it's related to security and performance, check :doc:`topic/performance`

- Look through this page

- Enable debug mode and trace log, check console log and trace log to find more information

- Make sure the scripts work without obfuscation

- Do a simple test, obfuscate a hello world script, and run it with python

- If not using latest Pyarmor version, try to upgrade Pyarmor to latest version.

- Search in the Pyarmor `issues`_

- Search in the Pyarmor `discussions`_

Please report bug in `issues`_ and ask questions in `discussions`_

.. _reporting bugs:

Reporting bug
=============

A good report should have

- A clear title
- Reproduced steps
- Actual results
- Expected results

For different issues, please following different guide to report bug, and do not paste snapshot image but paste text directly.

.. important::

   If a bug report misses necessary information and not clear, it may be marked as invalid and closed immediately.

Build issues
------------

If there is error message when run pyarmor, please first check :doc:`reference/errors` to find solutions

If still no solution, please run pyarmor with debug option :option:`-d`. For example::

    $ pyarmor -d gen ...
    $ pyarmor -d reg ...

It will generate file :file:`pyarmor.report.bug` like this::

    [Bug] `FileNotFoundError: [Errno 2] No such file or directory: 'aa.zip'`

    ### Full command options and console output
    pyarmor -d reg aa.zip

    2024-05-30 21:50:52,682 Python 3.7.10
    2024-05-30 21:50:52,684 Pyarmor 8.5.9 (pro), 005068, btarmor
    2024-05-30 21:50:52,696 Platform darwin.x86_64
    2024-05-30 21:50:52,696 native platform darwin.x86_64
    2024-05-30 21:50:52,696 home path: /Users/jondy/.pyarmor
    2024-05-30 21:50:52,696 register "aa.zip"
    2024-05-30 21:50:52,698 unknown error, please check pyarmor.error.log
    2024-05-30 21:50:52,704 [Errno 2] No such file or directory: 'aa.zip'

    ### Traceback
    Traceback (most recent call last):
        ...
        self.fp = io.open(file, filemode)
    FileNotFoundError: [Errno 2] No such file or directory: 'aa.zip'

Take the first line `[Bug] ...` as bug title, and the rest content as bug body and make necessary supplements and explanations

Pack issues
-----------

Check list for pack issues:

- Using PyInstaller to pack the script without obfuscation, make sure the final bundle works
- Without packing, only obfuscate scripts, make sure the obfuscated scripts works

If check list pass, then report bug as the next section guide

Runtime issues
--------------

If the obfuscated scripts doesn't work or not as expected, first check :doc:`topic/obfuscated-script`

If there is error message, also check :doc:`reference/errors` to find solutions

If using :option:`--enable-bcc`, try to obfuscate script without it. If make sure this option results in problem, check :ref:`using bccmode` to find solutions

If using :option:`--enable-rft`, , try to obfuscate script without it. If make sure this option results in problem, check :ref:`using rftmode` to find solutions

Try to use less options to obfuscate script, find the minimum options to reproduce this issue

Report runtime issue with:

- A clear title
- Full command options to obfuscate scripts
- Full command to run the obfuscated scripts and traceback (if any)
- Necessary supplements and explanations

Hot Questions
=============

**Is there any tool could broken Pyarmor?**

  Pyarmor team doesn't care about these kind of tools, but focus on researching CPython source to design obfuscation algorithm. Through several irreversible obfuscation methods, Pyarmor makes sure the obfuscated scripts can't be restored by any way.

  Refer to :doc:`how-to/security`, use the highest security options available for you to obfuscate this script

  .. code-block:: python

     import sys

     def fib(n):
         a, b = 0, 1
         while a < n:
             print(a, end=' ')
             a, b = b, a+b
         print()

     print('python version:', sys.version_info[:2])
     print('this is fib(10)', fib(10))

  And then try any tool to broken it.

  If it's broken, please send Python version, Pyarmor version, Platform, Obfuscation options, sample script and broken steps to |Contact|

  **Do not publish any pyarmor hack link in Pyarmor project**

  Pyarmor is good at protecting Python scripts, but not good at memory protection and anti-debug. If you care about runtime memory data, or runtime key verification, generally it need extra methods to prevent debugger from hacking dynamic libraries. More information check :doc:`how-to/protection`

..
  Segment fault in Apple
  ======================

  First upgrade Pyarmor to 8.3.0+ which has fixed non-system Python crash issues.

  If it has been the latest version, then check both of prebuilt extensions `pytransform3.so` and `pyarmor_runtime.so`

  * Make sure code sign is OK by `codesign -v /path/to/xxx.so`
  * Check used shared libraries `otool -L /path/to/xxx.so`, make sure all of them exist.

  For Pyarmor prior to 8.3.0, check the following issues

  **Generally it's code sign issue**

  If segment fault when obfuscating scripts or registering Pyarmor, try to re-sign extension ``pytransform3.so``::

      $ codesign -s - -f /path/to/lib/pythonX.Y/site-packages/pyarmor/cli/core/pytransform3.so

  If segment fault when launching obfuscated scripts, try to re-sign extension ``pyarmor_runtime.so``::

      $ codesign -s - -f dist/pyarmor_runtime_000000/pyarmor_runtime.so

  If your app doesn’t have the new signature format, or is missing the DER entitlements in the signature, you’ll need to re-sign the app on a Mac running macOS 11 or later, which includes the DER encoding by default.

  If you’re unable to use macOS 11 or later to re-sign your app, you can re-sign it from the command-line in macOS 10.14 and later. To do so, use the following command to re-sign the MyApp.app app bundle with DER entitlements by using a signing identity named "Your Codesign Identity" stored in the keychain::

      $ codesign -s "Your Codesign Identity" -f --preserve-metadata --generate-entitlement-der /path/to/MyApp.app

  Refer to Apple official documentation `Using the latest code signature format`__

  **Not system Python**

  The prebuilt ``pytrnasform.so`` and ``pyarmor_runtime.so`` need Python shared library, if there is no found Python shared library, it may crash.

  Using command line tool ``otool`` and ``install_name_tool`` to fix Python shared library issue.

  To display the names and version numbers of the shared libraries that the object file uses::

      $ otool -L /path/to/lib/python3.9/site-packages/pyarmor/cli/core/pytransform3.so

      /path/to/lib/python3.9/site-packages/pyarmor/cli/core/pytransform3.so:
  	pytransform3.so (compatibility version 0.0.0, current version 1.0.0)
  	@rpath/lib/libpython3.9.dylib (compatibility version 3.9.0, current version 3.9.0)
          ...

  And ``rpath`` is configured by::

      $ install_name_tool -id pytrnsform3.so \
              -change $deplib @rpath/lib/libpython$ver.dylib \
              -add_rpath @executable_path/.. \
              -add_rpath @loader_path/.. \
              -add_rpath /System/Library/Frameworks/Python.framework/Versions/$ver \
              -add_rpath /Library/Frameworks/Python.framework/Versions/$ver \
              build/$host/libs/cp$ver/$name.so

  So check there is ``@rpath/lib/libpython3.9.dylib``. If it doesn't exists, please adapt to current Python by using ``install_name_tool``. Suppose current Python shared library is ``/usr/local/Python.framework/Versions/3.9/Python``::

      $ install_name_tool -change @rpath/lib/libpython3.9.dylib /usr/local/Python.framework/Versions/3.9/Python \
              /path/to/lib/pythonX.Y/site-packages/pyarmor/cli/core/pytransform3.so

  How to find current Python shared library, please search network to find answer. Note that some Python may not built with shared library, it can't work with Pyarmor, please rebuild Python with shared library to fix this kind of issue.

  It's same for ``dist/pyarmor_runtime_000000/pyarmor_runtime.so``.

  Refer to Apple official documentation `Run-Path Dependent Libraries`__

  **If there are many same version Python installed, make sure pytransform3.so or pyarmor_runtime.so links to the right one**

  For example, there is default Python3.9 in ``/Library/Frameworks/Python.framework/Versions/3.9/`` and anaconda3 Python 3.9 in ``/Users/my_username/anaconda3/bin/python``

  When using ``/Users/my_username/anaconda3/bin/python`` to run the obfuscated script, it will load ``dist/pyarmor_runtime_000000/pyarmor_runtime.so``, and this library need Python dynamic library. According to RPATH settings, first search ``/Users/my_username/anaconda3/bin/python/../lib/libpython3.9.dylib``, if it exists, everything is fine. If it doesn't exists, then search ``/Library/Frameworks/Python.framework/Versions/3.9/lib/libpython3.9.dylib``, load this unexpected Python dynamic library, and results in crash issue.

  In this canse using `install_name_tool` to modify ``dist/pyarmor_runtime_000000/pyarmor_runtime.so`` so that it could load Python dynamic library in anaconda3.

  Note that the obfuscated scripts work with system Python by default, and as possible as work with Python installed in the other locations.

  **Application settings**

  Pyarmor uses JIT to improve security, In Apple M1, it need extra entitlements. Check Python entitlements::

      $ codesign -d --entitlements - $(which python)

  Refer to Apple official documentation `Allow Execution of JIT-compiled Code Entitlement`__

  **Check system segment fault log, and search solution by error message**

  __ https://developer.apple.com/documentation/xcode/using-the-latest-code-signature-format/
  __ https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/RunpathDependentLibraries.html
  __ https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_cs_allow-jit

  Registering
  ===========

  **ERROR request license token failed (104)**

    Please make sure firewall doesn't block the response of license server. If possible, turn off the firewall to verify it.

    In Windows ``pytransform.pyd`` will connect to ``pyarmor.dashingsoft.com`` port ``80`` to request token for online obfuscation, in other platforms it is ``pytransform3.so``. Refer to firewall documentation to allow it to connect ``pyarmor.dashingsoft.com:80``.

  **Group license raises "ERROR request license token failed"**

    First upgrade Pyarmor to 8.4.0+

    Then register group license with debug option ``-d`` in offline device. For example::

        $ pyarmor -d reg pyarmor-device-regfile-6000.4.zip

    Check log, make sure current machine id is inclueded by offline regfile. For example::

        DEBUG    group license for machines: ['tokens/mb04eb35da4f5378185c8663522e0a5e3']
        DEBUG    got machine id: mb04eb35da4f5378185c8663522e0a5e3

    If machine id is mismatched, please generate new device file for this device by Pyarmor 8.4.0+::

        $ pyarmor -v

        Pyarmor 8.4.0
        ...

        $ pyarmor reg -g 5

    For virtual machine, make sure machine id is same after reboot.

License
=======

**Will Pyarmor Pro license upload my scripts to remote server to verify license?**

  No. For Pyarmor Basic and Pro License, only Pyarmor License file, serial number of hard disk, Ethernet address, IPv4/IPv6 address, and hostname will be sent to remote server for verification.

**I am interested to know if the users are entitled to updates to ensure compatibility with future versions of Python.**

  No. Pyarmor license works with current Pyarmor version forever, but may not work with future Pyarmor version. I can't make sure current Pyarmor version could support all the future versions of Python, so the answer is no.

**we use Docker to build/obfuscate the code locally then publish the Docker file to the client. After the build stage, the whole environment (and the license) is gone. I wonder how the workflow would be? Can I add the license file to the pipeline and register every time and build?**

  Please refer to :doc:`how-to/ci`

**We are currently using a trial license for testing, but unfortunately our scripts are big and we are not able to statistically test the operation of Pyarmor. Do you have a commercial trial license for a certain trial period so that we can test the operation of Pyarmor for our scripts?**

  Sorry, Pyarmor is a small tool and only cost small money, there is no demo license plan.

  Most of features could be verified in trial version, other advanced features, for example, mix-str, bcc mode and rft mode, could be configured to ignore one function or one script so that all the others could work with these advanced features.

**Is the Internet connection only required to generate the obfuscated script? No internet connection is required on the target device that uses such script?**

  No internet connection is required on target device.

  Pyarmor has no any control or limitation to obfuscated scripts, the behaviors of obfuscated scripts are totally defined by user.

  Please check Pyarmor EULA 3.4.1

**Our company has a suite of products that we offer together or separately to our clients. Do we need a different license for each of them?**

  For a suite of products, if each product is different totally, for example, a suite "Microsoft Office” includes “Microsoft Excel”, “Microsoft Word”, each product need one license.

  If a suite of products share most of Python scripts, as long as the proportion of the variable part of each product is far less than that of the common part, they’re considered as "one product".

  If each product in a suite of products is functionally complementary, for example, product "Editor" for editing the file, product "Viewer" for view the file, they’re considered as "one product"

**Which PyArmor 8.0 license for CI, more than 100 runs / day**

  It's recommend to upgrade to Pyarmor 9, and use :term:`Pyarmor CI` License or :term:`Pyarmor Basic` License. See also :doc:`how-to/ci`
..
  **We intend to use PyArmor in CI to build obfuscated Docker images. According to the docs we can't use PyArmor in CI because the machine IDs will be different across each CI run (we verified this is the case), but according to this section in the docs, we can use PyArmor on "all the devices to develop, build, test the product", so we're a bit confused on whether this would work in CI. Could we buy a group license and then activate PyArmor as part of the CI pipeline? All of these different CI machines and developer laptops are building "one product"**

  Unfortunately the answer is **NO**. One license could be used in any device for one product, at the same time, they must be under license limitation.

Upgrading
---------

**If we buy version 8 license, is it compatible with earlier versions like 6.7.2?**

  No. Pyarmor 8 license can't be used with earlier versions, it may report HTTP 401 error or some unknown errors.

**Can we obfuscate our code base with the same level as current? (we are obfuscating our code using super plus mode ("--advanced 5"). Is that available on Pyarmor Basic?**

  The old license is valid for ever. In this case need not upgrade old license to Pyarmor Basic license, just install Pyarmor 8.x, and using :command:`pyarmor-7` with old license.

  Check :doc:`how-to/register` for more information about upgrading

**If we upgrade the old license, will the current license expire? (no more available in terms of Pyarmor v7?**

  If upgrade old license to any Pyarmor 8 license, the current license is no more available in the terms of Pyarmor 7.

**How long is the current license valid? Is there a published end-of-support schedule?**

  The license is valid for ever with Pyarmor version when purchasing this license, but may not work for future Pyarmor, there is no schedule about in which version current license doesn't work.

  Since the first release Pyarmor changed its license 2 times because the core libraries are rewritten:

  - the initial license issued around year 2010 (I forget the exact date)
  - the second license issued on 2019-10-10
  - this is the third license, issued on 2023-03-10

**Does the license include access to support and software updates? If so, what is the duration of support and how are updates delivered?**

  Generally the license could be used in the next versions, until there are big changes in one major version, but I have no plan in details. Just run `pip install` to upgrade Pyarmor to latest version, the license will keep work.

  But there is no more technical supports about how to use Pyarmor, Pyarmor is a command line tool, and all the options are full documentations. Pyarmor users need spend some time to learn Pyarmor by himself.

**Is there an option for custom licensing arrangements to accommodate specific project or organizational needs?**

  At this time, the answer is no.

**In the old pyarmor 7, I'm using "pyarmor pack ...", I could not find any relate information for this in the pyarmor 8.2. How to solve this?**

  There is no identical pack in Pyarmor 8, Pyarmor 8+ only provide repack function to handle bundle of PyInstaller. Refer to basic tutorial, topic `insight into pack`__ and this solved issue `Pyarmor pack missing in pyarmor 8.0`__

__ https://pyarmor.readthedocs.io/en/stable/topic/repack.html
__ https://github.com/dashingsoft/pyarmor/discussions/1107

Purchasing
==========

**How to refund my order?**

  If this order isn't activated and in 30 days since purchasing, you can refund the order by one of ways

  * If purchasing order from MyCommerce:

    1. Email to Ordersupport@mycommerce.com with order information and ask for refund.
    2. Or click `FindMyOrder page`_ to submit refund request

  * If purchasing order from reseller, contact your reseller

  * For other cases, email to pyarmor@163.com

.. _FindMyOrder page: https://www.findmyorder.com/store?Action=DisplayEmailCustomerServicePage&Env=BASE&Locale=en_US&SiteID=findmyor

Misc.
=====

**What is the ECCN or rating of Pyarmor (EAR99,5D99S,5D002 or other type ECCN)?**

  EAR99

**Does Pyarmor contain any encryption capabilities?**

  Pyarmor uses AES/RSA etc., but it hasn’t its own encryption algorithms.

**What is the country of origin of this package?**

  China

**Where is the final built for Pyarmor?**

  All of Pyarmor packages are published in the PyPI_, refer to :term:`Pyarmor Package` and section `Installation in offline device` in the chapter :doc:`tutorial/installation`

**Pyarmor Pro checks the internet, what is the output IP or DNS? I need to release it on my client's firewall, placing an outbound rule for yours IP.**

  Now it's `119.23.58.77` (March 20, 2024)

.. include:: _common_definitions.txt
