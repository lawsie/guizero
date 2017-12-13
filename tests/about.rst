Guizero testing
===============

Description
-----------
Each Guizero widget is assigned its own ``unittest.TestCase``.
All widgets that require a ``master`` argument, have a ``setUpClass``
method, which binds a Guizero ``App`` instance to the class.

Each class is guaranteed to implement at least these methods:

* ``test_constructor``:
  
  * Instantiate the widget;
  * Query the underlying ``tk`` widget using ``tk.cget`` and ``tk.winfo_*`` to get its properties;
  * Check if the properties match the expected values (those passed explicitly to the constructor
    or keyword arguments).

* ``test_properties``:

  * Instantiate the widget;
  * Query the underlying ``tk`` widget using ``tk.cget`` and ``tk.winfo_*`` to get its properties;
  * For each property, check if the corresponding Guizero getter returns the same value;
  * Use the Guizero setters to reconfigure the widget;
  * For each property, check if the corresponding Guizero getter returns the same value.

* ``test_methods`` (Not implemented yet):

  * Instantiate the widget;
  * Test all methods unique to the Guizero class (not those inherited from ``_Widget``).

If a Guizero class implements no custom methods or properties, those test cases should return immediately:

.. code-block:: python

  def test_constructor(self):
      ...

  def test_properties(self):
      return
      
  def test_methods(self):
      return

Bug tracker
-----------
I've added a module-level docstring with a primitive bug tracker. If you find any new
bugs while testing, please update it. If anybody cares to create a separate file for this,
that would be helpful.

Helping out
-----------
* All feedback is welcome.
* If you feel the need to remove or change something, please discuss the issue first
* Be reasonable about test cases. Don't test something twice, 'just to be sure'.
* Feel free to add comments to the code if something is unclear to you
