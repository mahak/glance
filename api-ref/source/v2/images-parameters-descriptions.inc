.. |p-start| raw:: html

    <p>

.. |p-end| raw:: html

    </p>

.. |html-br| raw:: html

    <br />

.. |disk_format_description| replace::
    |p-start|\ The format of the disk.\ |p-end|
    |p-start|\ Values may vary based on the configuration available in a
    particular OpenStack cloud. See the :ref:`Image Schema <image-schema>`
    response from the cloud itself for the valid values available.  See
    `Disk Format
    <https://docs.openstack.org/glance/latest/user/formats.html#disk-format>`__
    in the Glance documentation for more information.\ |p-end|
    |p-start|\ Example formats are: ``ami``, ``ari``, ``aki``, ``vhd``,
    ``vhdx``, ``vmdk``, ``raw``, ``qcow2``, ``vdi``, ``ploop`` or
    ``iso``.\ |p-end|
    |p-start|\ The value might be ``null`` (JSON null data type).\ |p-end|
    |p-start|\
    **Newton changes**: The ``vhdx`` disk format is a supported
    value.\ |html-br|
    **Ocata changes**: The ``ploop`` disk format is a supported
    value.\ |p-end|

.. |container_format_description| replace::
    |p-start|\ Format of the image container.\ |p-end|
    |p-start|\ Values may vary based on the configuration available in a
    particular OpenStack cloud. See the :ref:`Image Schema <image-schema>`
    response from the cloud itself for the valid values available.  See
    `Container Format
    <https://docs.openstack.org/glance/latest/user/formats.html#container-format>`__
    in the Glance documentation for more information.\ |p-end|
    |p-start|\ Example formats are: ``ami``, ``ari``, ``aki``, ``bare``,
    ``ovf``, ``ova``, ``docker``, or ``compressed``.\ |p-end|
    |p-start|\ The value might be ``null`` (JSON null data type).\ |p-end|
    |p-start|\
    **Train changes**: The ``compressed`` container format is a supported
    value.\ |p-end|
