# Material for MKDocs

In this section we will briefly explain how to update the user guide within this repo. For additional info, check the Material for MKDocs [official guide](https://squidfunk.github.io/mkdocs-material/).

## Update the user guide
To update the user guide, follow these steps:

- Run the `docker-compose.docs.yaml` configuration:

        (root) ➜ docker-compose -f docker-compose.docs.yaml up

- Open the browser at [http://localhost:9000](http://localhost:9000).
- Change the documents within the `docs/docs` folder (this will trigger an auto-reload that will automatically perform changes in the UI)

## Build the user guide
To build the user guide, follow these steps:

- Run the `docker-compose.docs.yaml` configuration:

        (root) ➜ docker-compose -f docker-compose.docs.yaml up

- SSH into the docs container:

        (root) ➜ docker exec -it docs sh

- Build the user guide by running the command:

        /code # mkdocs build

    this command will build the user guide into the `docs/site` folder. This folder can then be used for deployment purposes (this can be deployed, for instance, using an S3 bucket).


## Markdown syntax
This user guide is written using the markdown syntax. In this section we report an optimal set of markdown samples that are useful for the creation of the user guide. For more info, visit [this](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/) link.

!!! tip "Tip"
    To understand how to reproduce the examples given below, it is highly recommended to see `docs/docs/mkdocs.md`.
___
### Formatting
- **Bold**
- _Italic_
- `Code`
- ==Highlight==
- ^^Underline^^
- ~~Strikeout~~
- {--Deleted--}
- {++Added++}
- {~~Prev~>New~~}
- {>>Commented<<}
- <small>Small</small>
- Block:

    {==

    Formatting can also be applied to blocks, by putting the opening and closing
    tags on separate lines and adding new lines between the tags and the content.

    ==}

___
### Admonitions
!!! note "Phasellus posuere in sem ut cursus"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

???+ note "Collapsible admonition"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

??? abstract "Abstract"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

??? info "Info"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

??? tip "Tip"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

??? success "Success"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

??? question "Question"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

??? warning "Warning"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

??? failure "Failure"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

??? danger "Danger"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

??? bug "Bug"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

??? example "Example"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

??? quote "Quote"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!! info inline end "Inline Info"
    Lorem ipsum dolor sit amet, consectetur
    adipiscing elit.

```
# code -> line 1
# code -> line 2
# code -> line 3
# code -> line 4
# code -> line 5
```
___
### Code blocks
``` js
document$.subscribe(function() {
  var tables = document.querySelectorAll("article table")
  tables.forEach(function(table) {
    new Tablesort(table)
  })
})
```
``` python linenums="1"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```
``` python hl_lines="2 3"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```
___
### Content tabs
=== "C"

    ``` c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```

=== "C++"

    ``` c++
    #include <iostream>

    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```

!!! example "Embedded content tabs"

    === "Unordered List"

        _Example_:

        ``` markdown
        * Sed sagittis eleifend rutrum
        * Donec vitae suscipit est
        * Nulla tempor lobortis orci
        ```

        _Result_:

        * Sed sagittis eleifend rutrum
        * Donec vitae suscipit est
        * Nulla tempor lobortis orci

    === "Ordered List"

        _Example_:

        ``` markdown
        1. Sed sagittis eleifend rutrum
        2. Donec vitae suscipit est
        3. Nulla tempor lobortis orci
        ```

        _Result_:

        1. Sed sagittis eleifend rutrum
        2. Donec vitae suscipit est
        3. Nulla tempor lobortis orci
___
### Tables
!!! example

    === "Left"
        | Method      | Description                          |
        | :---------- | :----------------------------------- |
        | `GET`       | :material-check:     Fetch resource  |
        | `PUT`       | :material-check-all: Update resource |
        | `DELETE`    | :material-close:     Delete resource |

    === "Right"
        | Method      | Description                          |
        | ----------: | -----------------------------------: |
        | `GET`       | :material-check:     Fetch resource  |
        | `PUT`       | :material-check-all: Update resource |
        | `DELETE`    | :material-close:     Delete resource |

    === "Center"
        | Method      | Description                          |
        | :---------: | :----------------------------------: |
        | `GET`       | :material-check:     Fetch resource  |
        | `PUT`       | :material-check-all: Update resource |
        | `DELETE`    | :material-close:     Delete resource |

___
### Emoji & Icons
- :smile:
- :material-account-circle: – `.icons/material/account-circle.svg`
- :fontawesome-regular-laugh-wink: – `.icons/fontawesome/regular/laugh-wink.svg`
- :octicons-repo-push-24: – `.icons/octicons/repo-push-24.svg`
___
### Links
- Link to [markdown guide](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/)
- Link to [**Update the user guide section**](#update-the-user-guide)
- Link to [_Introduction_](index.md)
- Link to [Introduction :fontawesome-regular-arrow-alt-circle-right: Start the project](index.md#start-the-project)
___
### Footnotes
Lorem ipsum[^1] dolor sit amet, consectetur adipiscing elit[^2].

[^1]: Lorem ipsum dolor sit amet, consectetur adipiscing elit.

[^2]:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
___
### Abbreviations
The HTML specification is maintained by the W3C.

*[HTML]: Hyper Text Markup Language
*[W3C]: World Wide Web Consortium
___
### Lists
* Indented code block:
    ``` python linenums="1"
    def bubble_sort(items):
        for i in range(len(items)):
            for j in range(len(items) - 1 - i):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
    ```

* Indented quote block:

    !!! quote "Quote"
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
        nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
        massa, nec semper lorem quam in massa.

    Additional paragraph within this list item.

* Nested (ordered/unordered) list:
    1. first
    2. second
        * unordered item
        * another unordered item

`Lorem ipsum dolor sit amet`
:   Sed sagittis eleifend rutrum. Donec vitae suscipit est. Nullam tempus
    tellus non sem sollicitudin, quis rutrum leo facilisis.

`Cras arcu libero`
:   Aliquam metus eros, pretium sed nulla venenatis, faucibus auctor ex. Proin
    ut eros sed sapien ullamcorper consequat. Nunc ligula ante.

- [x] Lorem ipsum dolor sit amet, consectetur adipiscing elit
- [ ] Vestibulum convallis sit amet nisi a tincidunt
    * [x] In hac habitasse platea dictumst
    * [x] In scelerisque nibh non dolor mollis congue sed et metus
    * [ ] Praesent sed risus massa
- [ ] Aenean pretium efficitur erat, donec pharetra, ligula non scelerisque
___
### Images
![Placeholder](https://dummyimage.com/600x400/eee/aaa)

![Logo](img/logo.png)

<figure>
  <img src="../img/gif-example.gif" alt="GIF example" style="width: 600">
  <figcaption><small>Fig.1 - GIF example with caption.</small></figcaption>
</figure>
___
### MathJax
[MathJax](https://www.mathjax.org/) is a beautiful and accessible way to display mathematical content in the browser.

Mathematical expression using block syntax:

$$
\operatorname{ker} f=\{g\in G:f(g)=e_{H}\}{\mbox{.}}
$$

Mathematical expression using inline syntax:

!!! quote ""
    The homomorphism $f$ is injective if and only if its kernel is only the singleton set $e_G$, because otherwise $\exists a,b\in G$ with $a\neq b$ such that $f(a)=f(b)$.
