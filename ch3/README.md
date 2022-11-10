%title: Cascading Style Sheets
%author: tnguyen21

-> # Cascading Style Sheets <-

Separate content/layout and presentation

---

-> # Anatomy of CSS Rule <-

p {
    font-family: monospace;
    margin: 4px;
}

---

-> # Inheritance <-

some styles inherit
typically ones related to typography and links do
some don't

---

-> # Pseudo-classes <-

a:hover {
    color: blue;
}

---

-> # CSS Problems and Solutions <-

large applications will have _many_ styles

rapidly becomes hard to understand what styles will apply to which elements

modern tooling ecosystems tries to address this in a variety of ways

---

-> # Less/Sass <-

.content {
    ...
    img {
        styles here only apply to images w/in elements with content class
    }

}

---

-> # CSS Frameworks <-

tailwind, bootstrap, etc

minimize how many rules you have to write yourself

simply learn the utilities provided and compose them

steep learning curve

inevitably will need to add custom styles

drives lots of friction if underlying framework not understood well

---

-> `styled-components` and co <-

couple CSS + content + logic in one file/bundle

do some compilation to generate class names and apply them to specific elements

cons
extra compilation step

pros
solves most initial problems without using these tools
