`Unreleased <https://github.com/pace-neutrons/Euphonic/compare/v0.2.2...HEAD>`_
----------

`v0.2.2 <https://github.com/pace-neutrons/Euphonic/compare/v0.2.1...v0.2.2>`_
------

- Bug fixes:

  - Add MANIFEST.in for PyPI distribution

`v0.2.1 <https://github.com/pace-neutrons/Euphonic/compare/v0.2.0...v0.2.1>`_
------

- Bug fixes:

  - Cannot easily upload C header files to PyPI without an accompanying source
    file, so refactor C files to avoid this

`v0.2.0 <https://github.com/pace-neutrons/Euphonic/compare/v0.1-dev3...v0.2.0>`_
------

- There are several breaking changes:

  - Changes to the object instantiation API. The former interface
    ``InterpolationData(seedname)`` has been changed to
    ``InterpolationData.from_castep(seedname)`,` in anticipation of more codes
    being added which require more varied arguments.
  - Changes to the Debye-Waller calculation API when calculating the structure
    factor. The previous ``dw_arg`` kwarg accepted either a seedname or length
    3 list describing a grid. The new kwarg is now ``dw_data`` and accepts a
    ``PhononData`` or ``InterpolationData`` object with the frequencies
    calculated on a grid. This is to make it clearer to the user exactly what
    arguments are being used when calculating phonons on the grid.
  - Changes to parallel functionality. The previous parallel implementation
    based on Python's multiprocessing has been removed and replaced by a
    C/OpenMP version. This has both better performance and is more robust. As
    a result the ``n_procs`` kwarg to ``calculate_fine_phonons`` has been
    replaced by ``use_c`` and ``n_threads`` kwargs.

- Improvements:

  - The parallel implementation based on Python's multiprocessing has been
    removed and now uses C/OpenMP which both has better performance and is more
    robust
  - Documentation has been moved to readthedocs and is more detailed
  - Clearer interface for calculating the Debye-Waller factor
  - Better error handling (e.g. empty ``InterpolationData`` objects, Matplotlib
    is not installed...)

- Bug fixes:

  - Fix gwidth for DOS not being converted to correct units
  - Fix qwidth for S(Q,w) broadening being incorrectly calculated
