Cottage Labs website, powered by Pelican

# Generating and previewing the website

Create a virtualenv, if you like. **Requires Python 3.12**

Install `pelican` with
```
pip install pelican pelican-yaml-metadata pelican-css-cache-bust
```
Generate content from the project root with the command
`pelican content`
We commit the resulting HTML from the build (under `output/`) into the repo so it can be served immediately from the repo on the server.

Run the server from the project root
`pelican --listen`

For development you can use auto-reload mode so you can see changes immediately in browser:
`pelican --autoreload --listen`

Install sass with e.g.
`sudo apt install ruby-sass`

Generate styles from `themes/simple/static/scss`

```scss main.scss main.css```

# Generating new pages

## To add new project page:
- Add the content file `.md` to the `/content/projects` folder
- add required metadata to the header: title, tags (this will allow the project to be found by the project browser), template (`project`)

## To add any other page:
- Add the content file '.md' to the '/content/pages' folder
- add required metadata to the header: title (**"That Page" will translate to `/that-page` url**), template

## optional
- Create `.html` template in `/themes/simple/static/templates`
- Create link in `nav.html`


# Pages:

- `templates` can be found in `src/themes/simple/static/templates`
- `content` can be found in `src/content/pages`
- images referenced from the content should be added to `content/images` and can be referenced by `{static}/images`
- images referenced from the theme (templates and scss files) should be added to `themes/simple/static/images` and can be referenced by `{{ SITEURL }}/{{ THEME_STATIC_DIR }}/images/` (from the template) and `url("../images/[...]");` (from the stylesheet)
- folder `output` is autogenerated

## Resizing images

**Please** resize images _before_ committing them to the repo, this will reduce repo bloat and maintain site performance.

To resize all images in a directory, e.g. to a maximum size of 1024px in either dimension, use the `imagemagick mogrify` tool:

```
mogrify -resize 1024x1024 *.jpg
```

## Homepage `/`

### templates:
- index.html

### content:
- _to do: how to add content in md file to index page?_


## About Us `/about`

### templates:
- about.html
- partners.html
- registration.html

### content:
- about.md
- partners.md
- registration.md



## Lifecycle Pages:

### urls:
- `/data-lifecycle`
- `/project-lifecycle`

### templates:
- lifecycles.html

### content:
- datalifecycle.md
- projectlifecycle.md



## Expertiese Pages:

### urls:
- `/data-visualisation`
- `/data-repositories`
- `/bespoke-development`
- `/open-access-infrastructure`

### templates:
- expertise.html

### content:
- datavisualisation.md
- datarepositories.md
- bespokedevelopment.md
- oainfrastructure.md


## Projects' Pages

### urls:
- `/{project-name}`

### template:
- `project.html`

### content:
- `projects/{project-name}.md`

### logos:
- `themes/simple/static/images/projects`

### screenshots:
- `themes/simple/static/screenshots`

## Projects Browser

### urls:
- `/projects`
- `/projects/{technology}`

### templates:
- `tags.html`
- `tag.html`
- `browser.html`

## Themes tags:

### see `src/themes/simple/templates/partials/_tags.html` for slugs and tags' names

# Deployment on next.cottagelabs.com

This is managed using git hooks. You'll need the server in your ```.ssh/config``` file,
and run the following from your local checked-out repo to add the remote:

    git remote add next cloo@sauron:next.cottagelabs.com.git

You can only deploy the master branch. To do so, run the following command:

    git push next master

i.e. you are pushing master to the remote repo on machine `sauron`. This will run the hooks, and
restart ```nginx``` for you to pick up the changes.

## Server configuration

Requires a bare git repo on the host, e.g. called ```next.cottagelabs.com.git```. This is created
with ```git init --bare next.cottagelabs.com.git``` in the home directory.

Create the working tree directory where nginx will serve the files from and fix the
permissions:

    sudo mkdir /var/www/next.cottagelabs.com
    sudo chown www-data:www-data /var/www/next.cottagelabs.com
    sudo chmod -R 775 /var/www
    sudo usermod -a -G www-data cloo

The post receive hook then needs to be created on the host, by copying
```deploy/hooks/post-receive``` to ```~/next.cottagelabs.com.git/hooks/post-receive``` and
```chmod +x hooks/post-receive``` on the host. This will allow the script to run on
deploy and copy the code to the correct work tree.

Afterwards, replace the copied hook with a symlink to the checked out hook (so you can update the hooks):

    ln -sf /var/www/next.cottagelabs.com/deploy/hooks/post-receive hooks/post-receive
    chmod +x hooks/post-receive

# Deployment on cottagelabs.com

Set up server as above, but with `production` instead of `next`, and a host set up for `cottagelabs.com`:

    git remote add production cloo@cl-docker:cottagelabs.com.git
    git push production master

Also, use the `-production` hook which is hardcoded for `cottagelabs.com`, along with its corresponding `nginx` config.

## SSL Certificates

The nginx config expects an SSL certificate - this should be created via LetsEncrypt / certbot.

To use the nginx config, symlink it within `/etc/nginx/sites-available` and add a symlink to that one inside `/etc/nginx/sites-enabled`.

e.g.
```
sudo ln -s /var/www/next.cottagelabs.com/deploy/nginx/next.cottagelabs.com /etc/nginx/sites-available/next.cottagelabs.com
```