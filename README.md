Virt Tools planet site
======================

This directory contains content / configuration for managing

* [http://planet.virttools.org](http://planet.virttools.org)
* [http://planet.virt-tools.org](http://planet.virt-tools.org)

How to add your blog
--------------------
Add a config.ini section for your blog to `virt-tools/config.ini`:

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
file into the `public/images/` directory if you wish to use an image.

Please send a patch email to `libvir-list@redhat.com`:

```
$ git commit -as
$ git send-email --to libvir-list@redhat.com --cc berrange@redhat.com HEAD^..
```

How to run the site
-------------------

The site is intended to be published with GitLab Pages.

Upon pushing changes to the GitLab repository, CI rules will automatically
build the site and publish the result to the repository's GitLab Pages
site.

A scheduled CI pipeline should also be configured to run once an hour to
refresh the blog feeds.
