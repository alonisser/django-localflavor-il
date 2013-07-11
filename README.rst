
=====================
django_localflavor_il
=====================

.. image:: https://travis-ci.org/alonisser/django-localflavor-il.png
   :target: https://travis-ci.org/alonisser/django-localflavor-il

Country-specific Django helpers for Israel.

What's in the Israel localflavor?
=================================

* forms.ILPostalCodeField: A form field that validates its input as an Israeli
  Seven-digit postal code (since this change to 7 digits from 5 is new, this field also validates currently at 5 digits).

* forms.ILIDNumberField: A form field that validates its input as an
  `Israeli identification number`_. The output will be in the format of a 2-9
  digit number, consisting of a 1-8 digit ID number followed by a single
  checksum digit, calculated using the `Luhn algorithm`_.

  Input may contain an optional hyphen separating the ID number from the
  checksum digit.

* forms.ILMobilePhoneNumberField: A form field that validates its input as a valid Israeli Mobile phone number. including an optional hyphen, parethesis. and all Israeli and Palestinian carriers

.. _Israeli identification number: http://he.wikipedia.org/wiki/%D7%9E%D7%A1%D7%A4%D7%A8_%D7%96%D7%94%D7%95%D7%AA_(%D7%99%D7%A9%D7%A8%D7%90%D7%9C)
.. _Luhn algorithm: http://en.wikipedia.org/wiki/Luhn_algorithm

See the source code for full details.

About localflavors
==================

Django's "localflavor" packages offer additional functionality for particular
countries or cultures.

For example, these might include form fields for your country's postal codes,
phone number formats or government ID numbers.

This code used to live in Django proper -- in django.contrib.localflavor -- but
was separated into standalone packages in Django 1.5 to keep the framework's
core clean.

For a full list of available localflavors, see https://github.com/django/
