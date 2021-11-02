Virt Tools planet site
======================

This directory contains content / configuration for managing

* [http://planet.virttools.org](http://planet.virttools.org)
* [http://planet.virt-tools.org](http://planet.virt-tools.org)

How to add your blog
--------------------

Edit `virt-tools/config.ini` to add section for your blog:

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

How to submit your change
-------------------------

Contribution follows the normal GitLab merge request workflow. If
not already familiar with this, instructions follow below.

The first step is to create a personal fork of the main repository by
visiting:

 * https://gitlab.com/libvirt/virttools-planet/

and selecting the "fork" button. Now checkout the repository, add
your fork and create a local branch for the changes

```
  $ git clone https://gitlab.com/libvirt/virttools-planet
  $ cd virttools-planet
  $ git remote add gitlab ssh://git@gitlab.com/{YOURUSERNAME}/virttools-planet
  $ git checkout -b add-blog
```

Now make the changes described in the previous section and commit them.

Finally push to your fork:

```
  $ git push gitlab add-blog
```

and open a merge request from the web interface.

How to run the site
-------------------

The site is intended to be published with GitLab Pages.

Upon pushing changes to the GitLab repository, CI rules will automatically
build the site and publish the result to the repository's GitLab Pages
site.

A scheduled CI pipeline should also be configured to run once an hour to
refresh the blog feeds.
