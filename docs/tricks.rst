.. Copyright (c) 2015 Pietro Albini <pietro@pietroalbini.io>
   Released under the MIT license

.. _tricks:

~~~~~~~~~~~~~~~
Tips and tricks
~~~~~~~~~~~~~~~

The whole point of botogram is to make your life easier when creating Telegram
bots. In order to do so in a better way, there are some tricks you can use to
speed the development up.

.. _tricks-dynamic-arguments:

=================
Dynamic arguments
=================

There are a lot of information and methods you can get from every decorator,
but you don't always need them. botogram is smart enough to know which
arguments you want and in which order you want them. This means you can request
only the ones you need:

.. code-block:: python

   @botogram.command("test")
   def test(args, chat):
       chat.send(" ".join(args))

By default, the :py:meth:`~botogram.Bot.command` decorator provides three
arguments: ``chat``, ``message`` and ``args``. Instead, the function above
requested only two of them, and botogram is able to provide only them in the
right order.

Please remember this will work only if a function is called directly by
botogram (for example when a command is issued by an user). If you call it by
hand, you'll need to provide the arguments by hand.

There are some extra arguments you can request from every function called by
botogram, without being directly provided by the decorator:

* **bot**, which is an instance of the current bot.

* **shared**, which is an instance of the bot's
  :ref:`shared memory <shared-memory>`.