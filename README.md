Virt Tools planet site
======================

This directory contains content / configuration for managing

* [http://planet.virttools.org](http://planet.virttools.org)
* [http://planet.virt-tools.org](http://planet.virt-tools.org)

How to add your blog
--------------------
Add a config.ini section for your blog to `updater/virt-tools/config.ini`:

```
[https://example.org/my/blog/feed/]
name = John Doe
face = jdoe.png
facewidth = 96
faceheight = 96
```

Where `face` (logo image filename), `facewidth` (logo image width in pixels),
and `faceheight` (logo image height in pixels) are optional attributes that
describe the logo image associated with your blog.  Remember to add your image
file into the `updater/virt-tools/images/` directory if you wish to use an
image.

Please send a patch email to `libvir-list@redhat.com`:

```
$ git commit -as
$ git send-email --to libvir-list@redhat.com --cc berrange@redhat.com HEAD^..
```

How to run the site
-------------------

The site is setup to run under OpenShift

Initial load can be done with

```
oc process -f openshift/templates/virttools-planet.json  | oc create -f -
```

Updates to the OpenShift config are manually activated using `oc replace`.

Updates to the content itself are automatically propagated via a planet hook.
