Cottage Labs website, powered by Pelican

# Generating and previewing the website

Run the server from the project root
`pelican --listen`

generate content from the project root
`pelican content`

generate styles from `/website_pelican/src/themes/simple/static/scss`
`scss main.scss main.css`

# Generating new page

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

## urls:
- `/{project-name}`

### template:
- project.html

### content:
- projects/{project-name}.md